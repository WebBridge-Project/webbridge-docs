# Concepts

Every class exposed to the web inherits from `webbridge::object`. The API is
inspired by Qt, with each Qt concept mapped onto something web-native:

| webbridge        | Qt equivalent          | JavaScript side                    |
|-------------------|-------------------------|-------------------------------------|
| Method             | `Q_INVOKABLE`           | `Promise`-returning async function |
| `property<T>`      | `Q_PROPERTY`            | Svelte-compatible reactive store   |
| `event<Args...>`   | signal                  | `.on()` / `.once()` listener       |
| Constant           | enum/static const       | read-only value                    |

The generated code is functionally inspired by Qt's MOC (Meta-Object
Compiler), but needs far less boilerplate — see [webbridge-tools](tools/index.md)
for how that generation works.

## Methods

All public methods of a `webbridge::object` class are automatically
published to JavaScript.

A method marked `[[async]]` runs on a separate worker thread, so it never
blocks the main thread on the C++ side. On the JavaScript side, both
synchronous and asynchronous methods always return a `Promise` and never
block the main thread.

## Properties

Properties are accessed via the parenthesis operator `()` in C++. In
JavaScript they're exposed as read-only, reactive stores — changes made in
C++ propagate to JavaScript automatically and immediately.

## Events

Events are the webbridge equivalent of Qt's signal/slot mechanism, exposed
to JavaScript as event listeners (similar to Node's `EventEmitter`).

## Constants

Both **static** (class-wide) and **non-static** (instance-specific)
constants are automatically exported to JavaScript as read-only values.

## Error Handling

webbridge distinguishes JavaScript client errors (4xxx) from C++ server
errors (5xxx). Errors are serialized as JSON and, for asynchronous
operations, propagated as rejected Promises:

```json
{
  "error": {
    "code": 4001,
    "message": "Invalid argument type",
    "details": { "param": "value", "expected": "string" },
    "stack": "at function (file.js:10:5)",
    "origin": "javascript"
  }
}
```

- `4000-4999`: JavaScript errors, e.g. `4001` = `JSON_PARSE_ERROR` during
  parameter deserialization.
- `5000-5999`: C++ errors, e.g. `5000` = `RUNTIME_ERROR` during a runtime
  error.

This is inspired by JSON-RPC 2.0, GraphQL, and HTTP status codes; promises
reject automatically on error, enabling plain `async`/`await` exception
handling on the JavaScript side. See the [C++ API reference](cpp-api.rst)
for `webbridge::error` and `webbridge::set_error_handler`.

## Registration

The code generator (`webbridge-tools`) creates the binding files that make a
C++ class available in JavaScript; include the generated header and call its
registration function in `main.cpp`:

```cpp
#include "MyObject_registration.h"

int main() {
    webbridge::register_type<MyObject>();
    // ... initialize and run your webview ...
}
```

## Known Limitations

- Overloaded constructors and methods are not supported.
- Enums are automatically detected and exported to TypeScript, but complex
  enum use cases may require additional handling.
- Currently Windows-only (relies on Microsoft WebView2).
