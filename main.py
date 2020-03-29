from tkinter import *
import numpy
import scipy
import math
t=Tk()
t.title('最短路径')
t.geometry('1600x900')
Label(t,text='点的个数').place(x=5,y=5)#输入点的个数
x1=''
global e1
e1=Entry(t,width=10)
e1.place(x=60,y=5)
Label(t,text='       到               的距离:').place(x=22,y=40)
dis=Entry(t,width=5)
dis.place(x=185,y=40)
start=Entry(t,width=5)
start.place(x=5,y=40)
end=Entry(t,width=5)
end.place(x=75,y=40)
a=0#变量a用来判断按钮回调函数是否会被触发
def get():#储存按钮的回调函数
    global a
    if a!=0:#a不等于0时储存函数被触发
        if start.get().isdigit()==True and end.get().isdigit()==True and dis.get().isdigit()==True:
            a=2
            line=int(start.get())#起点
            column=int(end.get())#终点
            distance=int(dis.get())#距离
            pi=math.pi
            if column!=line and 0<column<=x1 and 0<line<=x1:#看一下两点是否符合条件
                if matrix[line-1][column-1]!=0:#如果已经生成过距离，需要重新定义
                    c.create_text(500+150*(math.cos(2*pi*(line-1)/x1)+math.cos(2*pi*(column-1)/x1)),375+150*(math.sin(2*pi*(line-1)/x1)+math.sin(2*pi*(column-1)/x1)),text=int(matrix[line-1][column-1]),fill='white')
                    #生成了一个白色的数字来覆盖掉原来的数字（距离）
                matrix[line-1][column-1]=distance#进行存储
                matrix[column-1][line-1]=distance#注意距离的无方向性
                trans[line-1][column-1]=column#暂时将终点定义为中间点
                trans[column-1][line-1]=line#另一边得倒过来
                c.create_text(500+150*(math.cos(2*pi*(line-1)/x1)+math.cos(2*pi*(column-1)/x1)),375+150*(math.sin(2*pi*(line-1)/x1)+math.sin(2*pi*(column-1)/x1)),text=int(distance))
                c.create_line(500+300*math.cos(2*pi*(line-1)/x1),375+300*math.sin(2*pi*(line-1)/x1),500+300*math.cos(2*pi*(column-1)/x1),375+300*math.sin(2*pi*(column-1)/x1),fill='red')
                #以上两行生成了红线和对应的距离
                if distance==0:#如果输错距离（两点之间本没有距离），则把生成的线和数字去掉（用白色的线条和数字去覆盖）
                    c.create_text(500+150*(math.cos(2*pi*(line-1)/x1)+math.cos(2*pi*(column-1)/x1)),375+150*(math.sin(2*pi*(line-1)/x1)+math.sin(2*pi*(column-1)/x1)),text=int(distance),fill='white')
                    c.create_line(500+300*math.cos(2*pi*(line-1)/x1),375+300*math.sin(2*pi*(line-1)/x1),500+300*math.cos(2*pi*(column-1)/x1),375+300*math.sin(2*pi*(column-1)/x1),fill='white')
            else:#如果你输入的点不存在或输入了两个一样的点，就会报错
                A=Tk()
                A.title('Error')
                A.geometry('200x100')
                Label(A,text='你输入的数据有误！',bg='red').place(x=50,y=20)
def establish():#生成按钮的回调函数
    global a
    if a==0 and e1.get().isdigit()==True and int(e1.get())>0:#a等于0并且输入的东西符合要求时，生成函数被触发
        a=1
        global x1
        x1=int(e1.get())
        global matrix#把一些变量全局化来进行调用
        global trans
        global c
        c=Canvas(t,width=1000,height=750,bg='white')
        c.place(x=5,y=70)
        c.create_oval(200,75,800,675)#在一个圆周上显示出这些点
        matrix=numpy.zeros((x1,x1))#把最短距离矩阵初始化
        trans=numpy.zeros((x1,x1))#把最短路径中间点初始化
        for i in range(x1):
            pi=math.pi
            c.create_oval(500+300*math.cos(2*pi*i/x1),375+300*math.sin(2*pi*i/x1),504+300*math.cos(2*pi*i/x1),379+300*math.sin(2*pi*i/x1),fill='black')
            #在大圆上生成一系列的点
            c.create_text(500+310*math.cos(2*pi*i/x1),375+310*math.sin(2*pi*i/x1),text=int(i+1))#在每个点边上生成数字
Button(t,text='存储',command=get).place(x=230,y=35)
Button(t,text='生成',command=establish).place(x=150,y=0)
def cal():#计算按钮的回调函数，采用弗洛伊德算法
    global a
    if a==2:#a=2时触发计算函数
        a=3
        for k in range(x1):
            for i in range(x1):
                for j in range(x1):
                    if matrix[i][k]!=0 and matrix[k][j]!=0:#判断两点之间是否有距离
                        if matrix[i][k]+matrix[k][j]<matrix[i][j] or matrix[i][j]==0:
                            matrix[i][j]=matrix[i][k]+matrix[k][j]
                            trans[i][j]=k+1#i,j之间的中间点变成k+1
