# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:42:14 2020

@author: mariu
"""

import numpy as np
import math

class Quaternion:
    alpha = [0,0,0]
    angler = 0
    q0 = 0
    q = np.matrix([0,0,0])  #später q = (a, bi, by, bz) 
    qE = 0                  #Einheitsquaternion
    q_abs = 0
    qE_neg = 0
    

    
    def __init__(self, alpha_vektor, angle_degree):
    #alpha_vektor beschreibt Drehachsen mit XYZ, angle_degree beschreibt
    #den Winkel der Rotation um die Achsen
            if alpha_vektor:
                self.alpha = alpha_vektor
            else:
                print("Quaternion needs rotation axes")
            if angle_degree:   
                self.setAngle(angle_degree)
            
            self.__calcQ()
            
            
    def __calcQ(self):
            #Zuerst Q0 bestimmen mit cos(alpha/2)
            self.q0 = math.cos(self.angler/2)
            self.q0 = np.asmatrix(self.q0)
            self.q.reshape(3,1)
            #Rotationsachsen mit sin(alpha/2) multiplizieren
            self.q = np.multiply(self.alpha, math.sin(self.angler/2))
            
            #q0 an Stelle null damit sich matrix q = (a, bi, by, bz) ergibt
            self.q = np.insert(self.q, 0, self.q0,axis = 0)
        
            
            #Betrag des Quaternion
            #self.q_abs = np.linalg.norm(self.q)
            self.q_abs = np.linalg.norm(self.alpha)
            
            #Einheitsquaternion  qE = sqrt(a^2+b^2+c^2+d^2)
            self.set_qE(self.q)
            self.set_qE_neg(self.qE)
            
        
        
    def setAlpha(self, alpha_vektor):
            self.alpha = alpha_vektor
        
    def setAngle(self, angle_degree):
            self.angler = np.deg2rad(angle_degree)
        
    def get_qE(self):
        qE = np.round(self.qE, 5)
        return qE
    
    def get_q(self):
        return self.q
    
    def set_q(self, quaternion):
        self.q = quaternion
    
    #Einheitsquaternion  qE = sqrt(a^2+b^2+c^2+d^2)
    def set_qE(self, quaternion):
        self.qE = np.multiply(quaternion, 1/self.q_abs)
        self.qE[0] = self.q0
        
    def set_qE_neg(self, qE):
        self.qE_neg = np.negative(qE)
    

    def Lq(self, vector, quaternion=None):
        if quaternion:
            q = quaternion
        else:
            q = self.qE
        
        M = np.ones((3,3))
        
        M[0][0] = q[1]**2+q[0]**2-q[2]**2-q[3]**2
        M[0][1] = 2*(q[1]*q[2]-q[0]*q[3])
        M[0][2] = 2*(q[1]*q[3]+q[0]*q[2])
        
        M[1][0] = 2*(q[0]*q[3]+q[1]*q[2])
        M[1][1] = q[0]**2-q[1]**2+q[2]**2-q[3]**2
        M[1][2] = 2*(q[2]*q[3]-q[0]*q[1])
        
        M[2][0] = 2*(q[1]*q[3]-q[0]*q[2])
        M[2][1] = 2*(q[0]*q[1]+q[2]*q[3])
        M[2][2] = q[0]**2-q[1]**2-q[2]**2+q[3]**2
        
        v = vector[1:4]
        v = np.array(v)
        
        p = np.dot(v,M.T)
        return p
    
    
    def quaternion_multiplication(self, quaternion):
        
        print("qe[3] = d1 =", self.qE[3])
        print("qe2[2] = d1 =", quaternion.get_qE()[2])
        qres = np.zeros(4)
        qres[0] = self.qE[0]*quaternion.get_qE()[0]- self.qE[1]*quaternion.get_qE()[1]- self.qE[2]*quaternion.get_qE()[2]- self.qE[3]*quaternion.get_qE()[3]
        qres[1] = self.qE[0]*quaternion.get_qE()[1]+self.qE[1]*quaternion.get_qE()[0]+self.qE[2]*quaternion.get_qE()[3]-self.qE[3]*quaternion.get_qE()[2]
        qres[2] = self.qE[0]*quaternion.get_qE()[2]-self.qE[1]*quaternion.get_qE()[3]+self.qE[2]*quaternion.get_qE()[0]+self.qE[3]*quaternion.get_qE()[1]
        qres[3] = self.qE[0]*quaternion.get_qE()[3]+self.qE[1]*quaternion.get_qE()[2]-self.qE[2]*quaternion.get_qE()[1]+self.qE[3]*quaternion.get_qE()[0]
        return qres
        
    def get_Rotationsachse(self, quaternion):
        q = quaternion
        x = q[1]/(math.sqrt(1-q[0]**2))
        y = q[2]/(math.sqrt(1-q[0]**2))
        z = q[3]/(math.sqrt(1-q[0]**2))
        rot_Achse = [x,y,z]
        return rot_Achse
    
        

        