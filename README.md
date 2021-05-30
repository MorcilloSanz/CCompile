# CCompile
Compile C and C++ files with Python

## Generate .compile and compile files
First we need to generate the .compile file
```
Windows: py CCompile.py --generate
Linux: python3 CCompile.py --generate
```
### .compile
```
#This is a comment
#COMPILER: g++
#FILES: main.cpp, ball.cpp
#LINKER: -lopengl32, -std=c++11
#EXE: test.exe
#AUTHOR: author

COMPILER: 
FILES: 
LINKER: 
EXE: 
AUTHOR: alber
```
### Compile
```
Windows: py CCompile.py
Linux: python3 CCompile.py
```
