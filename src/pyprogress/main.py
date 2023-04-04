import sys
from datetime import datetime


class ProgressBar():
    def __init__(self, max_iterations, start_iteration=0, num_divisions=25, loaded_symbol="=", empty_symbol="-") -> None:
        self.max_iterations = max_iterations
        self.num_divisions = num_divisions
        self.iteration = start_iteration
        self.loaded = loaded_symbol
        self.empty = empty_symbol
        self.message_length = 72
        self._division = 100//self.num_divisions
        self.message_remove_at = None
        self.message_remove_iter = None
        self.message = None
        self.previous_state = None

    def set_message(self, message, *, time=None, iterations=None) -> None:
        if self.message == None:
            if time or iterations == time:
                self.message_remove_at = datetime.now().timestamp()+time
            elif time or iterations == iterations:
                self.message_remove_iter = self.iteration+iterations
            self.message = message

    def update(self) -> None:
        self.iteration += 1
        if self.message_remove_at != None:
            if datetime.now().timestamp() >= self.message_remove_at:
                self.message = None
        elif self.message_remove_iter != None:
            if self.iteration >= self.message_remove_iter:
                self.message = None

    def print(self):
        if self.iteration == self.max_iterations:
            return self.clear()
        if str(self.display_bar) != str(self.previous_state):
            self.previous_state = self.display_bar
            self.clear()
            return self._print(self.display_bar)

    def clear(self):
        self._print(" "*self.message_length)

    def _print(self, string, end="\r", start="\r"):
        sys.stdout.write(start+string[:self.message_length]+" "*(len(string[:self.message_length])//2)+end)
        sys.stdout.flush()
    
    @property
    def display_bar(self):
        return f"[{self.loaded*self.divisions}{self.empty*(self.num_divisions-self.divisions)}] - {self.percentage}% {self.display_message}"
    
    @property
    def display_message(self):
        return f"| {self.message}" if self.message != None else ""
    
    @property
    def divisions(self):
        return self.percentage//self.division
    
    @property
    def percentage(self):
        return round(self.iteration/self.max_iterations*100)
    
    @property
    def division(self):
        return self._division