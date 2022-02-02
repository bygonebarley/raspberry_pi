# Author: Jeremy Stevens
#	E-mail: jsteve22@nd.edu
#	File Name: Makefile
#	Date Created: 1/28/2022
#	File Contents: This is the Makefile for compilation of liblilre.so

# gcc is the compiler for C
PP := gcc

# CFLAGS are the compiler flags for when we compile C code in this course
FLAGS := -O2 -g -Wall -Wextra -Wconversion -Wshadow -Werror -lm
CFLAGS := -std=c11 $(FLAGS)

# Folder Variables
SRC := src
INC := include
OBJ := objects
EXE := exe

# Initialize the folder for the objects and executables
initialize:
	mkdir $(OBJ) $(EXE)

# Create the liblilre.so library
$(OBJ)/liblilre.so: $(SRC)/liblilre.c $(INC)/liblilre.h
	$(PP) $(CFLAGS) -shared -fPIC $(SRC)/liblilre.c -o $@

# Create the comp object
$(OBJ)/comp.o: $(SRC)/comp.c $(INC)/liblilre.h 
	$(PP) $(CFLAGS) -c $(SRC)/comp.c -o $@ 

# Create the comp exe
comp: $(OBJ)/comp.o $(OBJ)/liblilre.so
	$(PP) $(CFLAGS) $(OBJ)/comp.o -llilre -L$(OBJ) -o $(EXE)/comp

# Make clean
clean:
	rm -rf $(OBJ)/* $(EXE)/*
