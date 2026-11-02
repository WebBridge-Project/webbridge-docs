# webbridge documentation

```{note}
Public availability is still in progress. `webbridge-tools` is published on
PyPI and installable with `pip install webbridge-tools`, but
`webbridge-runtime` is currently only published to a private Conan server —
the Conan install steps on this site won't work for outside users yet.
```

**Versions:** webbridge-runtime (Conan) `0.1.0` · webbridge-tools (PyPI) `1.0.0`

**Useful links:**
[webbridge-runtime source](https://github.com/WebBridge-Project/webbridge-runtime) |
[webbridge-tools source](https://github.com/WebBridge-Project/webbridge-tools) |
[webbridge-tools on PyPI](https://pypi.org/project/webbridge-tools/) |
[Getting Started](getting-started.md)

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
**webbridge-runtime** is the C++ library (Conan package) — `webbridge::object`,
properties, events, constants, error handling, and the
[webview](https://github.com/webview/webview)-based bridge to JavaScript.
**webbridge-tools** is the Python code generator (pip package) that reads
your C++ classes via tree-sitter and emits the C++ registration headers and
TypeScript type definitions. Both are required together: `webbridge-runtime`
provides the C++ types you write your classes against, `webbridge-tools`
generates the glue code that exposes them to JavaScript.

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} {octicon}`rocket` Getting Started
:link: getting-started
:link-type: doc

Set up the Conan remote, wire `webbridge_generate()` into CMake, and register
your first class.
:::

:::{grid-item-card} {octicon}`repo` webbridge-runtime
:link: runtime
:link-type: doc

Short description and Conan install info for the C++ library.
:::

:::{grid-item-card} {octicon}`terminal` webbridge-tools
:link: tools
:link-type: doc

The Python code generator: `webbridge-generate`, `webbridge-discoverer`,
`webbridge-parser`, and the underlying Python API.
:::

:::{grid-item-card} {octicon}`book` Concepts
:link: concepts
:link-type: doc

How properties, events, methods and constants map from Qt onto web-native
JavaScript, plus error handling and known limitations.
:::

:::{grid-item-card} {octicon}`file-code` Examples
:link: examples
:link-type: doc

A minimal end-to-end C++ class exposed to JavaScript.
:::

:::{grid-item-card} {octicon}`code` C++ API Reference
:link: cpp-api
:link-type: doc

Doxygen/Breathe-generated reference for `webbridge::object`, properties,
events and error handling.
:::

::::

```{toctree}
:maxdepth: 2
:hidden:

Getting Started <getting-started>
webbridge-runtime <runtime>
webbridge-tools <tools>
Concepts <concepts>
Examples <examples>
C++ API Reference <cpp-api>
```
