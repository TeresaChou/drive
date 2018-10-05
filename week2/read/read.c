#include <stdio.h>

int main() {
   int c;
   FILE *file;
   file = fopen("/dev/DHT11", "r");
   if (file) {
      while ((c = getc(file)) != EOF)
         putchar(c);
      fclose(file);
   }
   else{
   	printf("NO such FIle \n");
   }
}
