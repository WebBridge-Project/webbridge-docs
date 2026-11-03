# webbridge-tools

[webbridge-tools](https://pypi.org/project/webbridge-tools/) is
the Python code generator for webbridge. It reads your C++ classes and
writes the code that connects them to JavaScript, so you don't have to write
that glue code by hand.

It's a separate, pip-installable package from `webbridge-runtime` because
the two have different dependencies and release on their own schedules.
Install it with:

```bash
pip install webbridge-tools
```

See [Getting Started](getting-started.md) for wiring it into CMake, and
[CLI Reference](cli.md) / [Python API](tools-api.rst) for the generator itself.

```{toctree}
:maxdepth: 2
:hidden:

CLI Reference <cli>
Python API Reference <tools-api>
```
