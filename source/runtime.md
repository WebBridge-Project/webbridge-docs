# webbridge-runtime

```{note}
Not available for outside users yet: `webbridge-runtime` is only published
to a private Conan server (login required), not ConanCenter, so the install
step below won't resolve until it's published more broadly.
```

[webbridge-runtime](https://github.com/WebBridge-Project/webbridge-runtime) is
the C++ library for webbridge: `webbridge::object`, properties, events,
constants, error handling, and the
[webview](https://github.com/webview/webview)-based bridge to JavaScript.
Distributed as a Conan 2 package.

```python
# conanfile.py
def requirements(self):
    self.requires("webbridge/0.1.0")
```

See [Getting Started](getting-started.md) for adding the Conan remote and
wiring it into CMake, and [Concepts](concepts.md) / [Examples](examples.md) /
[C++ API Reference](cpp-api.rst) for the library itself.
