import numpy as np
import math
def imprimir(a):
    #if(a[0][0]=="+"):
        #print("Positivo")
    #else:
        #print("Negativo")
    i=0
    j=0
    z=len(a[0])
    x=len(a[1])
    for i in range(z):
       print(a[0][i],end ='')
    print(",",end ='')
    for j in range(x):
       print(a[1][j],end ='')
    print("")
def suma(a,b):
    z1=len(a[0])
    x1=len(a[1])
    z2=len(b[0])
    x2=len(b[1])
    res1=0
    res2=0
    j=0
    i=0
    j=abs(z1-z2)
    u=abs(x1-x2)
    e=a[0]
    o=a[1]
    c=b[0]
    p=b[1]
    if(z1>z2):
        d=[None]*z1
    else:
        d=[None]*z2
    if(x1>x2):
        h=[None]*x1
    else:
        h=[None]*x2
    for i in range(j):
        c.insert(1,0)
    for i in range(u):
        o.insert(len(o),0)
    if(e[0]==c[0]):
        d[0]=e[0]
        if(z1>z2):
            c=b[0]
            e=a[0]
        else:
            c=a[0]
            e=b[0]
        if(x1>x2):
            o=b[1]
            p=a[1]
        else:
            o=a[1]
            p=b[1]
        for k in range(1,len(o)+1):
            if(o[len(o)-k]+p[len(o)-k]+res1>=10):
                h[len(o)-k]=o[len(o)-k]+p[len(o)-k]+res1-10
                res2=1
                res1=1
            else:
                    h[len(o)-k]=o[len(o)-k]+p[len(o)-k]+res1
                    res2=0
                    res1=0
        for k in range(1,len(c)):
            if(e[len(c)-k]+c[len(c)-k]+res2>=10):
                d[len(c)-k]=e[len(c)-k]+c[len(c)-k]+res2-10
                res2=1
            else:
                    d[len(c)-k]=e[len(c)-k]+c[len(c)-k]+res2
                    res2=0
        if(res2==1):
            d.insert(1,1)    
    if(e[0]!=c[0]):
        res1=0
        res2=0
        g1=[None]*len(e)
        pe1=[None]*len(e)
        g2=[None]*len(h)
        pe2=[None]*len(h)
        s=1
        t=0
        while(s<len(e)):
            if(e[s]>c[s]):
                print("1")
                d[0]=e[0]
                g1=e
                pe1=c
                g2=o
                pe2=p
                s=len(e)
                t=len(o)
            elif(e[s]<c[s]):
                print("2")
                d[0]=c[0]
                g1=c
                pe1=e
                g2=p
                pe2=o
                s=len(e)
                t=len(o)
            else:
                s=s+1
        if(c[s-1]==e[s-1]):
            while(t<len(o)):
                if(p[t]>o[t]):
                    d[0]=e[0]
                    g1=e
                    pe1=c
                    g2=p
                    pe2=o
                    t=len(o)
                elif(p[t]<o[t]):
                    d[0]=c[0]
                    g1=c
                    pe1=e
                    g2=o
                    pe2=p
                    t=len(o)
                else:
                    t=t+1
        if(o==p):
            d[0]="+"
            res1=0
            res2=0
        else:
            for k in range(1,len(o)+1):
                if(g2[len(o)-k]-res2>=pe2[len(o)-k]):
                    h[len(o)-k]=g2[len(o)-k]-pe2[len(o)-k]-res2
                    res1=0
                    res2=0
                if(g2[len(o)-k]-res2<pe2[len(o)-k]):
                    h[len(o)-k]=10+g2[len(o)-k]-pe2[len(o)-k]-res2
                    res1=1
                    res2=1
            for k in range(1,len(e)):
                if(g1[len(g1)-k]-res1>=pe1[len(g1)-k]):
                    d[len(g1)-k]=g1[len(g1)-k]-pe1[len(g1)-k]-res1
                    res1=0
                if(g1[len(g1)-k]-res1<pe1[len(g1)-k]):
                    d[len(g1)-k]=10+g1[len(g1)-k]-pe1[len(g1)-k]-res1
                    res1=1       
    
    print("Suma")
    imprimir(a)
    print("")
    imprimir(b)
    print("")
    print("  =  ")
    v=(d,h)
    imprimir(v)
    return(v)

def resta(a, b):
    print("Resta")
    if(b[0][0]=="-"):
        b[0][0]="+"
    else:
        b[0][0]="-"
    suma(a,b)
    pass


