from tkinter import *
import matplotlib.pyplot as pt
import sqlite3
from tkinter import messagebox
root=Tk()
root.geometry("900x740")
root.title("Travelling Salesman Problem")
root.config(bg='cyan')
photo=PhotoImage(file="travelling.png")
l0=Label(root,image=photo)
l0.pack()
l1=Label(root,text="TRAVELLING SALESMAN PROBLEM",fg='red',bg='cyan')
l1.config(font=('times of roman',24,'bold'))
l1.pack()
l2=Label(root,text="A travelling sales man problem involves a sales man who must make a tour of 'n' cities.\nUsing the shortest path available by visiting each city exactly once and return to the starting city. ",bg='cyan')
l2.config(font=('times',16,'bold'))
l2.pack()
l17=Label(root,text="ASSIGNED DATA",bg='cyan',fg='orangered')
l17.config(font=('times',22,'bold'))
l17.pack()
l19=Label(root,text="Click the Button below to see assigned data",bg='cyan')
l19.config(font=('times',16,'bold'))
l19.pack()
def box():
    tt = Tk()
    tt.geometry("900x390")
    tt.config(bg='springgreen')
    cit = ['City','Ludhiana','Jalandhar','Amritsar','Chandigarh','Patiala']
    matrix=[['City','Ludhiana','Jalandhar','Amritsar','Chandigarh','Patiala'],['Ludhiana',0,61,140,106,93],['Jalandhar',61,0,80,149,154],['Amritsar',140,80,0,229,235],['Chandigarh',106,149,229,0,75],['Patiala',93,154,235,75,0]]
    for i in range(6):
        for j in range(6):
            if (matrix[i][j] in cit):
                label = Label(tt,text=matrix[i][j],bd=1,bg='crimson',relief=GROOVE,width=21,height=2)
            else:
                label = Label(tt,text=matrix[i][j],bd=1,bg='orange',relief=GROOVE,width=21,height=2)
            label.grid(row=i,column=j)
    l18=Label(tt,text="A travelling sales man problem involves a sales man who must make a tour of 5 cities.\nLudhiana, Jalandhar, Amritsar, Chandigarh, Patiala.\nUsing the shortest path available by visiting each city exactly once and return to the starting city.",bg='springgreen')
    l18.config(font=('times',16,'bold'))
    l18.place(x=1,y=230)
    Button(tt,text="Back",command=tt.destroy,width=10,bg='bisque',fg='black').place(x=400,y=330)
    tt.mainloop()
