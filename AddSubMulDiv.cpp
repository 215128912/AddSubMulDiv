#include<bits/stdc++.h>
using namespace std;
int numProblems;
struct problem
{
    int num1,num2,num3;
    int op1,op2;
    int ans;
};
int cal(int x,int op,int y)
{
    if(op==0) return x+y;
    if(op==1) return x-y;
    if(op==2) return x*y;
    if(op==3) return x/y;
}
void output(int op)
{
    if(op==0) printf(" + ");
    if(op==1) printf(" - ");
    if(op==2) printf(" * ");
    if(op==3) printf(" / ");
    if(op==4) printf(" = \n");
}
void outputProblem(problem *p)
{
    printf("%d",p->num1);output(p->op1);
    printf("%d",p->num2);output(p->op2);
    printf("%d",p->num3);output(4);
}
int check(problem p)
{
    bool isSwap=false;
    if((p.op1/2)<(p.op2/2))
    {
        int temp=p.num1;
        p.num1=p.num2;p.num2=p.num3;p.num3=temp;
        swap(p.op1,p.op2);isSwap=true;
    }
    if((p.op1==3)&&(p.num1%p.num2)!=0) return -1;
    int ret=cal(p.num1,p.op1,p.num2);
    if(ret<=0||ret>=100) return -1;
    if(isSwap&&(p.op2==1)) swap(ret,p.num3);
    if((p.op2==3)&&(ret%p.num3)!=0) return -1;
    int ans=cal(ret,p.op2,p.num3);
    if(ans<=0||ans>=100) return -1;
    return ans;
}
void get_problem(problem *p)
{
    p->op1=rand()%4;p->op2=rand()%4;
    p->num1=rand()%99+1;p->num2=rand()%99+1;p->num3=rand()%99+1;
}
int main()
{
    srand((unsigned)time(NULL));
    printf("Please enter the number of problems:");
    scanf("%d",&numProblems);
    int nownum=0;problem nowp;
    while(nownum<numProblems)
    {
        get_problem(&nowp);
        nowp.ans=check(nowp);
        if(nowp.ans<0) continue;
        outputProblem(&nowp);
        nownum++;
    }
    return 0;
}
