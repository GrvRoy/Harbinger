#include<stdio.h>

int main()
{
	int  max,min, file_name[25];
   FILE *fp;
 
   fp = fopen("book.txt", "r"); // read mode
 
   if (fp == NULL)
   {
      perror("Error while opening the file.\n");
      return 0;
   }
 
   printf("The contents of %s file are:\n", file_name);
 
   while((ch = fgetc(fp)) != EOF)
      printf("%c", ch);
 
   fclose(fp);
   return 0;
		
}
