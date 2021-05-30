# -*- coding: utf-8 -*-
'''
    MIT License

    Copyright (c) 2021 MorcilloSanz

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    ----------------------------------------------------------------------------

    Description:
        Compile C or C++ files using GCC

    Dev:
		Name: MorcilloSanz
		Email: amorcillosanz@gmail.com
		Twitter: @MorcilloSanz                                                   
'''

import os
import getpass
import sys

GENERATE_COMMAND = '--generate'
GENERATE_COMMAND_SHORT = '-g'
HELP_COMMAND = '--help'
HELP_COMMAND_SHORT = '-h'
VERSION_COMMAND = '--version'
VERSION_COMMAND_SHORT = '-v'

FILES_KEY_WORD = 'FILES'
LINKER_KEY_WORD = 'LINKER'
COMPILER_KEY_WORD = 'COMPILER'
EXE_KEY_WORD = 'EXE'
AUTHOR_KEY_WORD = 'AUTHOR'
COMMENT_KEY_WORD = '#'

CCOMPILE_FILE_NAME = 'CCompile.compile'
GENERATED_COMMENTS = (
    '#This is a comment\n'
    '#COMPILER: g++\n'
    '#FILES: main.cpp, ball.cpp\n'
    '#LINKER: -lopengl32, -std=c++11\n'
    '#EXE: test.exe\n'
    '#AUTHOR: author'
)
HELP_INFO = (
    'CCompile.py: Compiles the project\n'
    'CCompile.py ' + GENERATE_COMMAND + ': Creates CCompile File\n'
    'CCompile.py ' + VERSION_COMMAND + ': Version of CCompile'
)
VERSION_INFO = '1.0 MorcilloSanz'

class CCompile():

    global FILES_KEY_WORD
    global LINKER_KEY_WORD
    global COMPILER_KEY_WORD
    global EXE_KEY_WORD
    global COMMENT_KEY_WORD
    global HELP_COMMAND
    global HELP_COMMAND_SHORT

    def __init__(self, filePath):
        self.filePath = filePath
        self.lines = []
        try:
            self.file = open(filePath, 'r')
            self.lines = self.file.readlines()
            self.file.close()
        except IOError:
            print('No CCompile File, see CCompile.py ' + HELP_COMMAND + ' or ' + HELP_COMMAND_SHORT)
        self.command = ''

    def getCommand(self):
        for line in self.lines:
            if(line.startswith(COMPILER_KEY_WORD)):
                self.compiler = line.split(COMPILER_KEY_WORD + ':')[1]
                self.command = self.command + self.compiler + ' '
            elif(line.startswith(FILES_KEY_WORD)):
                splitted = line.split(FILES_KEY_WORD + ':')
                self.files = splitted[1].split(',')
                for f in self.files:
                    self.command = self.command + f + ' '
            elif(line.startswith(LINKER_KEY_WORD)):
                splitted = line.split(LINKER_KEY_WORD + ':')
                links = splitted[1].split(',')
                for l in links:
                    self.command = self.command + l + ' '
                self.command = self.command + ' -o '
            elif(line.startswith(EXE_KEY_WORD)):
                self.exe = line.split(EXE_KEY_WORD + ':')[1]
                self.command = self.command + self.exe
            elif(line.startswith(COMMENT_KEY_WORD)):
                pass

        fixedCommand = ''
        for c in self.command:
            if(c != '\n'):
                fixedCommand = fixedCommand + c
        self.command = fixedCommand
        return self.command

    def getExe(self):
        return self.exe

    def compile(self):
        command = self.getCommand()
        os.system(command)

def writeCCompile():

    global CCOMPILE_FILE_NAME
    global FILES_KEY_WORD
    global LINKER_KEY_WORD
    global COMPILER_KEY_WORD
    global EXE_KEY_WORD
    global AUTHOR_KEY_WORD
    global COMMENT_KEY_WORD
    global GENERATED_COMMENTS

    file = open(CCOMPILE_FILE_NAME, 'w')
    file.write(GENERATED_COMMENTS + '\n\n')
    file.write(COMPILER_KEY_WORD + ': \n')
    file.write(FILES_KEY_WORD + ': \n')
    file.write(LINKER_KEY_WORD + ': \n')
    file.write(EXE_KEY_WORD + ': \n')
    username = getpass.getuser()
    file.write(AUTHOR_KEY_WORD + ': ' + username)
    file.close()

if(len(sys.argv) > 1):
    for a in sys.argv:
        if(a == GENERATE_COMMAND or a == GENERATE_COMMAND_SHORT):
            print('Generating CCompile...')
            writeCCompile()
            print('CCompile File generated successfully')
        elif(a == HELP_COMMAND or a == HELP_COMMAND_SHORT):
            print(HELP_INFO)
        elif(a == VERSION_COMMAND or a == VERSION_COMMAND_SHORT):
            print(VERSION_INFO)
        else:
            print('CCompyle.py ' + HELP_COMMAND + ' or ' + HELP_COMMAND_SHORT)
else:
    ccompile = CCompile(CCOMPILE_FILE_NAME)
    ccompile.compile()