def voltear(a):
    d=[None]*len(a)
    for k in range(0,len(a)):
        d[k]=a[len(a)-1-k]
    return(d)
        
        

def multiplicacion(a, b):
    print("Multiplicacion")
    decimal=len(b[1])+len(a[1])
    t1=a[0]+a[1]
    t2=b[0]+b[1]
    c=voltear(t1)
    d=voltear(t2)
    r = [0]*(len(c)+len(d))
    p=len(c)-1
    q=len(d)-1
    for k in range(0,p):                                         
        carry = 0
        for s in range(0,q):                                        
            r[k+s] += carry + c[s] * d[k]
            carry = int(r[s+k] / 10)
            r[s+k] = int(r[s+k]%10)
        r[k + p] += carry  
    f=voltear(r)
    pentera=[0]*(len(f)-decimal)
    pdecimal=[0]*(decimal)
    for k in range(0,len(f)-decimal):
        pentera[k]=f[k]
    for g in range(len(f)-decimal,len(f)):
        pdecimal[len(f)-decimal-g]=f[g]
    if(a[0][0]==b[0][0]):
        pentera[0]="-"
    if(a[0][0]!=b[0][0]):
        pentera[0]="+"
    x=(pentera,pdecimal)
    imprimir(x)
    return(x)
def division(a, b,im):
    del a[0][0]
    del b[0][0]
    c=[]
    d=[]
    divdecimal=""
    diventero=""
    for i in range (len(a[0])):
        c.append(a[0][i])
    for j in range (len(a[1])):
        c.append(a[1][j])
    if len(a[1])<len(b[1]):
        cero=len(b[1])-len(a[1])
        for k in range(cero):
            c.append(0)
    for l in range(len(b[0])):
        d.append(b[0][l])
    for m in range (len(b[1])):
        d.append(b[1][m])
    if len(b[1])<len(a[1]):
        cero=len(a[1])-len(b[1])
        for k in range(cero):
            d.append(0)
    num1=float("".join(str(n) for n in c))
    num2=float("".join(str(o) for o in d))
    diventero+=str(int(num1/num2))
    mod=(num1%num2)*10
    for p in range (im):
        rest=int(mod/num2)
        divdecimal+=str(rest)
        mod=(mod%num2)*10
    d0=list(map(int,diventero))
    d1=list(map(int,divdecimal))
    if(a[0][0]==b[0][0]):
        d0.insert(0,"-")
    if(a[0][0]!=b[0][0]):
        d0.insert(0,"+")
    if im==101:
        if num1%num2==0:
            a1=[]
            a1.append(0)
        else:
            q=0
            while q==0:
                if a1[-1]=="0":
                    a1.pop(-1)
                else:
                    q=1
    r=(d0,d1)
    print("Division")
    imprimir(r)
    return(r)
def comparacion(c,d):
    a=[c[0],c[1]]
    b=[d[0],d[1]]
    if min(len(a[1]),len(b[1]))==len(a[1]):
        for i in range(len(b[1])-len(a[1])):
            a[1].append(0)
    if min(len(a[1]),len(b[1]))==len(b[1]):
        for i in range(len(a[1])-len(b[1])):
            b[1].append(0)
    if min(len(a[0]),len(b[0]))==len(a[0]):
        for i in range(len(b[0])-len(a[0])):
            a[0].insert(1,0)
    if min(len(a[0]),len(b[0]))==len(b[0]):
        for i in range(len(a[0])-len(b[0])):
            b[0].insert(1,0)
    if a[0]==b[0] and a[1]==b[1]:
        return True
    else:
        return False
def pi():
    c1=(["+",1],[0])
    m=(["-",1],[0])
    c2=(["+",2],[0])
    c4=(["+",4],[0])
    resultado=(["+",0],[0])
    t=0
    while t<10000:
        kfloat=(["+",t],[0])
        den=suma(multiplicacion(c2,kfloat),c1)
        if t%2==0:
            r=suma(r,division(c4,den))
        else:
            r=suma(r,multiplicacion(division(c4,den),m1))
    t+=1
    
    



#if __name__ == "__main__":
    #print(imprimir(pi()))
l=["+",3,0,0,9]
r=[1]
a=(l,r)
j=["+",1]
k=[2]
b=(j,k)
suma(a,b)
resta(a,b)
multiplicacion(a,b)
division(a,b,125)
comparacion(a,b)