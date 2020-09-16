# Python walk-through

Presentation given in the 2020/21 induction week.

# Agenda

<!-- vim-markdown-toc GFM -->

* [Getting started with Python](#getting-started-with-python)
    * [How to get Python](#how-to-get-python)
    * [OS-specific considerations](#os-specific-considerations)
* [Interacting with Python](#interacting-with-python)
    * [Interactive Python shell](#interactive-python-shell)
    * [Interactive IPython shell](#interactive-ipython-shell)
    * [Editing Python scripts – text editors](#editing-python-scripts--text-editors)
        * [Vim/Neovim](#vimneovim)
        * [Atom](#atom)
    * [Full-fledged IDEs](#full-fledged-ides)
        * [PyCharm](#pycharm)
        * [Spyder](#spyder)
    * [Jupyter *](#jupyter-)
* [Managing Python environment](#managing-python-environment)

<!-- vim-markdown-toc -->

# Getting started with Python

Installing a copy of Python on your machine is easy!

## How to get Python

+ download your copy of Python from the [official website](https://www.python.org/downloads/) of the project
+ download Python along with a bundle of packages for data science + package manager – e.g.:
  - [Enthought's Canopy](https://www.enthought.com/)
  - [Anaconda](https://www.anaconda.com/)

## OS-specific considerations

+ Python is a cross-platform software – i.e., the code is portable
+ ... however, installing 'complex' Python packages – e.g., libraries that build on C++ 
  libraries – in Windows is not a piece of cake:
  - Win users are warmly invited to install [WSL*](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

# Interacting with Python

There are several ways to interact with Python – let's avoid the boring ones.

## Interactive Python shell

+ step 1: open a terminal session
+ step 2: launch python
+ step 3: get bored

## Interactive IPython shell

+ step 1: open a terminal session
+ step 2: launch ipython
+ step 3: enjoy the autocompletion service and other great features offered by IPython

## Editing Python scripts – text editors

There old, powerful text editors and some rising stars – both categories have
their own strengths and weaknesses

### Vim/Neovim

+ pros:
  + most flexible, powerful editor on the market
  + impressive variety of plugins
  + fast
+ cons:
  + the learning curve is a little bit steep

### Atom

+ pros:
  + it goes well with GitHub
  + impressive variety of plugins
+ cons:
  + some plugins are buggy
  + slower than Vim/Neovim

## Full-fledged IDEs

Some users/developers like complex consoles and lots of buttons – are you a control
freak?


### PyCharm

+ best in class IDE on the market
+ largest, most distinctive set of features ever assembled in a Python IDE
+ great selection of plugins
+ it crosses the Python-R charm

### Spyder

+ lightweight IDE
+ very popular in the scientific community
+ it mirrors the layout of RStudio

## Jupyter *

+ Jupyter notebook/lab are a natural entry point for newbies
+ everything's in one place
+ no/minimal configuration costs
+ want to focus on coding? Yup
+ lot of power brought to you by software running behind the scences
+ great for reproducibility

# Managing Python environment

Want to do serious stuff with Python? Create a Python environment first.

