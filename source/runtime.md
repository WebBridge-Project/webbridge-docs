# webbridge-runtime

```{note}
Not available for outside users yet: `webbridge-runtime` is only published
to a private Conan server (login required), not ConanCenter, so the install
step below won't resolve until it's published more broadly.
```

[webbridge-runtime](https://github.com/WebBridge-Project/webbridge-runtime) is
the C++ library for webbridge. You write a class that inherits from
`webbridge::object`, and its properties, events, and constants show up
automatically in JavaScript — no manual getters, setters, or signals needed.
It also handles sending data back and forth between C++ and JavaScript
through [webview](https://github.com/webview/webview).

It's a separate Conan package from `webbridge-tools` because the two have
different dependencies and release on their own schedules. Declare it as a
dependency:

```python
# conanfile.py
def requirements(self):
    self.requires("webbridge/0.1.0")
```
