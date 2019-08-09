#include<stdio.h>
#include<string.h>
void main()
{
    int n,j=0,i;
    char s[100],b[100],c[100];
    scanf("%d",&n);
    scanf("%s",s);
    for(i=0;s[i]!='\0';i++)
    {
        if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' || s[i]=='A' || s[i]=='E' || s[i]=='I' || s[i]=='O'|| s[i]=='U')
            continue;
        else
        {
            b[j]=s[i];
            j--;
        }
    }
    printf("%s",strrev(b));
}
