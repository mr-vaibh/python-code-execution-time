exec-time
=====
`Downloads <https://pepy.tech/project/exec-time>`_
|
`License: MIT <https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mr-vaibh/python-code-execution-time/blob/master/LICENSE>`_

A code snippet used to compare execution time of two Python code

Installation
-----

You should be able to install using ``pip`` in the usual ways:

.. code:: sh

    $ pip install exec-time


Or just clone this repository and run:

.. code:: sh

    $ python setup.py install

Or place the `exec-time` folder that you downloaded somewhere where it can be accessed by your scripts.

Usage
-----

Add your code snippets in `first_func` and `second_func` respectively for comparison

.. code:: python

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

.. code:: python

    # === OUTPUT ===
    # first_func function executed in : 0.32839999767020345 mil sec
    # second_func function executed in : 0.006199989002197981 mil sec


That's it, enjoy 🍷
