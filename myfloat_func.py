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
    return
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
    return

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
        pentera[0]="+"
    else:
        pentera[0]="-"
    x=(pentera,pdecimal)
    imprimir(x)

    
    
    
def cerosd(a,d):
    for k in range(d,len(a)-1):
        print(d)
        if(a[k]<0.1):
            a[k]=a[k]*0.0
    return(a)
        
        
   
   
    
    
    pass
def division(a, b):
    pass


def comparacion(a, b):
    pass


def pi():
    pass


#if __name__ == "__main__":
    #print(imprimir(pi()))
l=["-",3,0,0,9]
r=[1]
a=(l,r)
j=["+",1]
k=[2]
b=(j,k)
suma(a,b)
resta(a,b)
multiplicacion(a,b)