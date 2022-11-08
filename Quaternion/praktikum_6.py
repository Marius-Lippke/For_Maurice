# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:18:35 2020

@author: marius
"""
import numpy as np

from quaternion_class import Quaternion


#Aufgabe 1.11:    
alpha = [1, 1, 0]
angled = 90
vector = [0, 2, 9, 14]

quaternion = Quaternion(alpha, angled)
print("\nAufgabe 1.11")
print("Quaternion: ", quaternion.get_qE())
print("Rotation aus: ", vector, " in r: ", quaternion.Lq(vector))

#Aufgabe 1.7:    
alpha = [1.0, 0.0, 0.0]
angled = 90
vector = [0, 8, 2, 1]
quaternion = Quaternion(alpha, angled)
print("\nAufgabe 1.7")
print("Quaternion: ", quaternion.get_qE())
print("Rotation aus: ", vector, " in r: ", quaternion.Lq(vector))

#Aufgabe 1.8:    
alpha = [1.0, 0.0, 0.0]
angled = 90
vector = [0, 6, 4, 3]
quaternion = Quaternion(alpha, angled)
print("\nAufgabe 1.8")
print("Quaternion: ", quaternion.get_qE())
print("Rotation aus: ", vector, " in r: ", quaternion.Lq(vector))


#Aufgabe 1.9:    
alpha = [0.0, 1.0, 0.0]
angled = 90
vector = [0, 12, 10, 4]
quaternion = Quaternion(alpha, angled)
print("\nAufgabe 1.9")
print("Quaternion: ", quaternion.get_qE())
print("Rotation aus: ", vector, " in r: ", quaternion.Lq(vector))


#Aufgabe 1.13:    
alpha = [1.0, 1.0, 1.0]
angled = 45
vector = [0, 20, 13, 7]
quaternion = Quaternion(alpha, angled)
print("\nAufgabe 1.14")
print("Quaternion: ", quaternion.get_qE())
print("Rotation aus: ", vector, " in r: ", quaternion.Lq(vector))

#Aufgabe 1.29:
alpha1 = [1.0, 1.0, 0.0]
angled1 = 45
quaternion1 = Quaternion(alpha1, angled1)

alpha2 = [1.0, 1.0, 1.0]
angled2 = 15
quaternion2 = Quaternion(alpha2, angled2)

print("\nquaternion 1: ", quaternion1.get_qE())
print("quaternion 2: ", quaternion2.get_qE())
qE_res = quaternion1.quaternion_multiplication(quaternion2)
print("resultierendes Einheitsquaternion:\t", qE_res)
rot_Achse_res = quaternion1.get_Rotationsachse(qE_res)
print("resultierende Rotationsachse:\t", rot_Achse_res)

#Aufgabe 1.29:
vector = [0, 1, 0, 0]
alpha1 = [0.0, 0.0, 1.0]
angled1 = 90
quaternion1 = Quaternion(alpha1, angled1)

alpha2 = [0.0, 1.0, 1.0]
angled2 = 90
quaternion2 = Quaternion(alpha2, angled2)

print("\nquaternion 1: ", quaternion1.get_qE())
print("quaternion 2: ", quaternion2.get_qE())
qE_res = quaternion1.quaternion_multiplication(quaternion2)
print("resultierendes Einheitsquaternion:\t", qE_res)
rot_Achse_res = quaternion1.get_Rotationsachse(qE_res)
print("resultierende Rotationsachse:\t", rot_Achse_res)

