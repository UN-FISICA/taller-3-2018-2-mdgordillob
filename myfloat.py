import math
import decimal

def cc1(f):
    float_string = repr(f)
    if 'e' in float_string:
        digits, exp = float_string.split('e')
        digits = digits.replace('.', '').replace('-', '')
        exp = int(exp)
        zero_padding = '0' * (abs(int(exp)) - 1)  
        sign = '-' if f < 0 else ''
        if exp > 0:
            float_string = '{}{}{}.0'.format(sign, digits, zero_padding)
        else:
            float_string = '{}0.{}{}'.format(sign, zero_padding, digits)
    return float_string
def imprimir(a):
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
        d=[0]*z1
    else:
        d=[0]*z2
    if(x1>x2):
        h=[0]*x1
    else:
        h=[0]*x2
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
        for i in range(j):
            c.insert(1,0)
        for i in range(u):
            o.insert(len(o),0)
        
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
        g1=[0]*len(d)
        pe1=[0]*len(d)
        g2=[0]*len(h)
        pe2=[0]*len(h)
        s=1
        t=0
        while(s<len(e)):
            if(e[s]>c[s]):
                d[0]=e[0]
                g1=e
                pe1=c
                g2=o
                pe2=p
                s=len(e)
                t=len(o)
            elif(e[s]<c[s]):
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
                    d[0]=e[0]
                    g1=e
                    pe1=c
                    g2=o
                    pe2=p
                    t=len(o)
                else:
                    t=t+1
        if(len(g2)>len(pe2)):
            h=[0]*len(o)
            x1=len(pe2)
            while(x1<len(g2)):
                pe2.insert(len(pe2),0)
                x1=x1+1
        if(len(g2)<len(pe2)):
            h=[0]*len(p)
            x1=len(g2)
            while(x1<len(pe2)):
                g2.insert(len(g2),0)
                x1=x1+1
        if(len(g2)==len(pe2)):
            x1=len(g2)
        for k in range(1,len(pe2)+1):
            if(g2[x1-k]-res2>=pe2[x1-k]):
                h[x1-k]=g2[len(o)-k]-pe2[x1-k]-res2
                res1=0
                res2=0
            if(g2[x1-k]-res2<pe2[x1-k]):
                h[x1-k]=10+g2[x1-k]-pe2[x1-k]-res2
                res1=1
                res2=1
        for k in range(1,len(e)):
            if(g1[len(g1)-k]-res1>=pe1[len(g1)-k]):
                d[len(g1)-k]=g1[len(g1)-k]-pe1[len(g1)-k]-res1
                res1=0
            if(g1[len(g1)-k]-res1<pe1[len(g1)-k]):
                d[len(g1)-k]=10+g1[len(g1)-k]-pe1[len(g1)-k]-res1
                res1=1       
    v=(d,h)
    return(v)

def resta(a, b):
    print("Resta")
    if(b[0][0]=="-"):
        b[0][0]="+"
    if(b[0][0]=="+"):
        b[0][0]="-"
    return(suma(a,b))

def cc(b):
    if b<0:
        t=-1*b
    else:
        t=b
    u=cc1(t)
    if type(b) is int:
        k=list(map(int, str(t)))
        l=[0]
    if type(b) is float:
        k=list(map(int, str(int(t))))
        l=list(map(int, u.split('.')[1]))
    if b>=0:
        k.insert(0,'+')
    else:
        k.insert(0,'-')
    return(k,l)

def pi():
	pi=MyFloat(0)
	for y in range(0,3000):
		pi=pi+(((-1)**y )/(2*y+1))
	pi=4*pi
	return pi
        
def sumatupla(a):
	c=a[0]+a[1]
	c.pop(0)
	return c
