#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <stdlib.h>
void print_memory(void* ptr,size_t bytes){
    for(size_t i=0;i<bytes;i++){
        fprintf(stderr,"%lu: %02x\n",i,*(unsigned char*)(ptr));
        ptr=(char*)ptr+1;
    }
    fprintf(stderr,"\n");
}
int main1(){
    char s1[]="aé你"; // literal
    char s2[]="\x61\xc3\xa9\xe4\xbd\xa0"; // same string in UTF-8
    char s3[]="\x61\xa8\xa6\xc4\xe3"; // same string in GBK
    #define s s3
    // char s[]="abc";
    print_memory(s,sizeof(s));
    setlocale(LC_ALL,"zh_CN.GBK");
    wchar_t s_buffer[4];
    mbstowcs(s_buffer,s,4);
    print_memory(s_buffer,sizeof(s_buffer));
    wprintf(L"%ls\n",s_buffer);
    wprintf(L"%lu\n",sizeof(s_buffer));
    return 0;
}
int main(){
    main1();
}