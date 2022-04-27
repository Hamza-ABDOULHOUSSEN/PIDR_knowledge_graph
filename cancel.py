from math import exp,sqrt
import matplotlib.pyplot as plt

def poisson(l,k):
    som=0
    for i in range(k+1):
        som+=l**i/fact(i)
    return som*exp(-l)
    
def fact(k):
    if k==0:
        return 1
    else: 
        return k*fact(k-1)
        
#print(poisson(15,22))

effectif = [5,16,32,31,11,5]
valeur = [105, 115, 125, 135, 145, 155]

def moyenne(effectif, valeur):
    som = 0
    tot = 0
    for k in range(len(valeur)):
        som+= effectif[k]*valeur[k]
        tot+=effectif[k]
    return som/tot

m = moyenne(effectif,valeur)
print(m)

def ecart_type(effectif, valeur):
    m = moyenne(effectif,valeur)
    e = 0
    tot = 0
    for k in range(len(valeur)):
        e+=effectif[k]*(valeur[k]-m)**2
        tot+=effectif[k]
    return sqrt(e/(tot-1))

print(ecart_type(effectif,valeur))

# plt.close()
# plt.bar(valeur, effectif)
# plt.show()