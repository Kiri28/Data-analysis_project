import random
import math

#Take start temperature
def Temperature(StartTempr,i):
    return(StartTempr*(0.1/(i+1)))

#Make probablity to changing point position to upper- condition position
def stochast(dE,Ti):
    return math.exp(-dE/Ti)

#ВЫдача решений по вероятности
def solution(prb):
    realSol=1.0-prb
    if random.uniform(0.0, 1.0)-realSol<0:
        return(1)
    else: return(0)

# Двумерная модель
def twoD-model(test_rait):
    Tt=100
    H=test_rait[random.randint(0, 100)]
    Itspp=[]
    i=-1
    while Tt>0.2:
        i+=1
        Sc=test_rait[random.randint(0, 100)]
        E=H-Sc
        if E>0:
            H=Sc
        else:
            if solution(stochast(E,Tt))==1:
                H=Sc    
        Tt= Temperature(100,(i+1))
        Itspp.append(H)
    return(Itspp)


#Алгоритм имитации отжига для трёхмерной модели с построением точек
def threeD-model(Itog_list):
    Itt=Itog_list.reshape((11,9,3))
    Tt=100
    H=Itt[random.randint(0, 11),random.randint(0, 9),1]
    Itspp=[]
    span=[]
    i=-1
    while Tt>0.2:
        i+=1
        a=random.randint(0, 10)
        b=random.randint(0, 8)
        Sc=Itt[a,b,1]
        span.append((a,Itt[a,b,1],b))
        E=H-Sc
        if E>0:
            H=Sc
        else:
            if solution(stochast(E,Tt))==1:
                H=Sc    
        Tt= Temperature(100,(i+1))
        Itspp.append(H)
    return(Itspp)
