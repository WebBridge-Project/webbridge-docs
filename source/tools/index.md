# webbridge-tools

```{note}
Not yet published to PyPI. Until it is, install directly from its GitHub
repo instead of `pip install webbridge-tools`:
`pip install git+https://github.com/WebBridge-Project/webbridge-tools.git`
```

[webbridge-tools](https://github.com/WebBridge-Project/webbridge-tools) is
the Python code generator for webbridge: it reads your C++ classes that
inherit from `webbridge::object` and emits the C++ registration headers and
TypeScript type definitions that wire them up to JavaScript. Code generation
exists because C++26 reflection isn't available yet.

It's deliberately a separate, pip-installable package rather than something
bundled into the `webbridge-runtime` Conan package — the generator has its
own dependencies (tree-sitter, Jinja2) and its own release cadence,
independent of the C++ library it generates code for. Once published,
installing it will be:

```bash
pip install webbridge-tools
```

See [Getting Started](../getting-started.md) for wiring it into CMake, and
[CLI Reference](cli.md) / [Python API](api.rst) for the generator itself.

## How it fits together

1. You write a C++ class inheriting from `webbridge::object` (see
   [Minimal Example](../examples.md)).
2. `webbridge_generate()` (a CMake function provided by this package) calls
   the generator automatically as part of your build.
3. The generator uses **tree-sitter** to parse the C++ header, extracting
   properties, events, methods and constants.
4. It renders, via Jinja2 templates, a `_registration.h` file (C++) and the
   matching TypeScript bindings.
5. You `#include` the generated header and call `webbridge::register_type<T>()`.
