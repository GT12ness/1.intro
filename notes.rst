Introduction
############

Types
=====

- ``bool`` - logical (binary) - ``True`` or ``False``
- ``int`` - integer, i.e. ``1``, ``-983``
- ``float`` - floating-point number, i.e. ``1.0``, ``3.14``, ``-0.123``
- ``str`` - string (text), can be enclosed in single quotes ``'foo'``, or double quotes ``"bar"``,
  special chars (like quotes) can be escaped using ``\``, i.e. ``"\"We'll be there,\" said Ron."``

Operators
=========

Arithmetic
----------

- ``+``, addition (also works for ``str``), ``1 + 2.1 -> 3.1``, ``'ab' + 'cd' -> 'abcd'``
- ``-``, subtraction, ``3.1 - 2.1 -> 1.0``, ``3 - 2 -> 1``
- ``*``, product (works between ``str`` and ``int``), ``3 * 2.1`` -> 6.3``, ``3 * 'a' -> 'aaa'``
- ``**``, power, ``2 ** 3 -> 8``, ``4 ** (1/2) -> 2``
- ``/``, division (always returns ``float``) ``3 / 2 -> 1.5``, ``2 / 1 -> 2.0``
- ``//``, floor division, ``9 // 2 -> 4``, ``9.0 // 2.0 -> 4.0``, ``-9 // 2 -> -5``
- ``%``, modulus, ``9 % 2 -> 1``, ``9 % 3 -> 0``


Comparison
----------
Result is always bool (``True`` or ``False``)

- ``==``, equals, ``1 == 1.0 -> True``, ``2 == 1 -> False``
- ``!=``, not equal (opposite of ``==``), ``1 != 1.0 -> False``, ``2 != 1 -> True``
- ``>``, greater than, ``1 > 1 -> False``, ``2 > 1.0 -> True``
- ``<``, less than, ``1 < 1 -> False``, ``2 < 1.0 -> False``
- ``>=``, greater than or equal to, ``1 >= 1 -> True``, ``2 >= 1.0 -> True``
- ``<=``, less than or equal to, ``1 <= 1 -> True``, ``2 <= 1.0 -> False``

Remark: various types are comparable to each other, i.e.
  ``1 == 1.0 -> True``, ``1 == True -> True``, ``1 == "1" -> False``

Logical
-------
Logical expression may seem a little bit tricky at first, but it is all logical :)
Every primitive value or basic data structure is evaluated either true or false by following rules

- Values considered false: ``False``, ``0``, ``0.0``, ``""``, ``()``, ``[]``, ``{}``, ``set()``
- Values considered true: ``True``, nonzero ``int``, nonzero ``float``, nonempty ``str``, nonempty ``tulpe``,
  nonempty ``list``, nonempty ``dict``, nonempty ``set``

- ``not`` - negation, always bool result, ``not True -> False``, ``not 0 -> True``, ``not 12 -> False``
- ``and`` - lazy evaluation, returns one of the operands. Expression ``a and b`` will be

    - ``a``, if ``a`` is false (``b`` is not evaluated at all), i.e. ``0.0 and (1/0) -> 0.0``
    - ``b``, if ``a`` is true, ``2 and -3 -> -3``

- ``or`` - lazy evaluation, returns one of the operands. Expression ``a or b`` will be

    - ``a``, if ``a`` is true (``b`` is not evaluated at all), i.e. ``12 or (1/0) -> 12``
    - ``b``, if ``a`` is false, ``False or -3 -> -3``, ``False or 0 -> 0``

Variables
=========

- ``=`` is used for variable assignment, i.e. ``a = 2`` will assign value ``2`` to variable ``a``.
- no declaration is needed
- variable is only reference therefore it is n

Syntactic sugar for updates
---------------------------
Let ``a``, ``b`` be variables with some value assigned, then

- ``a += b``, is same as ``a = a + b``
- ``a -= b``, is same as ``a = a - b``
- ``a *= b``, is same as ``a = a * b``
- ``a /= b``, is same as ``a = a / b``
- ``a **= b``, is same as ``a = a ** b``

Executing python script
=======================

Suppose we have a python script ``hello.py`` saved as ``"C:\\users\my documents\gt12ness\hello.py"``

Command line
------------

- open command line (``start -> <type "cmd"> -> select it``)
- type: ``python "C:\\users\my documents\gt12ness\hello.py"``

IDLE (python GUI)
-----------------

- open IDLE (python GUI) (``start -> <type "python"> -> select it``)
- open ``hello.py`` (using top menu ``file -> open -> <find and select "C:\\users\my documents\gt12ness\hello.py">``)
- run opened script (``F5`` or ``run -> Run Module``)



Flow control
############
In order to loop and branch our programs we use some flow control statements.
This chapter is almost completely copy-pasted from https://docs.python.org/3/tutorial/controlflow.html


Syntax
======
To mark block of code as part of branch or cycle, python requires both

1. the colon ``:`` at the end of the flow control statement
2. indentation of following code block (any indentation is sufficient, tab or 4 spaces are preferred)

Otherwise, syntax error will be raised by interpreter. Notice this syntax on following examples

if statements
=============
Perhaps the most well-known statement type is the if statement. For example:

>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More


There can be zero or more elif parts, and the else part is optional.
The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.
An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.

while statements
================
The while loop executes as long as the condition (here: b < 10) remains true.
In Python, like in C, any non-zero integer value is true; zero is false.
The condition may also be a string or list value, in fact any sequence;
anything with a non-zero length is true, empty sequences are false.

>>> a, b = 0, 1
>>> while b < 1000:
...     print(b, end=',')
...     a, b = b, a+b
...
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,


break and continue Statements, and else Clauses on Loops
========================================================
The break statement, like in C, breaks out of the innermost enclosing for or while loop.

Loop statements may have an else clause; it is executed when the loop terminates through
exhaustion of the list (with for) or when the condition becomes false (with while),
but not when the loop is terminated by a break statement.
This is exemplified by the following loop, which searches for prime numbers:

>>>
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

(Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement.)

When used with a loop, the else clause has more in common with the else clause of a try statement than it does that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs. For more on the try statement and exceptions, see Handling Exceptions.

The continue statement, also borrowed from C, continues with the next iteration of the loop:

>>>
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found a number", num)
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9

pass Statements
===============
The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

>>>
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
This is commonly used for creating minimal classes:

>>>
>>> class MyEmptyClass:
...     pass
...
Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The pass is silently ignored:

>>>
>>> def initlog(*args):
...     pass   # Remember to implement this!
...

