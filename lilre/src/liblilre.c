

#include "../include/liblilre.h"


void free_re(re_str *str)
{
	long unsigned int i;

	for (i = 0; i < str->size; i++){
		if (str->str[i])
			free(str->str[i]);
	}
	if(str->str)
		free(str->str);

	if(str->c_size)
		free(str->c_size);
}

void add_char(re_str *str, char *c, long unsigned int csize)
{
	// if the max size of the string has been reached, double the size of the array
	if (str->max == str->size) {
		// double the int*   size 
		// double the char** size
		char **str_tmp;
		long unsigned int *c_size_tmp;
		long unsigned int i;
		str_tmp = str->str;
		c_size_tmp = str->c_size;

		str->max = 2*(str->max);

		str->str = (char**) malloc( str->max * sizeof(char*));
		str->c_size = (long unsigned int*) malloc( str->max * sizeof(int));

		// copy over the previous values
		for (i = 0; i < str->size; i++) {
			str->c_size[i] = c_size_tmp[i];

			str->str[i] = (char*) malloc( str->c_size[i] * sizeof(char));
			
			memcpy(str->str[i],str_tmp[i],str->c_size[i]);

			free(str_tmp[i]);
		}
		free(str_tmp);
		free(c_size_tmp);
	}

	// update the c_size array
	str->c_size[str->size] = csize;
	// allocate memory and save the char array to re_str
	str->str[str->size] = (char*) malloc(csize*sizeof(char));
	memcpy(str->str[str->size],c,csize);
	str->size += 1;
}

void init_re(re_str *str)
{
	str->size = 0;
	str->max = 1;
	str->str = (char**) malloc( str->max * sizeof(char*));
	str->c_size = (long unsigned int*) malloc( str->max * sizeof(int));
}


void create_re(re_str *str, char *pattern, long unsigned int p_size)
{

	long unsigned int i,j,glen;

	for (i = 0; i < p_size; i++) {
		if (*(pattern+i) == '[') {

			for (j = i; j < p_size; j++) {
				if (*(pattern+j) == ']') 
					break;
			}
			i++;
			glen = j-i;
			add_char(str,pattern+i,glen);
			i = j;
		} else {
			add_char(str,pattern+i,1);	
		}
	}
}

void print_re(re_str *str)
{
	
	long unsigned int i,j;

	for (i = 0; i < str->size; i++) {
		for (j = 0; j < str->c_size[i]; j++){
			fprintf(stdout,"%c",str->str[i][j]);
		}
		fprintf(stdout,"\n");
	}
}

int re_search(char *base, char *pattern)
{

	long unsigned int i,j,k;
	long unsigned int b_size, p_size;
	re_str str;
	init_re(&str);

	b_size = strlen(base) + 1;
	p_size = strlen(pattern);

	create_re(&str,pattern,p_size);

	//print_re(&str);

	j = 1;
	k = 2;
	i = j + k;

	// loop through the characters in base
	for (i = 0; i < b_size; i++) {
		
		// fprintf(stdout, "%c\n",base[i]);

		// loop through the characters in pattern
		for (j = 0; j < str.size; j++) {
			// loop through the different chars in re_str
			for (k = 0; k < str.c_size[j]; k++) {

				// fprintf(stdout, "%c", str.str[j][k]);
				// if there is a match with the char -> break
				if (str.str[j][k] == base[i+j]) 
					break;

				if (str.str[j][k] == '%')
					if (base[i+j] == '\0')
						break;

				if (str.str[j][k] == '^') {
					//fprintf(stdout, "i: %lu \t k: %lu \n",i,k);
					if (i == 0) {
						i--;
						break;
					}
				}
			}
			// if k == str.c_size[j], no match was found
			// break out of j, move to the next char in base
			if (k == str.c_size[j])
				break;
		}
		
		// if the string does not break early
		// then everything matched and return 1
		if (j == str.size) {
			free_re(&str);
			return 1;
		}
		if ( i == (long unsigned int) -1)
			i = 0;

		//fprintf(stdout,"\n");
	}

	free_re(&str);
	return 0;
}


