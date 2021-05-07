# -*- coding: cp1252 -*-
import numpy as np
import matplotlib.pyplot as plt
import tp1_lib as tp

## Initialisation des donn�es 
Lx = 1.0                     # Demi longueur de l'intervalle       
a = 2.0                      # Vitesse du signal 
tmax = 2.0                   # Temps max de la simulation (=T)

J= 201                       # Nombre de noeuds
X = np.linspace(-Lx,Lx,J)    # Abscisses des noeuds
dx = X[1]-X[0]               # Pas de maillage
cfl = 0.8                    # Nombre CFL 
dt = cfl*dx/a                # Valeur du pas de temps 

## Initialisation de la solution 
Uini = tp.Uinit(X,J)         
U1 = Uini   # Schema 1
U2 = Uini   # Schema 2
U3 = Uini   # Schema 3


#Boucle en temps (tant que time < tmax) 
time = 0.0                     
while time < tmax :
    dt_reel = min(dt, tmax-time)   # dt_reel = dt sauf si tmax - time < dt 
    alpha = a*dt_reel/dx           # Nombre CFL effectif 
    print(' TIME ITERATION : ' , time , ' \ ' , tmax)
    U1 = tp.schema1(U1,J,alpha)    # Mise � jour de la solution schema 1
    U2 = tp.schema2(U2,J,alpha)    # Mise � jour de la solution schema 2
    U3 = tp.schema3(U3,J,alpha)    # Mise � jour de la solution schema 3
    time += dt_reel                # Incr�mente le temps 
 
## Affichage des r�sultats
fig=plt.figure(1)
plt.title("Solution u en fonction de x pour CFL = "+str(cfl)+" et T = "+str(tmax))
plt.xlabel('x')
plt.ylabel('u')
plt.axis([-1 , 1 , -0.25, 1.25])
plt.plot(X,U1,'-g',X,U2,'-b',X,U3,'-r',X,Uini,'-k')
plt.legend(['Schema1','Schema2', 'Schema3', 'Exacte'],loc='best')
plt.grid(True)     
plt.show(block=False)
plt.pause(10.0)  ## Pause pour voir la figure avant sauvegarde
plt.savefig("u=f(x)"+"T="+str(tmax)+"_CFL ="+str(cfl)+".png")  ##sauve figure
plt.close('all')


xi = np.linspace(0, np.pi/8.,1000)
fig=plt.figure(2)
plt.title('Erreur d\'amplitude sch�ma 1')
plt.xlabel('xi')
plt.ylabel('E(xi)')
plt.plot(xi, tp.E1(xi,0.2))
plt.plot(xi, tp.E1(xi,0.5))
plt.plot(xi, tp.E1(xi,0.8))
plt.xscale('log')
plt.legend(['alpha 0.2','alpha 0.5','alpha 0.8'])
plt.savefig("Ea_sch�ma1.png")


xi = np.linspace(0, np.pi/8.,1000)
fig=plt.figure(3)
plt.title('Erreur d\'amplitude sch�ma 2')
plt.xlabel('xi')
plt.ylabel('E(xi)')
plt.plot(xi, tp.E2(xi,0.2))
plt.plot(xi, tp.E2(xi,0.5))
plt.plot(xi, tp.E2(xi,0.8))
plt.xscale('log')
plt.yscale('log')
plt.legend(['alpha 0.2','alpha 0.5','alpha 0.8'])
plt.savefig("Ea_sch�ma2.png")

xi = np.linspace(0, np.pi/8.,1000)
fig=plt.figure(4)
plt.title('Erreur d\'amplitude sch�ma 3')
plt.xlabel('xi')
plt.ylabel('E(xi)')
plt.plot(xi, tp.E3(xi,0.2))
plt.plot(xi, tp.E3(xi,0.5))
plt.plot(xi, tp.E3(xi,0.8))
plt.xscale('log')
plt.yscale('log')
plt.legend(['alpha 0.2','alpha 0.5','alpha 0.8'])
plt.savefig("Ea_sch�ma3.png")