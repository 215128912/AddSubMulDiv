#include<bits/stdc++.h>
#define cp complex<double>
using namespace std;
const int maxn=1100000;
const double PI=acos(-1.0);
char s1[maxn],s2[maxn];
int len1,len2,len,l;
int rev[maxn<<1];
cp d1[maxn<<1],d2[maxn<<1];
int d[maxn<<1];
int ans[maxn<<1],numans;
void change(cp *f,int inv)
{
    rev[0]=0;
    for(int i=1; i<len; i++) rev[i]=(rev[i>>1]>>1)|((i&1)<<(l-1));
    for(int i=0; i<len; i++)
    {
        if(i<rev[i])
            swap(f[i],f[rev[i]]);
    }
    for(int nlen=2; nlen<=len; nlen<<=1)
    {
        int mid=nlen>>1;
        cp each(cos(2*PI/nlen),inv*sin(2*PI/nlen));
        for(int st=0; st<len; st+=nlen)
        {
            cp now(1,0);
            for(int i=st; i<st+mid; i++,now*=each)
            {
                cp x=f[i],y=f[i+mid];
                f[i]=x+now*y;
                f[i+mid]=x-now*y;
            }
        }
    }
}
int main()
{
    while(scanf("%s %s",s1,s2)!=EOF)
    {
        len1=strlen(s1);
        len2=strlen(s2);
        while(1<<l<(len1+len2-1)) l++;
        len=1<<l;
        for(int i=0; i<len; i++) d1[i]=d2[i]=cp(0,0);
        for(int j=len1-1,i=0; j>=0; j--,i++) d1[i]=cp(s1[j]-'0',0);
        for(int j=len2-1,i=0; j>=0; j--,i++) d2[i]=cp(s2[j]-'0',0);
        change(d1,1);
        change(d2,1);
        for(int i=0; i<len; i++) d1[i]*=d2[i];
        change(d1,-1);
        for(int i=0; i<len; i++) d[i]=(int)(d1[i].real()/len+0.5);
        numans=0;
        int now=d[0];
        for(int i=1; i<len; i++)
        {
            ans[numans++]=now%10;
            now=now/10+d[i];
        }
        while(now)
        {
            ans[numans++]=now%10;
            now/=10;
        }
        int pos=numans-1;
        while(ans[pos]==0) pos--;
        bool output=false;
        while(pos>=0)
        {
            printf("%d",ans[pos--]);
            output=true;
        }
        if(!output) printf("0");
        printf("\n");
    }
    return 0;
}
