# CLI Reference

`webbridge-tools` installs three console scripts (see `[project.scripts]` in
its `pyproject.toml`). Each is also runnable as a module, which is what the
`webbridge_generate()` CMake function does under the hood.

## `webbridge-generate`

Generates `_registration.h` files (and optional TypeScript bindings) from
explicitly specified C++ classes, using tree-sitter to parse the header and
Jinja2 to render the output.

```bash
# Single file
webbridge-generate <input.h> --class-name <ClassName> --cpp_out=<dir> --ts_impl_out=<dir>

# Batch processing of multiple files
webbridge-generate --batch file1.h|Class1 file2.h|Class2 --cpp_out=<dir> --ts_impl_out=<dir>

# Equivalent without the console script (e.g. from CMake)
python -m webbridge_tools.tools.generate <input.h> --class-name <ClassName> --cpp_out=<dir>
```

Example:

```bash
webbridge-generate ../src/MyObject.h --class-name MyObject --cpp_out=../build/src --ts_impl_out=../frontend/src
```

## `webbridge-discoverer`

Scans C++ header files and finds all classes that inherit from
`webbridge::object`, so CMake doesn't need an explicit class list (used by
`webbridge_generate(... AUTO ...)`). Inspired by Qt's MOC auto-discovery.

```bash
webbridge-discoverer header1.h header2.h ...
```

Output is one `filename|classname` pair per discovered class, consumable by
CMake via `COMMAND_OUTPUT_VARIABLE`.

## `webbridge-parser`

The tree-sitter based parser that extracts class information (properties,
events, methods) from a C++ header — used internally by `webbridge-generate`,
but also usable standalone for inspection/debugging. See the
[Python API](api.rst) for `parse_header()` and `ClassInfo`.