Button(root,text='Show Data',command=box,bg='bisque',fg='black',width=20).pack()
def new():
     print("\n\n************** BY THE METHOD OF BRANCH AND BOUND  ***************\n\n")
     print("Let the cordinates of cities be: ")
     print("(1,5)=Ludhiana")
     print("(4,8)=Jalandhar")
     print("(5,6)=Amritsar")
     print("(6,1)=Chandigarh")
     print("(2,2)=Patiala")
     #initializing matrix
     a=[[0,61,140,106,93],
        [61,0,80,149,154],
        [140,80,0,229,235],
        [106,149,229,0,75],
        [93,154,235,75,0]]
     x=[]
     print("initialized data is: \n")
     print(a[0])
     print(a[1])
     print(a[2])
     print(a[3])
     print(a[4])
     print("\n\n\nWE HAVE ASSUMED THAT THE STARTING AND ENDING CITY IS LUDHIANA\n\n\n")
     class per:
          n=0
          def travel(self):
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Jalandhar-->Amritsar-->Chandigarh-->Patiala-->Ludhiana")
               sum=a[0][1]+a[1][2]+a[2][3]+a[3][4]+a[4][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,4,5,6,2,1],[5,8,6,1,2,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,4,5,6,2,1],[5,8,6,1,2,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Jalandhar-->Amritsar-->Patiala-->Chandigarh-->Ludhiana")
               sum=a[0][1]+a[1][2]+a[2][4]+a[4][3]+a[3][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,4,5,2,6,1],[5,8,6,2,1,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,4,5,2,6,1],[5,8,6,2,1,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Jalandhar-->Chandigarh-->Amritsar-->Patiala-->Ludhiana")
               sum=a[0][1]+a[1][3]+a[3][2]+a[2][4]+a[4][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Jalandhar-->Chandigarh-->Patiala-->Amritsar-->Ludhiana")
               sum=a[0][1]+a[1][3]+a[3][4]+a[4][2]+a[2][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,4,6,2,5,1],[5,8,1,2,6,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,4,6,2,5,1],[5,8,1,2,6,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Jalandhar-->Patiala-->Amritsar-->Chandigarh-->Ludhiana")
               sum=a[0][1]+a[1][4]+a[4][2]+a[2][3]+a[3][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,4,2,5,6,1],[5,8,2,6,1,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,4,2,5,6,1],[5,8,2,6,1,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Jalandhar-->Patiala-->Chandigarh-->Amritsar-->Ludhiana")
               sum=a[0][1]+a[1][4]+a[4][3]+a[3][2]+a[2][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,4,2,6,5,1],[5,8,2,1,6,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,4,2,6,5,1],[5,8,2,1,6,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Amritsar-->Jalandhar-->Chandigarh-->Patiala-->Ludhiana")
               sum=a[0][2]+a[2][1]+a[1][3]+a[3][4]+a[4][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,5,4,6,2,1],[5,6,8,1,2,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,5,4,6,2,1],[5,6,8,1,2,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Amritsar-->Jalandhar-->Patiala-->Chandigarh-->Ludhiana")
               sum=a[0][2]+a[2][1]+a[1][4]+a[4][3]+a[3][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,5,4,2,6,1],[5,6,8,2,1,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,5,4,2,6,1],[5,6,8,2,1,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Amritsar-->Chandigarh-->Jalandhar-->Patiala-->Ludhiana")
               sum=a[0][2]+a[2][3]+a[3][1]+a[1][4]+a[4][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               c=[1,4,6,5,2,1]
               d=[5,8,1,6,2,5]
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot(c,d,'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot(c,d,'ro')
               pt.show()
               del c
               del d
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Amritsar-->Chandigarh-->Patiala-->Jalandhar-->Ludhiana")
               sum=a[0][2]+a[2][3]+a[3][4]+a[4][1]+a[1][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               c=[1,5,6,2,4,1]
               d=[5,6,1,2,8,5]
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot(c,d,'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot(c,d,'ro')
               pt.show()
               del c
               del d
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Amritsar-->Patiala-->Jalandhar-->Chandigarh-->Ludhiana")
               sum=a[0][2]+a[2][4]+a[4][1]+a[1][3]+a[3][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,5,2,4,6,1],[5,6,2,8,1,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,5,2,4,6,1],[5,6,2,8,1,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Amritsar-->Patiala-->Chandigarh-->Jalandhar-->Ludhiana")
               sum=a[0][2]+a[2][4]+a[4][3]+a[3][1]+a[1][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,5,2,6,4,1],[5,6,2,1,8,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,5,2,6,4,1],[5,6,2,1,8,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Chandigarh-->Jalandhar-->Amritsar-->Patiala-->Ludhiana")
               sum=a[0][3]+a[3][1]+a[1][2]+a[2][4]+a[4][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,6,4,5,2,1],[5,1,8,6,2,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,6,4,5,2,1],[5,1,8,6,2,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Chandigarh-->Jalandhar-->Patiala-->Amritsar-->Ludhiana")
               sum=a[0][3]+a[3][1]+a[1][4]+a[4][2]+a[2][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,6,4,2,5,1],[5,1,8,2,6,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,6,4,2,5,1],[5,1,8,2,6,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Chandigarh-->Amritsar-->Jalandhar-->Patiala-->Ludhiana")
               sum=a[0][3]+a[3][2]+a[2][1]+a[1][4]+a[4][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,6,5,4,2,1],[5,1,6,8,2,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,6,5,4,2,1],[5,1,6,8,2,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Chandigarh-->Amritsar-->Patiala-->Jalandhar-->Ludhiana")
               sum=a[0][3]+a[3][2]+a[2][4]+a[4][1]+a[1][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,6,5,2,4,1],[5,1,6,2,8,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,6,5,2,4,1],[5,1,6,2,8,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Chandigarh-->Patiala-->Jalandhar-->Amritsar-->Ludhiana")
               sum=a[0][3]+a[3][4]+a[4][1]+a[1][2]+a[2][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,6,2,4,5,1],[5,1,2,8,6,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,6,2,4,5,1],[5,1,2,8,6,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Chandigarh-->Patiala-->Amritsar-->Jalandhar-->Ludhiana")
               sum=a[0][3]+a[3][4]+a[4][2]+a[2][1]+a[1][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,6,2,5,4,1],[5,1,2,6,8,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,6,2,5,4,1],[5,1,2,6,8,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Patiala-->Jalandhar-->Amritsar-->Chandigarh-->Ludhiana")
               sum=a[0][4]+a[4][1]+a[1][2]+a[2][3]+a[3][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,2,4,5,6,1],[5,2,8,6,1,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,2,4,5,6,1],[5,2,8,6,1,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Patiala-->Jalandhar-->Chandigarh-->Amritsar-->Ludhiana")
               sum=a[0][4]+a[4][1]+a[1][3]+a[3][2]+a[2][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,2,4,6,5,1],[5,2,8,1,6,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,2,4,6,5,1],[5,2,8,1,6,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Patiala-->Amritsar-->Jalandhar-->Chandigarh-->Ludhiana")
               sum=a[0][4]+a[4][2]+a[2][1]+a[1][3]+a[3][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,2,5,4,6,1],[5,2,6,8,1,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,2,5,4,6,1],[5,2,6,8,1,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Patiala-->Amritsar-->Chandigarh-->Jalandhar-->Ludhiana")
               sum=a[0][4]+a[4][2]+a[2][3]+a[3][1]+a[1][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               c=[1,2,5,6,4,1]
               d=[5,2,6,1,8,5]
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot(c,d,'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot(c,d,'ro')
               pt.show()
               del c
               del d
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Patiala-->Chandigarh-->Jalandhar-->Amritsar-->Ludhiana")
               sum=a[0][4]+a[4][3]+a[3][1]+a[1][2]+a[2][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               c=[1,2,6,4,5,1]
               d=[5,2,1,8,6,5]
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot(c,d,'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot(c,d,'ro')
               pt.show()
               del c
               del d
               print("\n")
               x.append(sum)
               self.n=self.n+1
               sum=0
               print("Route is as follows")
               print("Ludhiana-->Patiala-->Chandigarh-->Amritsar-->Jalandhar-->Ludhiana")
               sum=a[0][4]+a[4][3]+a[3][2]+a[2][1]+a[1][0]
               print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
               fig=pt.figure()
               rect=fig.patch
               rect.set_facecolor('green')
               g=fig.add_subplot(1,1,1,facecolor='black')
               g.plot([1,2,6,5,4,1],[5,2,1,6,8,5],'white',linewidth=4.0)
               pt.title('Shortest Distance')
               pt.xlabel('Distance(in KM)')
               pt.ylabel('Distance(in KM)')
               pt.plot([1,2,6,5,4,1],[5,2,1,6,8,5],'ro')
               pt.show()
               print("\n")
               x.append(sum)
               sum=0
               self.n=self.n+1
               print("\n\nTHE POSSIBLE NUMBER OF WAYS THAT A SALESMAN CAN TRAVEL IS: ",self.n)
               print("\n\n")
               del self.n
               a1=min(x)
               print("THE SHORTEST PATH TRAVELLED IS: ",a1,"km")
               print("\n\n")
               print("HERE ARE THE LIST OF SHORTEST PATHS: \n\n")
               if(a1==x[0]):
                    print("Ludhiana-->Jalandhar-->Amritsar-->Chandigarh-->Patiala-->Ludhiana\n")
                    fig=pt.figure()
                    rect=fig.patch
                    rect.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,4,5,6,2,1],[5,8,6,1,2,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,4,5,6,2,1],[5,8,6,1,2,5],'ro')
                    pt.show()
                    print("\n")
               if(a1==x[1]):
                    print("Ludhiana-->Jalandhar-->Amritsar-->Patiala-->Chandigarh-->Ludhiana\n")
                    fig=pt.figure()
                    rect=fig.patch
                    rect.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,4,5,2,6,1],[5,8,6,2,1,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,4,5,2,6,1],[5,8,6,2,1,5],'ro')
                    pt.show()
                    print("\n")
               if(a1==x[2]):
                    print("Ludhiana-->Jalandhar-->Chandigarh-->Amritsar-->Patiala-->Ludhiana\n")
                    fig=pt.figure()
                    rect=fig.patch
                    rect.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'ro')
                    pt.show()
                    print("\n")
               if(a1==x[3]):
                    print("Ludhiana-->Jalandhar-->Chandigarh-->Patiala-->Amritsar-->Ludhiana\n")
                    fig=pt.figure()
                    rect=fig.patch
                    rect.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,4,6,2,5,1],[5,8,1,2,6,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,4,6,2,5,1],[5,8,1,2,6,5],'ro')
                    pt.show()
                    print("\n")
               if(a1==x[4]):
                   print("Ludhiana-->Jalandhar-->Patiala-->Amritsar-->Chandigarh-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,4,2,5,6,1],[5,8,2,6,1,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,4,2,5,6,1],[5,8,2,6,1,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[5]):
                   print("Ludhiana-->Jalandhar-->Patiala-->Chandigarh-->Amritsar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')         
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,4,2,6,5,1],[5,8,2,1,6,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,4,2,6,5,1],[5,8,2,1,6,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[6]):
                   print("Ludhiana-->Amritsar-->Jalandhar-->Chandigarh-->Patiala-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,5,4,6,2,1],[5,6,8,1,2,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,5,4,6,2,1],[5,6,8,1,2,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[7]):
                   print("Ludhiana-->Amritsar-->Jalandhar-->Patiala-->Chandigarh-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,5,4,2,6,1],[5,6,8,2,1,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,5,4,2,6,1],[5,6,8,2,1,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[8]):
                   print("Ludhiana-->Amritsar-->Chandigarh-->Jalandhar-->Patiala-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[9]):
                   print("Ludhiana-->Amritsar-->Chandigarh-->Patiala-->Jalandhar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,5,6,2,4,1],[5,6,1,2,8,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,5,6,2,4,1],[5,6,1,2,8,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[10]):
                   print("Ludhiana-->Amritsar-->Patiala-->Jalandhar-->Chandigarh-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,5,2,4,6,1],[5,6,2,8,1,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,5,2,4,6,1],[5,6,2,8,1,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[11]):
                   print("Ludhiana-->Amritsar-->Patiala-->Chandigarh-->Jalandhar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,5,2,6,4,1],[5,6,2,1,8,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,5,2,6,4,1],[5,6,2,1,8,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[12]):
                   print("Ludhiana-->Chandigarh-->Jalandhar-->Amritsar-->Patiala-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,6,4,5,2,1],[5,1,8,6,2,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,6,4,5,2,1],[5,1,8,6,2,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[13]):
                   print("Ludhiana-->Chandigarh-->Jalandhar-->Patiala-->Amritsar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,6,4,2,5,1],[5,1,8,2,6,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,6,4,2,5,1],[5,1,8,2,6,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[14]):
                   print("Ludhiana-->Chandigarh-->Amritsar-->Jalandhar-->Patiala-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,6,5,4,2,1],[5,1,6,8,2,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,6,5,4,2,1],[5,1,6,8,2,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[15]):
                   print("Ludhiana-->Chandigarh-->Amritsar-->Patiala-->Jalandhar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,6,5,2,4,1],[5,1,6,2,8,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,6,5,2,4,1],[5,1,6,2,8,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[16]):
                   print("Ludhiana-->Chandigarh-->Patiala-->Jalandhar-->Amritsar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,6,2,4,5,1],[5,1,2,8,6,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,6,2,4,5,1],[5,1,2,8,6,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[17]):
                   print("Ludhiana-->Chandigarh-->Patiala-->Amritsar-->Jalandhar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,6,2,5,4,1],[5,1,2,6,8,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,6,2,5,4,1],[5,1,2,6,8,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[18]):
                   print("Ludhiana-->Patiala-->Jalandhar-->Amritsar-->Chandigarh-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,2,4,5,6,1],[5,2,8,6,1,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,2,4,5,6,1],[5,2,8,6,1,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[19]):
                   print("Ludhiana-->Patiala-->Jalandhar-->Chandigarh-->Amritsar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,2,4,6,5,1],[5,2,8,1,6,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,2,4,6,5,1],[5,2,8,1,6,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[20]):
                   print("Ludhiana-->Patiala-->Amritsar-->Jalandhar-->Chandigarh-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,2,5,4,6,1],[5,2,6,8,1,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,2,5,4,6,1],[5,2,6,8,1,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[21]):
                   print("Ludhiana-->Patiala-->Amritsar-->Chandigarh-->Jalandhar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,2,5,6,4,1],[5,2,6,1,8,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,2,5,6,4,1],[5,2,6,1,8,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[22]):
                   print("Ludhiana-->Patiala-->Chandigarh-->Jalandhar-->Amritsar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,2,6,4,5,1],[5,2,1,8,6,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,2,6,4,5,1],[5,2,1,8,6,5],'ro')
                   pt.show()
                   print("\n")
               if(a1==x[23]):
                   print("Ludhiana-->Patiala-->Chandigarh-->Amritsar-->Jalandhar-->Ludhiana\n")
                   fig=pt.figure()
                   rect=fig.patch
                   rect.set_facecolor('green')
                   g=fig.add_subplot(1,1,1,facecolor='black')
                   g.plot([1,2,6,5,4,1],[5,2,1,6,8,5],'white',linewidth=4.0)
                   pt.title('Shortest Distance')
                   pt.xlabel('Distance(in KM)')
                   pt.ylabel('Distance(in KM)')
                   pt.plot([1,2,6,5,4,1],[5,2,1,6,8,5],'ro')
                   pt.show()
                   print("\n")
     obj=per()
     obj.travel() 
def user():
    def data():
        p=[]
        q=[]
        print("Remember this applicable for only five cities ")
        print("\n\n")
        for o in range(1,6):
            print("enter the city name",o)
            e=input()
            p.append(e)
            q.append(e)
        print("points on graph")
        print("(1,5) are coordinates of",p[0])
        print("(4,8) are coordinates of",p[1])
        print("(5,6) are coordinates of",p[2])   
        print("(6,1) are coordinates of",p[3])
        print("(2,2) are coordinates of",p[4])
        print("\n\n")
        #initializing matrix
        a=[]
        r1=True
        for i in range (0,5):
            new=[]
            for j in range (0,5):
                print("enter the distance between city '"+p[i]+"'--->'"+q[j]+"'")
                w=int(input())
                new.append(w)
                if(w!=0 and i==j):
                    print("invalid data")
                    r1=False
                    break
            if(r1==False):
                break
            a.append(new)
        r2=True
        for i in range(0,5):
            for j in range(0,5):
                if(a[i][j]!=a[j][i]):
                    print("!!!  Invalid  !!!")
                    print("Values at distance between'"+p[i]+"'-->'"+q[j]+"' and '"+q[j]+"'-->'"+p[i]+"'should be equal")
                    r2=False
                    break
        if(r2==False):
            return 0
        print("initialized data is: ")
        print(a[0])
        print(a[1])
        print(a[2])
        print(a[3]) 
        print(a[4])
        x=[]
        A=p[0]
        B=p[1]
        C=p[2]
        D=p[3]
        E=p[4]
        print("\n\n\nWE HAVE ASSUMED THAT THE STARTING AND ENDING CITY AS : 'A' \n\n\n")
        class us:
            n=0
            def travelling(self):
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+B+"'-->'"+C+"'-->'"+D+"'-->'"+E+"'-->'"+A+"'")
                sum=a[0][1]+a[1][2]+a[2][3]+a[3][4]+a[4][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,4,5,6,2,1],[5,8,6,1,2,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,4,5,6,2,1],[5,8,6,1,2,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+B+"'-->'"+C+"'-->'"+E+"'-->'"+D+"'-->'"+A+"'")
                sum=a[0][1]+a[1][2]+a[2][4]+a[4][3]+a[3][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,4,5,2,6,1],[5,8,6,2,1,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,4,5,2,6,1],[5,8,6,2,1,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+B+"'-->'"+D+"'-->'"+C+"'-->'"+E+"'-->'"+A+"'")
                sum=a[0][1]+a[1][3]+a[3][2]+a[2][4]+a[4][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+B+"'-->'"+D+"'-->'"+E+"'-->'"+C+"'-->'"+A+"'")
                sum=a[0][1]+a[1][3]+a[3][4]+a[4][2]+a[2][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,4,6,2,5,1],[5,8,1,2,6,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,4,6,2,5,1],[5,8,1,2,6,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+B+"'-->'"+E+"'-->'"+C+"'-->'"+D+"'-->'"+A+"'")
                sum=a[0][1]+a[1][4]+a[4][2]+a[2][3]+a[3][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,4,2,5,6,1],[5,8,2,6,1,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,4,2,5,6,1],[5,8,2,6,1,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+B+"'-->'"+E+"'-->'"+D+"'-->'"+C+"'-->'"+A+"'")
                sum=a[0][1]+a[1][4]+a[4][3]+a[3][2]+a[2][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,4,2,6,5,1],[5,8,2,1,6,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,4,2,6,5,1],[5,8,2,1,6,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+C+"'-->'"+B+"'-->'"+D+"'-->'"+E+"'-->'"+A+"'")
                sum=a[0][2]+a[2][1]+a[1][3]+a[3][4]+a[4][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,5,4,6,2,1],[5,6,8,1,2,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,5,4,6,2,1],[5,6,8,1,2,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+C+"'-->'"+B+"'-->'"+E+"'-->'"+D+"'-->'"+A+"'")
                sum=a[0][2]+a[2][1]+a[1][4]+a[4][3]+a[3][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,5,4,2,6,1],[5,6,8,2,1,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,5,4,2,6,1],[5,6,8,2,1,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+C+"'-->'"+D+"'-->'"+B+"'-->'"+E+"'-->'"+A+"'")
                sum=a[0][2]+a[2][3]+a[3][1]+a[1][4]+a[4][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+C+"'-->'"+D+"'-->'"+E+"'-->'"+B+"'-->'"+A+"'")
                sum=a[0][2]+a[2][3]+a[3][4]+a[4][1]+a[1][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,5,6,2,4,1],[5,6,1,2,8,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,5,6,2,4,1],[5,6,1,2,8,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+C+"'-->'"+E+"'-->'"+B+"'-->'"+D+"'-->'"+A+"'")
                sum=a[0][2]+a[2][4]+a[4][1]+a[1][3]+a[3][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,5,2,4,6,1],[5,6,2,8,1,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,5,2,4,6,1],[5,6,2,8,1,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+C+"'-->'"+E+"'-->'"+D+"'-->'"+B+"'-->'"+A+"'")
                sum=a[0][2]+a[2][4]+a[4][3]+a[3][1]+a[1][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,5,2,6,4,1],[5,6,2,1,8,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,5,2,6,4,1],[5,6,2,1,8,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+D+"'-->'"+B+"'-->'"+C+"'-->'"+E+"'-->'"+A+"'")
                sum=a[0][3]+a[3][1]+a[1][2]+a[2][4]+a[4][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,6,4,5,2,1],[5,1,8,6,2,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,6,4,5,2,1],[5,1,8,6,2,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+D+"'-->'"+B+"'-->'"+E+"'-->'"+C+"'-->'"+A+"'")
                sum=a[0][3]+a[3][1]+a[1][4]+a[4][2]+a[2][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,6,4,2,5,1],[5,1,8,2,6,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,6,4,2,5,1],[5,1,8,2,6,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+D+"'-->'"+C+"'-->'"+B+"'-->'"+E+"'-->'"+A+"'")
                sum=a[0][3]+a[3][2]+a[2][1]+a[1][4]+a[4][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,6,5,4,2,1],[5,1,6,8,2,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,6,5,4,2,1],[5,1,6,8,2,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+D+"'-->'"+C+"'-->'"+E+"'-->'"+B+"'-->'"+A+"'")
                sum=a[0][3]+a[3][2]+a[2][4]+a[4][1]+a[1][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,6,5,2,4,1],[5,1,6,2,8,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,6,5,2,4,1],[5,1,6,2,8,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+D+"'-->'"+E+"'-->'"+B+"'-->'"+C+"'-->'"+A+"'")
                sum=a[0][3]+a[3][4]+a[4][1]+a[1][2]+a[2][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,6,2,4,5,1],[5,1,2,8,6,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,6,2,4,5,1],[5,1,2,8,6,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+D+"'-->'"+E+"'-->'"+C+"'-->'"+B+"'-->'"+A+"'")
                sum=a[0][3]+a[3][4]+a[4][2]+a[2][1]+a[1][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,6,2,5,4,1],[5,1,2,6,8,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,6,2,5,4,1],[5,1,2,6,8,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+E+"'-->'"+B+"'-->'"+C+"'-->'"+D+"'-->'"+A+"'")
                sum=a[0][4]+a[4][1]+a[1][2]+a[2][3]+a[3][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,2,4,5,6,1],[5,2,8,6,1,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,2,4,5,6,1],[5,2,8,6,1,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+E+"'-->'"+B+"'-->'"+D+"'-->'"+C+"'-->'"+A+"'")
                sum=a[0][4]+a[4][1]+a[1][3]+a[3][2]+a[2][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,2,4,6,5,1],[5,2,8,1,6,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,2,4,6,5,1],[5,2,8,1,6,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+E+"'-->'"+C+"'-->'"+B+"'-->'"+D+"'-->'"+A+"'")
                sum=a[0][4]+a[4][2]+a[2][1]+a[1][3]+a[3][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,2,5,4,6,1],[5,2,6,8,1,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,2,5,4,6,1],[5,2,6,8,1,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+E+"'-->'"+C+"'-->'"+D+"'-->'"+B+"'-->'"+A+"'")
                sum=a[0][4]+a[4][2]+a[2][3]+a[3][1]+a[1][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,2,5,6,4,1],[5,2,6,1,8,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,2,5,6,4,1],[5,2,6,1,8,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+E+"'-->'"+D+"'-->'"+B+"'-->'"+C+"'-->'"+A+"'")
                sum=a[0][4]+a[4][3]+a[3][1]+a[1][2]+a[2][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,2,6,4,5,1],[5,2,1,8,6,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,2,6,4,5,1],[5,2,1,8,6,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                self.n=self.n+1
                sum=0
                print("Route is as follows")
                print("'"+A+"'-->'"+E+"'-->'"+D+"'-->'"+C+"'-->'"+B+"'-->'"+A+"'")
                sum=a[0][4]+a[4][3]+a[3][2]+a[2][1]+a[1][0]
                print("TOTAL DISTANCE NEED TO BE TRAVELLED IS: ",sum,"km")
                fig=pt.figure()
                r=fig.patch
                r.set_facecolor('green')
                g=fig.add_subplot(1,1,1,facecolor='black')
                g.plot([1,2,6,5,4,1],[5,2,1,6,8,5],'white',linewidth=4.0)
                pt.title('Shortest Distance')
                pt.xlabel('Distance(in KM)')
                pt.ylabel('Distance(in KM)')
                pt.plot([1,2,6,5,4,1],[5,2,1,6,8,5],'ro')
                pt.show()
                print("\n")
                x.append(sum)
                sum=0
                self.n=self.n+1
                print("\n\nTHE POSSIBLE NUMBER OF WAYS THAT A SALESMAN CAN TRAVEL IS: ",self.n)
                print("\n\n")
                a1=min(x)
                print("THE SHORTEST PATH TRAVELLED IS: ",a1,"km")
                print("\n\n")
                print("HERE ARE THE LIST OF SHORTEST PATHS: \n\n")
                if(a1==x[0]):
                    print("'"+A+"'-->'"+B+"'-->'"+C+"'-->'"+D+"'-->'"+E+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    pt.plot([1,4,5,6,2,1],[5,8,6,1,2,5],'ro')
                    pt.show()
                if(a1==x[1]):
                    print("'"+A+"'-->'"+B+"'-->'"+C+"'-->'"+E+"'-->'"+D+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,4,5,2,6,1],[5,8,6,2,1,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,4,5,2,6,1],[5,8,6,2,1,5],'ro')
                    pt.show()
                if(a1==x[2]):
                    print("'"+A+"'-->'"+B+"'-->'"+D+"'-->'"+C+"'-->'"+E+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    pt.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'ro')
                    pt.show()
                if(a1==x[3]):
                    print("'"+A+"'-->'"+B+"'-->'"+D+"'-->'"+E+"'-->'"+C+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,4,6,2,5,1],[5,8,1,2,6,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,4,6,2,5,1],[5,8,1,2,6,5],'ro')
                    pt.show()
                if(a1==x[4]):
                    print("'"+A+"'-->'"+B+"'-->'"+E+"'-->'"+C+"'-->'"+D+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,4,2,5,6,1],[5,8,2,6,1,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,4,2,5,6,1],[5,8,2,6,1,5],'ro')
                    pt.show()
                if(a1==x[5]):
                    print("'"+A+"'-->'"+B+"'-->'"+E+"'-->'"+D+"'-->'"+C+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,4,2,6,5,1],[5,8,2,1,6,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,4,2,6,5,1],[5,8,2,1,6,5],'ro')
                    pt.show()
                if(a1==x[6]):
                    print("'"+A+"'-->'"+C+"'-->'"+B+"'-->'"+D+"'-->'"+E+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,5,4,6,2,1],[5,6,8,1,2,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,5,4,6,2,1],[5,6,8,1,2,5],'ro')
                    pt.show()
                if(a1==x[7]):
                    print("'"+A+"'-->'"+C+"'-->'"+B+"'-->'"+E+"'-->'"+D+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,5,4,2,6,1],[5,6,8,2,1,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,5,4,2,6,1],[5,6,8,2,1,5],'ro')
                    pt.show()
                if(a1==x[8]):
                    print("'"+A+"'-->'"+C+"'-->'"+D+"'-->'"+B+"'-->'"+E+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,4,6,5,2,1],[5,8,1,6,2,5],'ro')
                    pt.show()
                if(a1==x[9]):
                    print("'"+A+"'-->'"+C+"'-->'"+D+"'-->'"+E+"'-->'"+B+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,5,6,2,4,1],[5,6,1,2,8,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,5,6,2,4,1],[5,6,1,2,8,5],'ro')
                    pt.show()  
                if(a1==x[10]):
                    print("'"+A+"'-->'"+C+"'-->'"+E+"'-->'"+B+"'-->'"+D+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,5,2,4,6,1],[5,6,2,8,1,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,5,2,4,6,1],[5,6,2,8,1,5],'ro')
                    pt.show()
                if(a1==x[11]):
                    print("'"+A+"'-->'"+C+"'-->'"+E+"'-->'"+D+"'-->'"+B+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,5,2,6,4,1],[5,6,2,1,8,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,5,2,6,4,1],[5,6,2,1,8,5],'ro')
                    pt.show()
                if(a1==x[12]):
                    print("'"+A+"'-->'"+D+"'-->'"+B+"'-->'"+C+"'-->'"+E+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,6,4,5,2,1],[5,1,8,6,2,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,6,4,5,2,1],[5,1,8,6,2,5],'ro')
                    pt.show()
                if(a1==x[13]):
                    print("'"+A+"'-->'"+D+"'-->'"+B+"'-->'"+E+"'-->'"+C+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,6,4,2,5,1],[5,1,8,2,6,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,6,4,2,5,1],[5,1,8,2,6,5],'ro')
                    pt.show()
                if(a1==x[14]):
                    print("'"+A+"'-->'"+D+"'-->'"+C+"'-->'"+B+"'-->'"+E+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,6,5,4,2,1],[5,1,6,8,2,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,6,5,4,2,1],[5,1,6,8,2,5],'ro')
                    pt.show()
                if(a1==x[15]):
                    print("'"+A+"'-->'"+D+"'-->'"+C+"'-->'"+E+"'-->'"+B+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,6,5,2,4,1],[5,1,6,2,8,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,6,5,2,4,1],[5,1,6,2,8,5],'ro')
                    pt.show()
                if(a1==x[16]):
                    print("'"+A+"'-->'"+D+"'-->'"+E+"'-->'"+B+"'-->'"+C+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,6,2,4,5,1],[5,1,2,8,6,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,6,2,4,5,1],[5,1,2,8,6,5],'ro')
                    pt.show()
                if(a1==x[17]):
                    print("'"+A+"'-->'"+D+"'-->'"+E+"'-->'"+C+"'-->'"+B+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,6,2,5,4,1],[5,1,2,6,8,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,6,2,5,4,1],[5,1,2,6,8,5],'ro')
                    pt.show()
                if(a1==x[18]):
                    print("'"+A+"'-->'"+E+"'-->'"+B+"'-->'"+C+"'-->'"+D+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,2,4,5,6,1],[5,2,8,6,1,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,2,4,5,6,1],[5,2,8,6,1,5],'ro')
                    pt.show()
                if(a1==x[19]):
                    print("'"+A+"'-->'"+E+"'-->'"+B+"'-->'"+D+"'-->'"+C+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,2,4,6,5,1],[5,2,8,1,6,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,2,4,6,5,1],[5,2,8,1,6,5],'ro')
                    pt.show()
                if(a1==x[20]):
                    print("'"+A+"'-->'"+E+"'-->'"+C+"'-->'"+B+"'-->'"+D+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,2,5,4,6,1],[5,2,6,8,1,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,2,5,4,6,1],[5,2,6,8,1,5],'ro')
                    pt.show()
                if(a1==x[21]):
                    print("'"+A+"'-->'"+E+"'-->'"+C+"'-->'"+D+"'-->'"+B+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,2,5,6,4,1],[5,2,6,1,8,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,2,5,6,4,1],[5,2,6,1,8,5],'ro')
                    pt.show()
                if(a1==x[22]):
                    print("'"+A+"'-->'"+E+"'-->'"+D+"'-->'"+B+"'-->'"+C+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,2,6,4,5,1],[5,2,1,8,6,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,2,6,4,5,1],[5,2,1,8,6,5],'ro')
                    pt.show()
                if(a1==x[23]):
                    print("'"+A+"'-->'"+E+"'-->'"+D+"'-->'"+C+"'-->'"+B+"'-->'"+A+"'")
                    fig=pt.figure()
                    r=fig.patch
                    r.set_facecolor('green')
                    g=fig.add_subplot(1,1,1,facecolor='black')
                    g.plot([1,2,6,5,4,1],[5,2,1,6,8,5],'white',linewidth=4.0)
                    pt.title('Shortest Distance')
                    pt.xlabel('Distance(in KM)')
                    pt.ylabel('Distance(in KM)')
                    pt.plot([1,2,6,5,4,1],[5,2,1,6,8,5],'ro')
                    pt.show()
        ob=us()
        ob.travelling()  
    raw=Tk()
    raw.geometry("700x500") 
    raw.config(bg='cornflowerblue')       
    l6=Label(raw,text="Remember this is only for 5 cities",bg='cornflowerblue',fg='red')
    l6.config(font=('times',28,'bold'))
    l6.pack()
    username=StringVar()
    password=StringVar()
    l7=Label(raw,text="Login",bg='cornflowerblue')
    l7.config(font=('times',24,'bold'))
    l7.place(x=100,y=60)    
    l8=Label(raw,text="Enter your username:",bg='cornflowerblue')
    l8.place(x=50,y=120)        
    e5=Entry(raw,textvar=username,bd=5)
    e5.place(x=200,y=120)
    l9=Label(raw,text="Enter password:",bg='cornflowerblue')
    l9.place(x=50,y=160)
    e6=Entry(raw,textvar=password,bd=5,show="*")
    e6.place(x=200,y=160)
    def database(u1,p1):
        con=sqlite3.connect("tspdata.db")
        #con.execute("create table tsp(username varchar(30) primary key ,password varchar(10))")
        c=con.execute("select * from tsp where username='"+u1.get()+"' and password='"+p1.get()+"'")
        if(u1.get()=="" or p1.get()==""):
            messagebox.showwarning('note','please check the username and password')
        else:
            r=c.fetchall()
            if(len(r)!=0):
                messagebox.showinfo('Access','Acess Granted: welcome '+u1.get())
                data()
            else:
                messagebox.showerror('note','Acess Denied')        
    register=StringVar()
    passw=StringVar()
    l12=Label(raw,text="Register",bg='cornflowerblue')
    l12.config(font=('times',24,'bold'))
    l12.place(x=100,y=260)
    l13=Label(raw,text="Username:",bg='cornflowerblue')
    l13.place(x=50,y=320)        
    e7=Entry(raw,textvar=register,bd=5)
    e7.place(x=200,y=320)
    l14=Label(raw,text="Password:",bg='cornflowerblue')
    l14.place(x=50,y=360)
    e8=Entry(raw,textvar=passw,bd=5,show="*")
    e8.place(x=200,y=360)
    def reg(u2,p2):
        name=register.get() 
        pas=passw.get()
        if(u2.get()=="" or p2.get()==""):
             messagebox.showwarning('note','Fill the requirements')
        else:
            con=sqlite3.connect("tspdata.db")
            #con.execute("create table tsp(username varchar(30) primary key ,password varchar(10))")
            con.execute("insert into tsp(username,password)values(?,?)",(e7.get(),e8.get()))
            messagebox.showinfo('Registration',' Your registration has done')
            con.commit()  
    def clearreg():
        e7.delete(0,"end")
        e8.delete(0,"end")
    def clearlog():
         e5.delete(0,"end")
         e6.delete(0,"end")
    Button(raw,text="submit",bg='bisque',fg='black',command=lambda:database(e5,e6),width=20).place(x=100,y=200)
    Button(raw,text="Register Now",bg='bisque',fg='black',command=lambda:reg(e7,e8),width=20).place(x=100,y=400)
    Button(raw,text="Back",command=raw.destroy,bg='bisque',fg='black',width=10).place(x=500,y=450)
    Button(raw,text="Clear",command=clearreg,bg='bisque',fg='black',width=10).place(x=300,y=400)
    Button(raw,text="Clear",command=clearlog,bg='bisque',fg='black',width=10).place(x=300,y=200)
    raw.mainloop()  
l20=Label(root,text="Click here to execute the assigned data",bg='cyan')
l20.config(font=('times',16,'bold'))
l20.pack()  
b1=Button(root,text="Execute",fg='black',bg='bisque',width=20,command=new)
b1.pack()
l8=Label(root,text="Click on the button below to enter the values by user manually",fg="orangered",bg='cyan')
l8.config(font=('times',16,'bold'))
l8.pack() 
b2=Button(root,text="User Execution",fg='black',bg='bisque',width=20,command=user)
b2.pack()
root.mainloop()
