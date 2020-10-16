# -*- coding: utf-8 -*-
'''
     ____                                            ___             
    /\  _`\                                      __ /\_ \            
    \ \ \/\_\    ___    ___     ___ ___   _____ /\_\\//\ \      __   
     \ \ \/_/_  /'___\ / __`\ /' __` __`\/\ '__`\/\ \ \ \ \   /'__`\ 
      \ \ \L\ \/\ \__//\ \L\ \/\ \/\ \/\ \ \ \L\ \ \ \ \_\ \_/\  __/ 
       \ \____/\ \____\ \____/\ \_\ \_\ \_\ \ ,__/\ \_\/\____\ \____\
        \/___/  \/____/\/___/  \/_/\/_/\/_/\ \ \/  \/_/\/____/\/____/
                                            \ \_\                    
                                             \/_/                  
    
    DESCRIPTION:
        CCompile is a simple program which alows you to make C/C++ compilations easier
        
    DEVELOPER:
		NAME: Alberto Morcillo Sanz, aka MorcilloSanz or alber6morci
		EMAIL: amorcillosanz@gmail.com
		TWITTER: @MorcilloSanz
        
    VERSION:
        1.0
        
             ______  ______      __                                                   
     /'\_/`\/\__  _\/\__  _\    /\ \       __                                         
    /\      \/_/\ \/\/_/\ \/    \ \ \     /\_\    ___     __    ___     ____     __   
    \ \ \__\ \ \ \ \   \ \ \     \ \ \  __\/\ \  /'___\ /'__`\/' _ `\  /',__\  /'__`\ 
     \ \ \_/\ \ \_\ \__ \ \ \     \ \ \L\ \\ \ \/\ \__//\  __//\ \/\ \/\__, `\/\  __/ 
      \ \_\\ \_\/\_____\ \ \_\     \ \____/ \ \_\ \____\ \____\ \_\ \_\/\____/\ \____\
       \/_/ \/_/\/_____/  \/_/      \/___/   \/_/\/____/\/____/\/_/\/_/\/___/  \/____/
                                                                                     
	                                                                               
	MIT License

	Copyright (c) 2020 MorcilloSanz

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
'''

import os
import getpass
import sys

GENERATE_COMMAND = '-generate'
HELP_COMMAND = '-help'
VERSION_COMMAND = '-version'

CCOMPILE_FILE_NAME = 'CCompile.compile'

FILES_KEY_WORD = 'FILES'
LINKER_KEY_WORD = 'LINKER'
COMPILER_KEY_WORD = 'COMPILER'
EXE_KEY_WORD = 'EXE'
AUTHOR_KEY_WORD = 'AUTHOR'
COMMENT_KEY_WORD = '#'

GENERATED_COMMENTS = '# COMPILER: g++\n# FILES: main.cpp, ball.cpp\n# LINKER: -lopengl32, -std=c++11\n# EXE: test.exe\n# AUTHOR: author'
HELP_INFO = 'CCompile.py: Compiles the project\nCCompile.py ' + GENERATE_COMMAND + ': Creates CCompile File\nCCompile.py ' + VERSION_COMMAND + ': Version of CCompile'
VERSION_INFO = '1.0 MorcilloSanz'

class CCompile():

    global FILES_KEY_WORD
    global LINKER_KEY_WORD
    global COMPILER_KEY_WORD
    global EXE_KEY_WORD
    global COMMENT_KEY_WORD
    
    global HELP_COMMAND
    
    def __init__(self, filePath):
        self.filePath = filePath
        self.lines = []
        try:
            self.file = open(filePath, 'r')
            self.lines = self.file.readlines()
            self.file.close()
        except IOError:
            print('No CCompile File, see CCompile.py ' + HELP_COMMAND)
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
    
    username = getpass.getuser()
    
    file = open(CCOMPILE_FILE_NAME, 'w')
    file.write(GENERATED_COMMENTS + '\n\n')
    file.write(COMPILER_KEY_WORD + ': \n')
    file.write(FILES_KEY_WORD + ': \n')
    file.write(LINKER_KEY_WORD + ': \n')
    file.write(EXE_KEY_WORD + ': \n')
    file.write(AUTHOR_KEY_WORD + ': ' + username)
    file.close()

def runProgramm():

    global GENERATE_COMMAND
    global HELP_COMMAND
    global VERSION_COMMAND
    global CCOMPILE_FILE_NAME
    global HELP_INFO
    global VERSION_INFO
    
    if(len(sys.argv) > 1):
        for a in sys.argv:
            if(a == GENERATE_COMMAND):
                print('Generating CCompile...')
                writeCCompile()
                print('CCompile File generated successfully')
            elif(a == HELP_COMMAND):
                print(HELP_INFO)
            elif(a == VERSION_COMMAND):
                print(VERSION_INFO)
    else:
        ccompile = CCompile(CCOMPILE_FILE_NAME)
        ccompile.compile()

runProgramm()