# neoj-compiler

This image compiles Java bytecode (.class) into NEO AVM code (`.avm`).

## Setup

```
make update-submodule
```
```
make publish-neoj
```
```
make build
```

## Usage

```
docker run -it --rm -v '/path/to/src:/compile/src' coz/neoj-compiler HelloWorld.class
```

Where `/path/to/src` is an absolute path to where `HelloWorld.class` is located.
