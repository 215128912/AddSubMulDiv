
import random
from tkinter import *
from tkinter import messagebox

allproblem=[]
class problem:
	def __init__(self, num1,num2,num3,op1,op2,ans):
		self.num1=num1
		self.num2=num2
		self.num3=num3
		self.op1=op1
		self.op2=op2
		self.ans=ans
	def show(self):
		print("%d%c%d%c%d=%d"%(self.num1,change(self.op1),self.num2,\
			change(self.op2),self.num3,self.ans))

def change(op):
	if op==0: return '+'
	if op==1: return '-'
	if op==2: return '*'
	if op==3: return '/'

def cal(x,op,y):
	if op==0: return x+y
	if op==1: return x-y
	if op==2: return x*y
	if op==3: return x//y

def get_problem():
	p=problem(0,0,0,0,0,0)
	p.num1=random.randint(1,99)
	p.num2=random.randint(1,99)
	p.num3=random.randint(1,99)
	p.op1=random.randint(0,3)
	p.op2=random.randint(0,3)
	return p

def check(p):
	pp=problem(p.num1,p.num2,p.num3,p.op1,p.op2,p.ans)
	isSwap=0
	if((pp.op1//2)<(pp.op2//2)):
		temp=pp.num1
		pp.num1=pp.num2;pp.num2=pp.num3;pp.num3=temp;
		temp=pp.op1;pp.op1=pp.op2;pp.op2=temp;
		isSwap=1
	if((pp.op1==3) and (pp.num1%pp.num2)!=0): return -1
	ret=cal(pp.num1,pp.op1,pp.num2)
	if(ret<=0 or ret>=100): return -1
	if(isSwap==1 and pp.op2==1):
		temp=ret;ret=pp.num3;pp.num3=temp;
	if(pp.op2==3 and ret%pp.num3!=0): return -1;
	ans=cal(ret,pp.op2,pp.num3)
	if(ans<=0 or ans>=100): return -1;
	p.ans=ans
	return ans

def fcbt1():
	Te1.delete(1.0,END)
	num=int(Et1.get())
	nownum=0
	allproblem.clear()
	while(nownum<num):
		nowp=get_problem()
		if(check(nowp)<0): continue
		nownum+=1
		allproblem.append(nowp)
	linenum=0;
	for p in allproblem:
		if linenum%2==0: Te1.insert(INSERT,"     ")
		Te1.insert(INSERT,"%-2d%-1c%-2d%-1c%-2d=  "%(p.num1,change(p.op1),p.num2,\
			change(p.op2),p.num3))
		if linenum%2==0: Te1.insert(INSERT,"       ")
		else: Te1.insert(INSERT,"\n")
		linenum+=1

def fcck1():
	state=CheckVar.get()
	Te1.delete(1.0,END)
	if state==0:
		linenum=0;
		for p in allproblem:
			if linenum%2==0: Te1.insert(INSERT,"     ")
			Te1.insert(INSERT,"%-2d%-1c%-2d%-1c%-2d=  "%(p.num1,change(p.op1),p.num2,\
				change(p.op2),p.num3))
			if linenum%2==0: Te1.insert(INSERT,"       ")
			else: Te1.insert(INSERT,"\n")
			linenum+=1
	else:
		linenum=0;
		for p in allproblem:
			if linenum%2==0: Te1.insert(INSERT,"     ")
			Te1.insert(INSERT,"%-2d%-1c%-2d%-1c%-2d=%-2d"%(p.num1,change(p.op1),p.num2,\
				change(p.op2),p.num3,p.ans))
			if linenum%2==0: Te1.insert(INSERT,"       ")
			else: Te1.insert(INSERT,"\n")
			linenum+=1
		
def export():
	state=CheckVar.get()
	fp=open("./四则运算题.txt","w")
	if state==0:
		linenum=0;
		for p in allproblem:
			if linenum%2==0: 
				fp.write("                      ")
			fp.write("%-2d%-1c%-2d%-1c%-2d=  "%(p.num1,change(p.op1),p.num2,\
				change(p.op2),p.num3))
			if linenum%2==0: 
				fp.write("                              ")
			else: fp.write("\n")
			linenum+=1
	else:
		linenum=0;
		for p in allproblem:
			if linenum%2==0: fp.write("                      ")
			fp.write("%-2d%-1c%-2d%-1c%-2d=%-2d"%(p.num1,change(p.op1),p.num2,\
				change(p.op2),p.num3,p.ans))
			if linenum%2==0: fp.write("                              ")
			else: fp.write("\n")
			linenum+=1		
	fp.close()

top=Tk()
top.title("四则运算生成器")
top.geometry("300x350+500+200")
top.resizable(0,0)

frame_root=Frame(top)
frame_root.pack()
frame1=Frame(frame_root)
frame1.pack()
frame2=Frame(frame_root)
frame2.pack()

Lb1=Label(frame1,text="题目数量:")
Et1=Entry(frame1,width=5)
Bt1=Button(frame1,text="确定",command=fcbt1)
CheckVar=IntVar()
Ck1=Checkbutton(frame1,text="显示答案",command=fcck1,variable=CheckVar)
Bt2=Button(frame1,text="导出",command=export)
Sc=Scrollbar(frame2)
Sc.pack(side=RIGHT,fill=Y)
Te1=Text(frame2,height=50,yscrollcommand=Sc.set)
Sc.config(command=Te1.yview)

Lb1.pack(side=LEFT)
Et1.pack(side=LEFT)
Bt1.pack(side=LEFT)
Bt2.pack(side=LEFT)
Ck1.pack(side=LEFT)
Te1.pack()

top.mainloop()
