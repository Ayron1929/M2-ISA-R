# CoreDSL 2 Parser

This parser understands the preliminary version 2 of CoreDSL. Its grammar is implemented after the [original XText grammar](https://github.com/Minres/CoreDSL/blob/master/com.minres.coredsl/src/com/minres/coredsl/CoreDsl.xtext) and the [accompanying programmer's manual](https://github.com/Minres/CoreDSL/wiki/CoreDSL-2-programmer's-manual), as the reference grammar is not complete.

## Setup
This parser uses the ANTLR parsing toolkit internally, the parser component needs to be generated before use. Download the ANTLR parser generator from [here](https://www.antlr.org/download.html), then execute:
```
cd /path/to/M2-ISA-R/m2isar/frontends/coredsl2
java -jar /path/to/antlr-4.9.3-complete.jar -o parser_gen -listener -visitor -Dlanguage=Python3 CoreDSL2.g4
```

A VSCode task for parser generation is already created for this project. To use it, put the ANTLR binary in the `/path/to/M2-ISA-R/ext` folder.

## Limitations
This parser should be considered as in active development, so bugs will most likely occur. In addition, this parser (but also the metamodel and therefore the code generator) do not implement the following CoreDSL 2 features (at the moment):
- Loops
- Switch case statements
- Complex datatypes (`struct`, `enum`)
- Pointers
- `spawn` statements
- String literals

In addition to that, qualifiers other than `extern` and `register` in `architectural_state` declarations are ignored. The "flexible attribute system" of the reference parser is also not implemented, only a fixed set of attributes are understood.

In the future, these features might also be implemented if needed. For most CPU models, they should however not be absolutely necessary.

Currently implemented but untested functionality:
- Slicing expressions
- Concatenation expressions

Implementation pending:
- Postfix expressions

## Outputs

The parser outputs the architecture model as a pickled python object at `path/to/input/gen_model/<top_level>.m2isarmodel`.

## Usage

The parser can be called by its full python module path `python -m m2isar.frontends.coredsl2.parser` or if installed as in the main README, simply by `coredsl2_parser`.

```
$ coredsl_parser --help
usage: parser.py [-h] [--log {critical,error,warning,info,debug}] top_level

positional arguments:
  top_level             The top-level CoreDSL file.

optional arguments:
  -h, --help            show this help message and exit
  --log {critical,error,warning,info,debug}
```

## Internals
CoreDSL 2 files are parsed using the ANTLR v4 grammar [CoreDSL2.g4](CoreDSL2.g4). Generation of the architecture model takes place during multiple phases:
1) Read top-level CoreDSL file
2) Recursively resolve and read all imports
3) Generate a bottom-up parsing order, to preserve the hierarchical model contained in the CoreDSL description during model generation
4) Parse architectural details and build an architectural model. Here everything except instruction and function behavior is read and generated.
5) Check if top-level architecture model is fully resolved. As CoreDSL 2 allows arbitrary expressions almost anywhere (i.e. user-defined parameters as register size), try to evaluate all expressions describing architectural details. Cancel parsing if evaluation fails.
6) Parse instruction / function behavior, build the behavioral models for each instruction and function. This and the previous parsing steps are seperated to make state tracking between different passes easy.
7) Dump the resulting model to disk, as a binary Python pickle dump.