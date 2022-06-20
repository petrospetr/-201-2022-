from numpy import *
import numpy as np , matplotlib.pyplot as plt, math

sqpi=np.sqrt(np.pi)
E=3.0; alpha=np.sqrt(E-0.5) 
factr=np.exp(0.5*alpha*alpha); nmax=20 

def Hermite(x,n): 
    if(n==0): 
        p=1.0
    elif(n==1): 
        p=2*x
    else: 
        p0=1
        p1=2*x
        for i in range(1,n): 
            p2=2*x*p1-2*i*p0
            p0=p1
            p1=p2
            p=p2
    return p
        
def glauber(x,t,nmax): 
    Reterm=0.0 
    Imterm=0.0 
    
    factr=np.exp(-0.5*alpha*alpha) 
    
    for n in range(0,nmax+1):
        fact=np.sqrt(1.0/(math.factorial(n)*sqpi*(2**n))) 
        psin=fact*Hermite(x,n)*np.exp(-0.5*x*x) 
        
        den=np.sqrt(math.factorial(n)) 
        
        num=factr*(alpha**n)*psin

       
        Reterm+=num*(np.cos((n+0.5)*t))/den  
        Imterm+=num*(np.sin((n+0.5)*t))/den 

        phi=Reterm*Reterm+Imterm*Imterm 
    return phi


def animate(t):
    y=glauber(xx,t,nmax)
    s=str(t)
    plt.plot(xx,y,label=s)
    leg=plt.legend(loc="best",ncol=4,mode="expand",shadow=True)

    
fig=plt.figure()  
ax=fig.add_subplot(111,autoscale_on=True,xlim=(-6,6),ylim=(0,1.5)) 
ax.grid()


plt.title(f"Glauber states at different times, nmax=%d" %nmax)
plt.xlabel("x")
plt.ylabel("$|\psi(x,t)|^2$")

xx=np.arange(-6.0,6.0,0.2)

for t in np.arange(0,3.6,0.5):
    animate(t)

plt.show()


