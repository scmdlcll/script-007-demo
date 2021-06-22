
# Documentation

[Official documentation](https://docs.python.org/2.7/library/unittest.html)

# Run tests

Run unit tests:



Success example:

```console
$ python -m unittest discover -s Testing/myunittests
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Failure example:

```console
python -m unittest discover -s Testing/myunittests
F
======================================================================
FAIL: test_fsub (test_01.TestMyFuncs)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Work\TC\Trainings\My\python\script-007\demo\Testing\myunittests\test_01.py", line 17, in test_fsub
    self.assertEqual(a + b, c)
AssertionError: 16 != 6

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

Flag `-v` show test files:

```console
```
