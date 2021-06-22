
# Documentation

[Official documentation](https://docs.python.org/2.7/library/unittest.html)

# Run tests

Run unit tests:



Success example:

```console
$ python -m unittest discover -s tests/myunittests
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Failure example:

```console
$ python -m unittest discover -s tests/myunittests
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
$ python -m unittest discover -s tests/myunittests -v
test_existent (test_checkfile.TestMCheckFile) ... ok
test_nonexistent (test_checkfile.TestMCheckFile) ... ok
test_myadd (test_myadd.TestMyAdd) ... ok
test_myadd_complex (test_myadd.TestMyAdd) ... skipped 'Unimplemented'

----------------------------------------------------------------------
Ran 4 tests in 0.008s

OK (skipped=1)
```

# Coverage

Measure coverage:

```console
$ coverage run -m unittest discover -s tests/myunittests
```

Show report:

```console
$ coverage report -m
Name                                  Stmts   Miss  Cover   Missing
-------------------------------------------------------------------
tests\__init__.py                         0      0   100%
tests\myfuncs.py                         11      4    64%   6, 11-13
tests\myunittests\test_checkfile.py      14      0   100%
tests\myunittests\test_myadd.py          11      1    91%   24
-------------------------------------------------------------------
TOTAL                                    36      5    86%
```

Generate HTML report:

```console
$ coverage html
$ chrome demo/htmlcov/index.html
```
