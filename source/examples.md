# Minimal Example

A C++ class with methods, properties, and events exposed to the web:

```cpp
#include "webbridge/object.h"

class MyObject : public webbridge::object
{
public:
    property<bool> aBool = false;
    property<std::string> strProp;
    event<int, bool> aEvent;
    inline static constexpr auto PI = 3.141592654;
    const std::string version = "1.0";

public:
    [[async]] void foo(std::string_view val) {
        // long-running action
        strProp = val;
        aEvent.emit(42, false);
    }

    bool bar() const {
        // Parenthesis operator accesses value
        return !aBool();
    }
};
```

## Tracking properties in JavaScript

```js
const myObj = await MyObject.create();

myObj.aBool.subscribe(value => {
    console.log('aBool updated:', value);
});
```

## Calling a method from JavaScript

```js
const myObj = await MyObject.create();

// Synchronous method: blocks the main thread in C++, JS awaits it
const result = await myObj.bar();
console.log('Result of bar():', result);

// [[async]] method: runs on a C++ worker thread, never blocks either side
myObj.foo('new value').then(() => {
    console.log('foo() completed');
});
```

## Handling events in JavaScript

```js
const myObj = await MyObject.create();

myObj.aEvent.on((intValue, boolValue) => {
    console.log('Event received:', intValue, boolValue);
});

myObj.aEvent.once((intValue, boolValue) => {
    console.log('One-time event:', intValue, boolValue);
});
```

## Accessing constants in JavaScript

```js
const myObj = await MyObject.create();
console.log(myObj.version); // Instance constant: "1.0"
console.log(MyObject.PI);   // Static constant: 3.141592654
```