Button(t,text='计算',command=cal).place(x=350,y=35)
Label(t,text='你想查看              到             的距离:').place(x=1040,y=110)
global getstart
global getend
getstart=Entry(t,width=5)#查看的起点
getstart.place(x=1100,y=110)
getend=Entry(t,width=5)#查看的终点
getend.place(x=1170,y=110)
T=Text(t,width=46,height=45)#最短路径显示框
T.place(x=1020,y=140)
def look():#查看按钮的回调函数
    global a
    if a==3 or a==4:#a=3或4并且输入的数据符合要求时，查看函数被触发
        if getstart.get().isdigit()==True and int(getstart.get())>0 and getend.get().isdigit()==True and int(getend.get())>0:
            a=4
            gets=int(getstart.get())
            gete=int(getend.get())
            T.insert('insert','点')
            T.insert('insert',gets)
            T.insert('insert','到')
            T.insert('insert',gete)
            T.insert('insert','的最短路径为:')
            if gete==gets:#起点和终点一样时
                T.insert('insert','你输入了两个一样的点！')
                T.insert('insert','\n')
            elif matrix[gets-1][gete-1]==0:#两点之间距离为0，即无法连接时
                T.insert('insert','这两个点之间不可通行哦！')
                T.insert('insert','\n')
            else:
                k=int(trans[gets-1][gete-1])
                T.insert('insert',gets)
                while k!=gete:#当中间点不是终点时，要继续循环
                    T.insert('insert','--->')
                    T.insert('insert',k)
                    k=int(trans[k-1][gete-1])
                T.insert('insert','--->')
                T.insert('insert',k)
                T.insert('insert','   距离为')
                T.insert('insert',matrix[gets-1][gete-1])
                T.insert('insert','\n')
Button(t,text='查看',command=look).place(x=1270,y=105)
def clear():#定义清除按钮的回调函数
    global a
    matrix=numpy.zeros((1,1))
    trans=numpy.zeros((1,1))
    T.delete(1.0,END)
    c=Canvas(t,width=1000,height=750,bg='white')
    c.place(x=5,y=70)
    c.create_oval(200,75,800,675)
    dis.delete(0,END)
    start.delete(0,END)
    end.delete(0,END)
    getstart.delete(0,END)
    getend.delete(0,END)
    e1.delete(0,END)
    a=0#将a变成0 这步很重要
Button(t,text='清空',command=clear).place(x=1150,y=770)
def guide():#定义规则按钮的回调函数
    M=Tk()
    M.title('规则')
    M.geometry('600x400')
    S=Text(M,width=80,height=30)
    S.place(x=0,y=0)
    S.insert('insert','欢迎来到最短路径计算小程序！以下是程序使用的注意事项，请认真阅读，按照规则进行！祝大家使用愉快！')
    S.insert('insert','\n')
    S.insert('insert','1.首先你需要输入一个数字，代表点的个数，然后点击【生成】按钮，会生成一个圆周，上面会生成均匀分布的点。')
    S.insert('insert','\n')
    S.insert('insert','2.现在你要输入有距离的两点和这两点之间的距离，然后点击【储存】按钮，数据会被储存，同时两点之间会连一条红线，红线上标有距离。')
    S.insert('insert','\n')
    S.insert('insert','3.两点之间距离没有方向性(即A到B的距离与B到A的距离相等)')
    S.insert('insert','\n')
    S.insert('insert','4.注意：输入的点为正整数，标号在圆周上会显示，距离为浮点数。')
    S.insert('insert','\n')
    S.insert('insert','5.若不小心输错了距离，可以更改，只需重新输入起点，终点和新的距离即可，红线上的距离会跟着更改。')
    S.insert('insert','\n')
    S.insert('insert','6.系统一开始默认两点之间距离为0(这两点无法连接)，你不需要输入这样的两点，修改时若想取消两点之间的连线，距离那一处输入0，相应的红线和距离会被消除。')
    S.insert('insert','\n')
    S.insert('insert','7.当你把所有的距离信息输入完成并确认无误之后，点击【计算】按钮，程序将会计算出任意两点之间的最短距离和路径')
    S.insert('insert','\n')
    S.insert('insert','8.最短距离优先级如下：当两点之间有两条路径最短时，经过的点标号较小的将被输出。')
    S.insert('insert','\n')
    S.insert('insert','9.计算完成后，在右边的屏幕中，输入你想知道的两点之间的距离，点击【查看】按钮，文本框中就会出现相应结果。')
    S.insert('insert','\n')
    S.insert('insert','10.当你获得了你所需要的一系列最短距离之后，可以点击【清零】按钮，每个文本框都会被清空，所有距离和点的信息也会被清除。')
    S.insert('insert','\n')
    S.insert('insert','11.请从第一条开始阅读！【手动狗头】')
Button(t,text='规则',command=guide).place(x=350,y=0)
t.mainloop()