# Python environment - README

<!-- TOC -->

- [Python environment - README](#python-environment---readme)
- [Creating a new environment for SMM692](#creating-a-new-environment-for-smm692)
  - [Using Conda](#using-conda)
  - [Using pure 'Python'](#using-pure-python)

<!-- /TOC -->

# Creating a new environment for SMM692

## Using Conda

A new environment can be created using:

+ the graphical user interface, namely, Anaconda Navigator
+ the command line

If you go with the latter:

```{bash}
$ conda create -n smm692 python=3.x
````

To enact `smm692`:

```{bash}
$ conda activate smm692
```

When it comes to populate `smm692`, there are two options
– surprise-surprise:

+ browsing the Anaconda channels and 'ticking' stuff with the graphical user interface
+ *ibidem*, command line

If you go with the latter:

```{bash}
$ conda install numpy
```

Sometimes, the list of target variables is included in a text file (good practice – it improves code reproducibility):

```{bash}
$ conda install --file requirements.txt
```

If you aren't sure about the name of the target library or you want to browse the Anaconda channels:

```{bash}
$ conda search numpy
```

A set of items (if any) will be displayed on the terminal – now you've made sure about the name of the library (libraries) to install.

## Using pure 'Python'

The command line is the route to go down. Create the `venv` module of Python to create a new environment:

```{bash}
$ python3 -m venv smm692
```

It's time to activate the environment using the `activate` script that the `venv` module creates by default:

```{bash}
$ source smm692/bin/activate
```

To populate `smm692`:

```{bash}
(smm692) $ pip install -r requirements.txt
```
