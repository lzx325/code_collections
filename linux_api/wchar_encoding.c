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
    char s3[]="\x61\xa8\xa6\xc4\xe3"; // same string in GBK, if GBK is not installed (by checking `locale -a`), use `sudo dpkg-reconfigure --force locales` to install GBK encoding
    char s4[]="\x61\xe9"; // first two characters in iso8859-1, ensure the encoding is installed
    // https://blog.csdn.net/wenwenxiong/article/details/17116791
    wchar_t s5[]=L"aé你"; 
    wchar_t s_buffer[4];

    fprintf(stderr,"Testing s1[].\n");
    fprintf(stderr,"Storage of s1[]\n");
    print_memory(s1,sizeof(s1));
    setlocale(LC_ALL,"en_US.UTF-8"); // will affect mbstowcs, wprintf
    mbstowcs(s_buffer,s1,4); // UTF-8 -> UTF-32 (or other default encoding of wchar_t)
    fprintf(stderr,"Storage of s_buffer[]\n");
    print_memory(s_buffer,sizeof(s_buffer));
    fprintf(stderr,"wprintf of s_buffer[]\n");
    wprintf(L"%ls\n\n",s_buffer);

    fprintf(stderr,"Testing s2[].\n");
    fprintf(stderr,"Storage of s2[]\n");
    print_memory(s2,sizeof(s2));
    setlocale(LC_ALL,"en_US.UTF-8"); // UTF-8 -> UTF-32 (or other default encoding of wchar_t)
    mbstowcs(s_buffer,s2,4);
    fprintf(stderr,"Storage of s_buffer[]\n");
    print_memory(s_buffer,sizeof(s_buffer));
    fprintf(stderr,"wprintf of s_buffer[]\n");
    wprintf(L"%ls\n\n",s_buffer);

    fprintf(stderr,"Testing s3[].\n");
    fprintf(stderr,"Storage of s3[]\n");
    print_memory(s3,sizeof(s3));
    setlocale(LC_ALL,"zh_CN.GBK");
    mbstowcs(s_buffer,s3,4); // GBK -> UTF-32 (or other default encoding of wchar_t)
    fprintf(stderr,"Storage of s_buffer[]\n");
    print_memory(s_buffer,sizeof(s_buffer));
    fprintf(stderr,"wprintf of s_buffer[]\n");
    wprintf(L"%ls\n\n",s_buffer);

    fprintf(stderr,"Testing s4[].\n");
    fprintf(stderr,"Storage of s4[]\n");
    print_memory(s4,sizeof(s4));
    setlocale(LC_ALL,"fr_FR.iso88591"); // iso88591 -> UTF-32 (or other default encoding of wchar_t)
    mbstowcs(s_buffer,s4,4);
    fprintf(stderr,"Storage of s_buffer[]\n");
    print_memory(s_buffer,sizeof(s_buffer));
    fprintf(stderr,"wprintf of s_buffer[]\n");
    wprintf(L"%ls\n\n",s_buffer);

    fprintf(stderr,"Testing s5[].\n");
    fprintf(stderr,"Storage of s5[]\n");
    print_memory(s5,sizeof(s5)); // wchar_t literals by default use UTF-32 or UTF-16
    setlocale(LC_ALL,"en_US.UTF-8"); // Ensure that non-ASCII characters can be print out by wprintf
    fprintf(stderr,"wprintf of s5[]\n");
    wprintf(L"%ls\n\n",s5);
    return 0;
}
int main(){
    main1();
}