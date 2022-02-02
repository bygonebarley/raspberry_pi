#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct {
	char **str;
	long unsigned int size;
	long unsigned int max;
	long unsigned int *c_size;
} re_str;

void free_re(re_str*);
void add_char(re_str*,char*,long unsigned int);
void init_re(re_str*);
void create_re(re_str*,char*,long unsigned int);
void print_re(re_str*);
int re_search(char*,char*);
