# neo-boa-compiler

This image builds Python code (`.py`) into NEO AVM code (`.avm`), using the [neo-boa](https://github.com/CityOfZion/neo-boa) compiler.

## Setup

```
make build
```

## Usage

```
docker run -it --rm -v '/path/to/src:/compile/src' coz/neo-boa-compiler HelloWorld.py
```

Where `/path/to/src` is an absolute path to where `HelloWorld.py` is located.