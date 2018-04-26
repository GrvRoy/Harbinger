#include<stdio.h>

int main()
{
	char ch;
		int hum,max[10],min[10], file_name[25];
   FILE *fp;
 
   fp = fopen("book.txt", "r"); // read mode
 
   if (fp == NULL)
   {
      perror("Error while opening the file.\n");
      return 0;
   }
 
   printf("The contents of %s file are:\n", file_name);
 	int i=2;
   while(i--)
    {
    	fscanf(fp,"%d %d %d %d ", &date,&hum,&max[i],&min[i]);
	}
   fclose(fp);
   return 0;
		
}
