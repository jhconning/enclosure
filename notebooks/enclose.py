import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed

Tbar=100
Lbar=100

def f(T, L, a=1/2, th=1):
    '''production technology on commons/un-enclosed land'''
    return th * T**(1-a) * L**a

def mple(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''marginal product of Labor on enclosed land'''
    return th*a* f(te,le,a,th)/le  * tlbar**(1-a)

def mpte(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''marginal product of Land on enclosed land'''
    return th*(1-a)* f(te,le,a,th)/te  * tlbar**(-a)

def mplu(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''marginal product of Labor on unenclosed land'''
    return th*a* f(1-te,1-le,a,th)/(1-le)  * tlbar**(1-a)

def aplu(te,le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''average product of Labor on unenclosed land'''
    return th * f(1-te,1-le,a,th)/(1-le)  * tlbar**(1-a)

def lopt(te, a=1/2, th=1):
    '''optimal labor allocation (from MPLe = MPLu) given enclosed land a'''
    lam = th**(1/(1-a))
    return (lam*te)/(1-te+te*lam) 

def weq(te, th=1, alp=1/2, tlbar=1):
    lam = (th*alp)**(1/(1-alp))
    return (1-te+lam*te)**(1-alp) * (tlbar)**(1-alp)

def req(te, th=1, alp=1/2, tlbar=1):
    lam = (th*alp)**(1/(1-alp))
    return (1-alp)*th * lam**alp * (1-te+lam*te)**(-alp) * (tlbar)**(-alp)

def le(te, th, alp):
    lam = (th*alp)**(1/(1-alp))
    return lam*te/(1-te+lam*te)
 
def totalq(te, th, alp):
    '''total output in the economy given '''
    leq = le(te, th, alp)
    return f(Tbar,Lbar,alp, th) * ( th*f(te, leq, alp, th) + f(1-te, 1-leq, alp, 1) )

def plotY(alp = 0.5, th = 1, c = 1):
    '''Plot total income net of clearing costs'''
    te = np.linspace(0, 1.0, 20)
    plt.title("total output as function of enclosure te")
    plt.plot(te, totalq(te, th, alp) - c*te*Tbar)
    plt.xlabel('a')
    #plt.ylim(0,1.5)


def plotle(te=1/2, th=1, alp=1/2):
    '''Draw edgeworth box and te/le(te) ratio'''
    fig, ax = plt.subplots(figsize=(7,7))
    tte = np.linspace(0,1,50)
    leq = le(te, th, alp)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_aspect('equal', 'box')
    ax.plot(tte, tte, linestyle=':')
    ax.plot(le(tte, th, alp),tte)
    ax.plot([0, leq],[0,te],linestyle=':')
    ax.scatter(leq, te, linestyle=':')
    ax.axhline(y=te, xmin=0, xmax=leq, linestyle=':')
    ax.axvline(x=leq, ymin=0, ymax=te, linestyle=':')
    ax.set_xlabel(r'$l_e$', fontsize=15)
    ax.set_ylabel(r'$t_e$', fontsize=15)
    lam = (th*alp)**(1/(1-alp))
    ax.text(0.1, 0.9, r'$\Lambda =$'+f'{lam: 3.2f}'+r'$\ \ \ \frac{t_e}{l_e}=$'+ f'{te/(leq+0.001):3.1f}')

    
def plotreq(th=1, alp=1/2, tlbar=1, c=0, wplot=True):
    tte = np.linspace(0,1,50)
    fig, ax =  plt.subplots(figsize=(5,5))
    r0 = req(0, th, alp, tlbar)
    r1 = req(1, th, alp, tlbar)
    ax.set_xlim(0,1)
    ax.set_ylim(0,2)
    ax.plot(tte, req(tte, th, alp, tlbar),  label= r'$r$')
    ax.set_xlabel(r'$t_e$', fontsize=15)
    ax.text(1.025,r1,r'$r^*(1)$',fontsize=14)
    ax.text(-0.25,r0,r'$r^*(0)$',fontsize=14)
    ax.grid()
    ax.axhline(y=c,linestyle=':')
    if wplot:
        ax.plot(tte, weq(tte, th, alp, tlbar), label= r'$w$')
    lam = (th*alp)**(1/(1-alp))
    ax.legend()


def plotmpts(te=1/2, alp=1/2, th=1, tlbar=Tbar/Lbar):
    ll = np.linspace(0.001, 0.999, 50)
    plt.figure(figsize=(10,6))
    plt.plot(ll, mple(te, ll, alp, th, tlbar)) 
    plt.plot(ll, mplu(te, ll, alp, 1, tlbar))
    plt.plot(ll, aplu(te, ll, alp, 1, tlbar))
    plt.xlabel('l - labor')
    plt.axvline(le(te, th, alp), linestyle=':') 
    plt.axvline(lopt(te, alp, th), linestyle='-') 
    plt.title('MPL and APL on enclosed and unenclosed lands')
    plt.ylim(0,3)
    plt.xlim(0,1)

