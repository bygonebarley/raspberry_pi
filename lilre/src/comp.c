#include "../include/liblilre.h"


int main(void)
{
	
//	char *base = "GME this is a cool call";

	char base[100];
	char opt;
	char *pat = "[ $^]GME[| %]";
	int check;
	long unsigned int i;

	do {
		fprintf(stdout,"pattern: ''%s''\n",pat);
		fprintf(stdout,"enter a base string \n");
		fgets(base,100,stdin);

		for (i = 0; i < (long unsigned int) strlen(base) + 1; i++)
			if (base[i] == '\n')
				base[i] = '\0';
		for (i = 0; i < (long unsigned int) strlen(base) + 1; i++)
			fprintf(stdout, "c - %c \t %d\n", base[i], (int) base[i]);

		check = re_search(base,pat);
		fprintf(stdout,"check = %d\n",check);
		fprintf(stdout,"do you wish to continue(y/n): ");
		opt = (char) fgetc(stdin);
		check = fgetc(stdin);
	} while (opt == 'y');


	return 0;
}
