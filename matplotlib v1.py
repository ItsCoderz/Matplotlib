from tkinter import Tk,Label,Entry,Button,Frame,Canvas
import matplotlib.pyplot as plt

class GraphPlotter(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(500,500)
        self.title('My Line Graph Plotter')
        c=LineGraph(self)
        self.mainloop()

class LineGraph(Frame):
    def __init__(self,r):
        super().__init__(r)
        l1=Label(self,text='Equation of line is y=mx+c')
        l1.pack()
        l2=Label(self,text='Enter value for m: ')
        l2.pack()
        self.e1=Entry(self)
        self.e1.pack()
        l3=Label(self,text='Enter value for c: ')
        l3.pack()
        self.e2=Entry(self)
        self.e2.pack()
        b1=Button(self,text='Draw Line',command=self.drawLine)
        b1.pack()
        self.pack()
    def drawLine(self):
        x=[]
        y=[]
        m=int(self.e1.get())
        c=int(self.e2.get())
        for i in range (400):
            x.append(i)
            y.append(m*i+c)
        plt.plot(x,y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('My Line Graph')
        plt.show()


g=GraphPlotter()

