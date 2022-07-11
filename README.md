exec-time documentation
=====

*"kamaal hai!, ab DOCS bhi mai hi likhu? "*

**exec-time** is a very tiny package which provides a decorator that helps you
measure the execution time (in milliseconds) of functions.

PYPI official page: <https://pypi.org/project/exec-time/>

[![image](https://static.pepy.tech/personalized-badge/exec-time?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/exec-time)
[![image](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mr-vaibh/python-code-execution-time/blob/master/LICENSE)

Installation
-----

You should be able to install using `pip` in the usual ways:

`$ pip install exec-time`

Or just clone this repository and run:

`$ python setup.py install`

Or place the [exec-time]{.title-ref} folder that you downloaded
somewhere where it can be accessed by your scripts.

Usage
=====

Add your code snippets in `first_func` and `second_func` respectively for comparison

``` {.python}
# === USAGE ===
@exec_time
def first_func():
    '''Here goes function 1'''
    x = 0
    for i in range(1, 10001):
        x += 10

@exec_time
def second_func():
    '''Here goes function 2'''
    x = 0
    for i in range(1, 101):
        x += 10

first_func()
second_func()
```

``` {.python}
# === OUTPUT ===
# first_func function executed in : 0.32839999767020345 mil sec
# second_func function executed in : 0.006199989002197981 mil sec
```

That\'s it, enjoy 🍷
