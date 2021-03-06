ml
==

Learning about machine learning in Python: Walking before you Run

This is dedicated to learning machine learning. All of the algorithms that here are well known and studied algorithms 
with multiple implementations. There is a good chance that these algorithms are implemented better in a number of machine learning packages such as:

1. [Scikit Learn](http://scikit-learn.org/stable/)
2. [Weka](http://www.cs.waikato.ac.nz/ml/weka/)

If you are planning on implementing these algorithms yourself, I highly recommend basing your implementations off of one of these libraries if you 
can not use the library directly.

This project is meant for learning. That means that the implementations here will be as well documented and easy to follow as possible. Each 
project will have an associated article explaining it.

The [Scikit-Learn tutorial page](http://scikit-learn.org/stable/auto_examples/index.html) is an absolutely amazing resource, but I feel that it is simply
too hard to learn code by staring at code. You need to step through it and see how it works at every level to understand its purpose and function, which is the
primary purpose of this project.

# Building this project
This project has the following dependencies:

* Python 2.7

* Pip

* virtualenv

Once you have these requirements, you can pull the repository and execute the following shell script from the root of the project:
```
virtualenv .                        # Initialize the virtual environment to your current directory
pip install -r requirements.txt     # Install ther required python dependencies
```
