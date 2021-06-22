
# Documentation

https://docs.pytest.org/en/latest/getting-started.html

# Run tests

Usage:

```console
$ pytest [options] [file_or_dir] [file_or_dir] [...]
```

Success example:

```console
$ pytest testing/mypytests
$ pytest testing/mypytests/test_0_myadd.py
```

# Capture output

https://docs.pytest.org/en/6.2.x/capture.html

Extra summary info can be shown using the '-r' option:

```console
$ pytest --help | rg -e -r -C 3
  -r chars              show extra test summary info as specified by chars:
                        (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
                        (p)assed, (P)assed with output, (a)ll except passed
                        (p/P), or (A)ll. Warnings are displayed at all times
```

shows the captured output of passed tests:

```console
$ pytest -rP
```

shows the captured output of failed tests (default behaviour):

```console
$ pytest -rx
```

`-s` allows seeing output as is.

