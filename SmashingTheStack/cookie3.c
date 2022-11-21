#include <stdio.h>

int main(){
  char buf[80];
  int cookie;

  printf("buf: %lx cookie: %08x\n", &buf, &cookie);
  gets(buf);

  if(cookie == 0x01020305)
    printf("you lose!\n");
}
