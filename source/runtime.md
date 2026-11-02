# webbridge-runtime

webbridge-runtime is the C++ library for webbridge, distributed as a Conan 2
package. See the
[GitHub repository](https://github.com/WebBridge-Project/webbridge-runtime)
for details.

```{note}
Not available for outside users yet: `webbridge-runtime` is only published
to a private Conan server (login required), not ConanCenter, so the install
step below won't resolve until it's published more broadly.
```

```python
# conanfile.py
def requirements(self):
    self.requires("webbridge/0.1.0")
```
