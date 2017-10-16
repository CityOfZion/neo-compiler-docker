<p align="center">
  <img 
    src="http://res.cloudinary.com/vidsy/image/upload/v1503160820/CoZ_Icon_DARKBLUE_200x178px_oq0gxm.png" 
    width="125px"
  >
</p>

<h1 align="center">neo-compiler-docker</h1>

<p align="center">
  Compile <b>NEO</b> smart contracts using Docker.
</p>

<p align="center">
  <a href="https://github.com/CityOfZion/neo-compiler-docker/releases">
    <img src="https://img.shields.io/github/tag/CityOfZion/neo-compiler-docker.svg?style=flat">
  </a>
</p>

## What?

- A set of [Docker](https://www.docker.com/) images
- Each provide a cross-platform mechanism for compiling [NEO](https://neo.org/) smart contracts
- No need to setup NEO development environment 🎉

## Images

### neoj-builder

This image builds Java (`.java`) code into Java bytecode (`.class`).

### neoj-compiler

This image compiles Java bytecode (`.class`) into NEO AVM code (`.avm`).

## Usage

Each image has a README within the directory, which describes how to use it. Please note that 
for security reasons, all Docker images have to first be built locally.

