from setuptools import setup, find_packages

setup(
    name = 'pyprogressbar', 
    version = '0.0.3',
    description = 'An utility package that gives you the ability to easily create custom progress bars without anything redundant.',
    py_modules = ["main"],
    package_dir = {'':'src'},
    author = 'PolyTree18(sh4r)',
    author_email = 'sandalovir@gmail.com',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    url='https://github.com/PolyTree18/pyprogress',
    include_package_data=True,
    classifiers  = [
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Topic :: Printing',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent'
    ],
    
    install_requires = [],
    keywords = ['Progress bar', 'Loading bar'],
    packages = find_packages()
)