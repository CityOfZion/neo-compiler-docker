# neoj-builder

This image builds Java code (`.java`) into Java bytecode (`.class`).

## Setup

```
make build
```

## Usage

```
docker run -it --rm -v '/path/to/src:/build/files' coz/neoj-builder MyClass.java
```

Where `/path/to/src` is an absolute path to where `MyClass.java` is located.