# webbridge

```{note}
Public availability is still in progress. `webbridge-runtime` is currently
only published to a private Conan server, and `webbridge-tools` hasn't been
published to PyPI yet (only installable from its GitHub repo). The install
steps on this site describe the intended workflow once both are public —
they won't work for outside users yet.
```

C++ objects seamlessly integrated into modern web applications — a **Qt
alternative** for web-based UIs. Where Qt relies on QML/Qt Quick or Qt
WebEngine, webbridge lets you build the UI with standard web technologies
while keeping application logic in C++.

A simple reactive property in Qt needs a getter, a setter, a signal and a
backing field:

```cpp
// Qt approach - verbose boilerplate
Q_PROPERTY(bool aBool READ aBool WRITE setABool NOTIFY aBoolChanged)
bool aBool() const { return _aBool; }
void setABool(bool v) {
    if (v != _aBool) { _aBool = v; emit aBoolChanged(); }
}
signals:
    void aBoolChanged();
private:
    bool _aBool;
```

The same thing in webbridge:

```cpp
property<bool> aBool;
```

webbridge is split across two packages that this site documents together:

- **webbridge-runtime** ([GitHub](https://github.com/WebBridge-Project/webbridge-runtime)) —
  the C++ library: `webbridge::object`, properties, events, constants, error
  handling, and the [webview](https://github.com/webview/webview)-based
  bridge to JavaScript. Distributed as a Conan 2 package.
- **[webbridge-tools](https://github.com/WebBridge-Project/webbridge-tools)** — the
  Python code generator that reads your C++ classes (via tree-sitter) and
  emits the C++ registration headers and TypeScript type definitions.
  Distributed as a pip package and wired into your build through CMake.

Both are required together: `webbridge-runtime` provides the C++ types you
write your classes against, `webbridge-tools` generates the glue code that
exposes them to JavaScript.

```{toctree}
:maxdepth: 2
:caption: webbridge-runtime

getting-started
concepts
examples
cpp-api
```

```{toctree}
:maxdepth: 2
:caption: webbridge-tools

tools/index
tools/cli
tools/api
```
