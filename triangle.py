#!/usr/bin/env python3

'''
@author: stfischr
@modified: E.C.
'''

from decimal import *
import exactmath

class Triangle(object):
    
    def __init__(self):
        # private Variablen:
        self._line_a =  0
        self._line_b = 0
        self._line_c = 0
        self._line_p = 0
        self._line_q = 0
        self._line_h = 0
        self._area_A = 0
        self._angle_alpha = 0
        self._angle_beta = 0
        self.triangle_vars = [self._line_a, self._line_b, self._line_c,
                              self._line_p, self._line_q, self._line_h,
                              self._area_A, self._angle_alpha, self._angle_beta]

        self.valid_triangle = False
        

    def validation(self, triangle_vars):
        # Zählt die gegebenen Werte (0 entspricht "unbekannt")
        # Bin mir nicht sicher, ob wir das nicht besser in die API oder
        # in die jeweiligen Interfaces einbauen sollten
        self.number_of_not_0 = 0
        if 0 in self.triangle_vars:
            for i in self.triangle_vars:
                if i != 0:
                    self.number_of_not_0 += 1

        if self.number_of_not_0 == 2:
            self.valid_triangle = True
        else:
            self.valid_triangle = False
            

    def set_value(self, triangle_vars):
        # Funktion erlaubt bequem per Übergabe einer Liste das setzen der Werte
        self.triangle_vars = triangle_vars
        self.validation(dreieck.triangle_vars)

    # Hier sollten dann noch die Funktionen zum berechnen reinkommen 

    def get_value(self):
        return self.triangle_vars        
            

dreieck = Triangle()
dreieck.set_value([0, 0, 35, 0, 0, 0, 0, 0, 21])
print("Valid triangle: " + str(dreieck.valid_triangle))
print(dreieck.get_value())