def multiplicacion(a, b):
	c=sumatupla(a)
	d=sumatupla(b)
	decimal=len(a[1])+len(b[1])
	res1=0
	z=0
	m1=[]
	m2=[]
	for i in range(len(d)):
		m1.append([])
		if z>=1:
			for k in range(z):
				m1[i].insert(0,0)
		for m in range (len(c)):
			mul=(((c[-m-1]*d[-i-1])+res1))%10
			res1=int(((c[-m-1]*d[-i-1])+res1)/10)
			m1[i].insert(0,mul)
		if (c[0]*d[-i-1])+res1>9:
			m1[i].insert(0,res1)        
		z+=1
		res1=0
	for k in range(len(m1)):
		longitud=len(m1[-1])-len(m1[k])
		for m in range(longitud):
			m1[k].insert(0,0)
	suma=0
	res1=0
	for k in range (len(m1[0])):
		if len(m2)==len(m1[0])-1:
			m1[0].insert(0,0)
		for m in range (len(m1)):
			suma=m1[m][-k-1]+suma
		if suma>9:
			total=suma%10
			m2.insert(0,total)
			res1=int(suma/10)
		else:
			m2.insert(0,suma)
			res1=0
		m1[0][-k-2]+=res1
		suma=0
	if res1!=0:
		m2.insert(0,m1[0][0])
	d0=[]
	d1=[]
	for k in range (decimal):
		d1.append(m2[-decimal+k])
	for k in range(len(m2)-decimal):
		d0.append(m2[k])
	for k in range (len(d1)):
		if len(d1)==1:
			break
		else:
			if d1[-1]==0:
				d1.pop(-1)
	if(a[0][0]!=b[0][0]):
		d0.insert(0,"-")
	if(a[0][0]==b[0][0]):
		d0.insert(0,"+")
	t=(d0,d1)
	return(t)

    
    
    
def cerosd(a,d):
    for k in range(d,len(a)-1):
        print(d)
        if(a[k]<0.1):
            a[k]=a[k]*0.0
    return(a)
        
        
   
   
    
    
    pass
def division(a, b, interval):
    c=[]
    d=[]
    div1=""
    div2=""
    c=sumatupla(a)
    d=sumatupla(b)
    if len(b[1])<len(a[1]):
        z=len(a[1])-len(b[1])
        for k in range(z):
            d.append(0)
    l=float("".join(str(n) for n in c))
    h=float("".join(str(o) for o in d))
    div2o+=str(int(l/h))
    mod=(l%h)*10
    for p in range (interval):
        rest=int(mod/h)
        div1+=str(rest)
        mod=(mod%h)*10
    d0=list(map(int,div2))
    d1=list(map(int,div1))
    if(a[0][0]==b[0][0]):
        d0.insert(0,"-")
    if(a[0][0]!=b[0][0]):
        d0.insert(0,"+")
    if interval==101:
        if l%h==0:
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

class MyFloat:
    def __init__(self,other1):
        if(type(other1)is float) or (type(other1)is int):
            self.other1=cc(other1)
        else:
            self.other1=other1

    def __add__(self,other):
        
        if isinstance (other , MyFloat ):
            return MyFloat(suma(self.other1,other.other1))
        elif isinstance (other ,( int , float )):
            return MyFloat(suma(self.other1,cc(other)))
        else: 
            return NotImplemented

    def __sub__(self,other):
        if isinstance (other , MyFloat ):
            return MyFloat(resta(self.other1,other.other1))
        elif isinstance (other ,( int , float )):
            return MyFloat(resta(self.other1,cc(other)))
        else: 
            return NotImplemented

    def __mul__(self,other):
        if isinstance (other , MyFloat ):
            return MyFloat(multiplicacion(self.other1,other.other1))
        elif isinstance (other ,( int , float )):
            return MyFloat(multiplicacion(self.other1,cc(other)))
        else:
            return NotImplemented

    def __truediv__(self,other):
        if isinstance (other , MyFloat ):
            return MyFloat(division(self.other1,other.other1,200))
        elif isinstance (other ,( int , float )):
            return MyFloat(division(self.other1,cc(other),2000))
        else:
            return NotImplemented
        
    def __radd__(self,other):
        return self.__add__(other)

    def __rsub__(self,other):
        return self.__sub__(other)*-1
    
    def __rmul__(self,other):
        return self.__mul__(other)
    

    def __rtruediv__(self,other):
        t=MyFloat(other)
        return t/self

    def __str__(self):
        return imprimir(self.other1)

    def __repr__(self):
        return imprimir(self.other1)

    def __eq__(self,other):
         if isinstance (other , MyFloat ):
             return comparacion(self.other1,other.other1)
         elif isinstance (other ,( int , float )):
             return comparacion(self.other1,cc(other))

    def __ne__(self,other):
        return not self.__eq__(other)
        pass
if __name__ == "__main__":
   a=pi()
   print(a)
