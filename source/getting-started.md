# Getting Started

## Prerequisites

- **Visual Studio 2022** with C++ Desktop Development (MSVC compiler)
- **Conan 2** and **CMake 3.26+**
- **Python 3.9+** with [webbridge-tools](https://pypi.org/project/webbridge-tools/)
  installed (`pip install webbridge-tools`) — provides the code generator
  and its `webbridge_generate()` CMake function
- **Microsoft Edge WebView2 Runtime** (usually preinstalled on Windows 10/11)

`webbridge-runtime` is Conan-only and covers the C++ library only;
`webbridge-tools` is a separate, pip-installable package — see
[webbridge-tools](tools/index.md) for what it does and why it's separate.

## 0. Add the Conan remote

`webbridge-runtime` is published on an internal Conan server, not
ConanCenter, so it needs to be added as a remote (and logged into, since it
isn't anonymous) before `conan install`/`conan create` can find the package:

```bash
conan remote add --insecure --index 0 fsb http://<server-host>:9300
conan remote login fsb <username> -p <password>
```

`--index 0` gives this server priority over `conancenter` when resolving
`webbridge` itself; other dependencies such as `nlohmann_json` still resolve
from `conancenter` as usual.

## 1. Declare the dependency

In your `conanfile.py`:

```python
def requirements(self):
    self.requires("webbridge/0.1.0")
```

## 2. Wire it into CMakeLists.txt

**The `webbridge` Conan package itself:**

```cmake
find_package(webbridge REQUIRED CONFIG)

target_compile_features(your_target PRIVATE cxx_std_20)
target_link_libraries(your_target PRIVATE webbridge::webbridge)
```

**The code generator** is not a Conan dependency, so it isn't found by
`find_package(webbridge)` above — point CMake at it explicitly instead:

```cmake
find_package(Python REQUIRED COMPONENTS Interpreter)
execute_process(
    COMMAND ${Python_EXECUTABLE} -m webbridge_tools --cmake-dir
    OUTPUT_VARIABLE WEBBRIDGE_TOOLS_CMAKE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE)
list(APPEND CMAKE_MODULE_PATH "${WEBBRIDGE_TOOLS_CMAKE_DIR}")
include(webbridge)

webbridge_generate(
    TARGET your_target
    AUTO
    LANGUAGE cpp
)
```

Replace `your_target` with the name of your own CMake target.

## 3. Write and register a class

Write a class that inherits from `webbridge::object` — see
[Minimal Example](examples.md) for what this looks like — then register it
where you create your webview window:

```cpp
webbridge::register_type<YourClass>(&your_webview);
```

## 4. Build and run

```bash
conan install . --output-folder=build --build=missing -s build_type=Debug  # Debug
conan install . --output-folder=build --build=missing                      # Release (default)

cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE=build/generators/conan_toolchain.cmake

cmake --build build --config Debug                  # Debug
cmake --build build --config Release                # Release (default)
```

```bash
build\Debug\your_target.exe    # Debug build, with DevTools
build\Release\your_target.exe  # Release build, without DevTools
```
