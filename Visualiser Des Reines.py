#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *


# In[ ]:


echiquier=[] #tableau NxN
pos_reine=[] #Les positions des N reines
sol=[]


# In[ ]:


#Procedure d'initialisation

def init_echiquier(n):
 for i in range(0,n):
    pos_reine.append(0)
    li=[]
 for k in range(0,n):
    li.append(0)
 echiquier.append(li)


# In[ ]:


#Procedure d'affichage de toutes les solutions possibles

def affiche():              
 for ligne in echiquier:
    for case in ligne:

        
     print(case,"",end="")
 print("")
print("")


# In[ ]:


#Procedures de placer les reines sur l'echiquier

def poser(n):
 for i in range(0,n):
    for k in range(0,n):
        echiquier[i][k]=0
 for i in range(0,n):
 
    echiquier[pos_reine[i]][i]=1
    affiche()


# In[ ]:


#Fonction de teste si la case est libre 

def valide(li ,co):
 for i in range(0,co):
    if pos_reine[i]==li or abs(pos_reine[i]-li)==abs(i-co):
     return 0
 return 1


# In[ ]:


#Fonction recursive qui fait la recherche des solutions 

def cherche_solution(r,n):
     global k,x,t,sol 
     if(r==n): 
         sol=sol+pos_reine
         print(pos_reine)
         x=int(k.get())+1
         k.set(x)
     else :
       for i in range(0,n):  
             if(valide(i,r)): 
                 pos_reine[r]=i 
                 cherche_solution(r+1,n) 


# In[ ]:


def calculer(n):
 global k,clic,pos_reine,sol
 sol=[]
 clic.set(0)
 pos_reine=[]
 k.set(0)
 init_echiquier(n)
 cherche_solution(0,n)


# In[ ]:


def voir (n):
    global clic,k
    clic=int(clic.get())-1
    d=600//n
    for i in range(n):
        r=list(range(n))
        for j in range(n):
            r[i]=list(range(n))
            lo=i*d
            ha=j*d
            r[i][j]=c.create_rectangle(lo,ha,lo+d,ha+d,outline='black',fill='white')
            for i in range (n*clic,n*clic+n):
                c.create_oval(sol[i]*d+1,(i-n*clic)*d+1,sol[i]*d+d-1,(i-n*clic)*d++-1,fill='black')
                if clic+1<int(k.get()):
                    clic=clic+1
                    clic.set(clic+1)


# In[ ]:


x=0
sol=[]
f=Tk()   #Recherche solution(0)
clic=StringVar()
clic.set(1)
k=StringVar()
k.set(0)
c = Canvas(f,bg='white',height=600,width=600)
c.pack(side=LEFT)
spin=Spinbox(f, values=(4,5,6,7,8,9,10,11), width=4)
spin.config( font="sans 12", justify="center")
spin.pack()
b=Button(f,text="calculer",command=lambda:calculer(int(spin.get())))
b.pack()
ll=Label(f,text="nombre de solutions")
ll.pack()
l=Label(f,textvariable=k)
l.pack()
Label(f).pack()
bb=Button(f,text="voir des solutions",command=lambda:voir(int(spin.get())))
bb.pack()
lll=Label(f,textvariable=clic)
lll.pack()
f.mainloop()
print(k.get())
print(sol)

