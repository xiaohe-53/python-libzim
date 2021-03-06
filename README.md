# python-libzim

The Python-libzim package allows you to read/write [ZIM
files](https://openzim.org) in Python. It provides a shallow Python
interface on top of the [`libzim`](https://github.com/openzim/libzim)
C++ library.

It is primarily used in openZIM scrapers like for example
[`Sotoki`](https://github.com/openzim/sotoki) or
[`Youtube2zim`](https://github.com/openzim/youtube).

Read [CONTRIBUTING.md](./CONTRIBUTING.md) to know more about
Python-libzim development.

[![Build Status](https://github.com/openzim/python-libzim/workflows/test/badge.svg?query=branch%3Amaster)](https://github.com/openzim/python-libzim/actions?query=branch%3Amaster)
[![CodeFactor](https://www.codefactor.io/repository/github/openzim/python-libzim/badge)](https://www.codefactor.io/repository/github/openzim/python-libzim)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![PyPI version shields.io](https://img.shields.io/pypi/v/libzim.svg)](https://pypi.org/project/libzim/)
[![codecov](https://codecov.io/gh/openzim/python-libzim/branch/master/graph/badge.svg)](https://codecov.io/gh/openzim/python-libzim)

## Installation

The [PyPI package](https://pypi.org/project/libzim/) is bundled with a
recent version of the libzim for macOS and GNU/Linux (x86_64
architecture). For other OSes, the latest libzim has to be
compiled manually, See [Setup hints](#setup-hints) to know more.

```bash
pip3 install libzim
```

## Quickstart

### Read a ZIM

```python
from libzim.reader import Archive

zim = Archive("test.zim")
print(f"Main entry is at {zim.main_entry.get_item().path}")
entry = zim.get_entry_by_path("path/to/my-article")
print(f"Entry {entry.title} at {entry.path} is {entry.get_item().size}b:")
print(bytes(entry.get_item().content).decode("UTF-8"))
```

### Write a ZIM

See [example](examples/basic_writer.py) for a basic usage of the
writer API.

## Setup hints

### Installing the `libzim` dylib and headers manually

If you have to install the libzim manually, you will have to [compile
`libzim` from
source](https://github.com/openzim/libzim). This binding has been designed
to work with the latest version of the libzim, we only recommend to
use it with latest released version.

If you have not installed libzim in standard directory, you will have
to set `LD_LIBRARY_PATH` to allow python to find the library. Assuming
you have extracted (or installed) the library if LIBZIM_DIR:

```bash
export LD_LIBRARY_PATH="${LIBZIM_DIR}/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"
```

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0) or later, see
[LICENSE](LICENSE) for more details.
