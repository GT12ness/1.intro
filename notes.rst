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
