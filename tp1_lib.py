# -*- coding: cp1252 -*-
import numpy as np


def Uinit(X, J):
    Uinit = np.zeros(J)
    idX = abs(X) <= 0.25
    Uinit[idX] = 256*(X[abs(X) <= 0.25]-0.25)**2*((X[abs(X) <= 0.25]+0.25)**2)
    return Uinit


def Uinit2(X, J):
    Uinit = np.zeros(J)
    idX = abs(X) <= 0.25
    Uinit[idX] = 1.
    return Uinit


def Uinit3(X, J):
    Uinit = np.zeros(J)
    idX = abs(X) <= np.pi/4.
    Uinit[idX] = np.sin(X*np.pi*4.)/2.
    return Uinit


def schema1(U0, J, alpha):
    U1 = np.zeros(J)
    U1[1:] = U0[1:] - alpha*(U0[1:] - U0[0:-1])
    U1[0] = U0[0] - alpha*(U0[0] - U0[-2])
    return U1


def schema2(U0, J, alpha):
    U1 = np.zeros(J)
    U1[1:-1] = U0[1:-1] - alpha/2.*(U0[2:] - U0[0:-2]) + (alpha**2) / \
        2.*(U0[2:] - 2.*U0[1:-1] + U0[0:-2])
    # U1[0] = U0[0] - alpha/2.*(U0[1] - U0[-1]) + (alpha**2)/2.*(U0[1] - 2.*U0[0] + U0[-1])
    U1[0] = U0[0] - alpha/2.*(U0[1] - U0[-2]) + (alpha**2)/2.*(U0[1] - 2.*U0[0] + U0[-2])
    U1[-1] = U1[0]
    # U1[-1] = U0[-1] - alpha/2.*(U0[0] - U0[-2]) + (alpha**2)/2.*(U0[0] - 2.*U0[-1] + U0[-2])
    return U1


def schema3(U0, J, alpha):
    U1 = np.zeros(J)
    U1[2:-1] = U0[2:-1] - alpha*(U0[2:-1] - U0[1:-2]) - alpha*(1-alpha) / \
        4.*(U0[3:]-U0[2:-1]-U0[1:-2]+U0[0:-3])
    U1[0] = U0[0] - alpha*(U0[0] - U0[-2]) - alpha*(1-alpha)/4.*(U0[1]-U0[0]-U0[-2]+U0[-3])
    U1[1] = U0[1] - alpha*(U0[1] - U0[0]) - alpha*(1-alpha)/4.*(U0[2]-U0[1]-U0[0]+U0[-2])
    U1[-1] = U1[0]
    # U1[-1] = U0[-1] - alpha*(U0[-1] - U0[-2]) - alpha*(1-alpha)/4.*(U0[0]-U0[-1]-U0[-2]+U0[-3])
    return U1


def E1(xi, alpha):
    return 1 - np.sqrt(1-2*alpha*(1-alpha)*(1-np.cos(xi)))


def E2(xi, alpha):
    return 1 - np.sqrt(1-(alpha**2)*(1-alpha**2)*((1-np.cos(xi))**2))


def E3(xi, alpha):
    theta = xi/2.
    return 1-np.sqrt((1-2*alpha*(np.sin(theta)**2)*(1-(1-alpha)*(np.cos(theta)**2)))**2 + 4*(alpha**2)*(np.sin(theta)**2)*(np.cos(theta)**2)*(1+(1-alpha)*(np.sin(theta)**2))**2)
    # return 1


def Ephase1(xi, alpha):
    return alpha * xi - np.arccos((1-alpha*(1-np.cos(xi)))/(np.sqrt(1-2*alpha*(1-alpha)*(1-np.cos(xi)))))


def Ephase2(xi, alpha):
    return alpha*xi - np.arccos((1-(alpha**2)*(1-np.cos(xi)))/np.sqrt(1-(alpha**2)*(1-alpha**2)*((1-np.cos(xi))**2)))


def Ephase3(xi, alpha):
    theta = xi/2.
    p1 = 1-2*alpha*(np.sin(theta)**2)*(1-(1-alpha)*(np.cos(theta)**2))
    p2 = (1-2*alpha*(np.sin(theta)**2)*(1-(1-alpha)*(np.cos(theta)**2)))**2 + 4*(alpha**2) * \
        (np.sin(theta)**2)*(np.cos(theta)**2)*(1+(1-alpha)*(np.sin(theta)**2))**2
    # return alpha*xi - np.arccos((1-2*alpha*(np.sin(theta)**2)*(1-(1-alpha)*(np.cos(theta)**2)))/np.sqrt((1-2*alpha*(np.sin(theta)**2))))
    return alpha*xi - np.arccos(p1/np.sqrt(p2))

