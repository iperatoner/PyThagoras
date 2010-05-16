#!/usr/bin/env python3

import math


class Triangle(object):
    
    def __init__(self):
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
        self.exact_triangle = True
        

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
        elif self.triangle_vars[-1] != 0 and self.triangle_vars[-2] != 0:
            self.valid_triangle = False
        else:
            self.valid_triangle = False
            

    def set_value(self, triangle_vars):
        # Funktion erlaubt bequem per Übergabe einer Liste das Setzen der Werte
        self.triangle_vars = triangle_vars
        self.validation(dreieck.triangle_vars)

 

    def get_value(self):
        return self.triangle_vars, self.exact_triangle

    def calc_a(self):
        if self._line_a == 0:
            if self._line_b != 0 and self._line_c != 0:
                a = (self._line_c**2 - self._line_b**2).sqrt()

            elif self._line_b != 0 and self._angle_beta != 0:
                a = self._line_b/math.tan(self._angle_beta)
                
            elif self._line_c != 0 and self._line_p != 0:
                a = math.sqrt(self._line_c * self._line_p)

            elif self._line_c != 0 and self._angle_alpha != 0:
                a = math.sin(self._angle_alpha) * self._line_c

            elif self._line_h != 0 and self._angle_beta != 0:
                a = self._line_h/math.sin(self._angle_beta)

            elif self._line_b != 0 and self._angle_alpha != 0:
                a = b*math.tan(self._angle_alpha)

            elif self._line_c != 0 and self._angle_beta != 0:
                a = c*math.cos(self._angle_beta)

            elif self._line_p != 0 and self._angle_beta != 0:
                a = self._line_p/math.cos(self._angle_beta)

            elif self._line_h != 0 and self._angle_beta != 0:
                a = self._line_h / math.sin(self._angle_beta)

            elif self._area_A != 0 and self._line_b != 0:
                a = self._area_A/(0.5*self._line_b)

            elif self._line_p != 0 and self._line_h != 0:
                a = math.sqrt(self._line_p**2 + self._line_h**2)

            self._line_a = a

        return self._line_a

    def calc_b(self):
        if self._line_b == 0:
            if self._line_a != 0 and self._line_c != 0:
                b = math.sqrt(self._line_c**2 - self._line_a**2)

            elif self._line_a != 0 and self._area_A != 0:
                b = self._area_A/(0.5*self._line_a)

            elif self._line_c != 0 and self._angle_alpha != 0:
                b = math.cos(self._angle_alpha) * self._line_c

            elif self._line_a != 0 and self._angle_beta != 0:
                b = self._line_a/math.tan(self._angle_beta)
            
            elif self._line_a != 0 and self._angle_beta != 0:
                b = math.tan(self._angle_beta) * self._line_a

            elif self._line_c != 0 and self._angle_beta != 0:
                b = self._line_c * math.sin(self._angle_beta)

            elif self._line_h != 0 and self._line_q != 0:
                b = math.sqrt(self._line_h**2 - self._line_q**2)

            elif self._line_q != 0 and self._angle_alpha != 0:
                b = self._line_q / math.cos(self._angle_alpha)

            elif self._line_h != 0 and self._angle_alpha != 0:
                b = self._line_h / math.sin(self._angle_alpha)

            self._line_b = b

        return self._line_a


    def calc_c(self):
        if self._line_c == 0:
            if self._line_a != 0 and self._line_b != 0:   
                c = math.sqrt(self._line_a**2 + self._line_b**2)
                
            elif self._line_h != 0 and self._area_A != 0:
                c = self._area_A*2 / self._line_h
                
            elif self._line_p != 0 and self._line_q != 0:
                c = self._line_p + self._line_q

            elif self._line_a != 0 and self._angle_alpha != 0:
                c = self._line_a / math.sin(self._angle_alpha)

            elif self._line_b != 0 and self._angle_beta != 0:
                c = self._line_b / math.sin(self._angle_beta)

            elif self._line_b != 0 and self._angle_alpha != 0:
                c = self._line_b / math.cos(self._angle_alpha)

            elif self._line_a != 0 and self._angle_beta != 0:
                c = self._line_a / math.cos(self._angle_beta)

            elif self._line_p != 0 and self._line_b != 0:
                c = ((math.sqrt(4*self._line_b**2+p**2))+p)/2

            elif self._line_q != 0 and self._line_q != 0:
                c = ((math.sqrt(4*self._line_a**2+q**2))+q)/2

            self._line_c = c

        return self._line_c

    def calc_p(self):
        if self._line_p == 0:
            if self._line_a != 0 and self._line_q != 0:   
                p = ((math.sqrt(4*(a**2)+q**2))-q)/2
                
            elif self._line_h != 0 and self._line_a != 0:
                p = math.sqrt(a**2-h**2)
                
            elif self._line_c != 0 and self._line_q != 0:
                p = self._line_h**2/self._line_q

            elif self._line_q != 0 and self._area_A != 0:
                p = ((-6*math.sqrt(3)*self._area_A*
                      math.sqrt(27*self._area_A**2+self._line_q**4)+
                      54*self._area_A**2+self._line_q**4)**(1/3)+
                     (6*math.sqrt(3)*self._area_A*
                      math.sqrt(27*self._area_A**2+self._line_q**4)+
                      54*self._area_A**2+self._line_q**4)**(1/3)-2*
                     self._line_q**(4/3))/(3*self._line_q**(1/3))
                
            elif self._line_h != 0 and self._angle_beta != 0:
                p = self._line_h/math.sin(self._angle_beta)

            elif self._line_h != 0 and self._area_A != 0:
                p = 2*self._area_A/self._line_h
                
            self._line_p = p
            
        return self._line_p

    def calc_q(self):
        if self._line_q == 0:
            if self._line_b != 0 and self._line_p != 0:   
                q = ((math.sqrt(4*(b**2)+p**2))-p)/2
                
            elif self._line_h != 0 and self._line_b != 0:
                q = math.sqrt(b**2-h**2)

            elif self._line_c != 0 and self._line_p != 0:
                q = self._line_h**2/self._line_p

            elif self._line_p != 0 and self._area_A != 0:
                q = ((-6*math.sqrt(3)*self._area_A*
                      math.sqrt(27*self._area_A**2+self._line_p**4)+
                      54*self._area_A**2+self._line_p**4)**(1/3)+
                     (6*math.sqrt(3)*self._area_A*
                      math.sqrt(27*self._area_A**2+self._line_p**4)+
                      54*self._area_A**2+self._line_p**4)**(1/3)-2*
                     self._line_p**(4/3))/(3*self._line_p**(1/3))

            elif self._line_h != 0 and self._angle_alpha != 0:
                q = self._line_h/math.sin(self._angle_alpha)

            elif self._line_h != 0 and self._area_A != 0:
                q = 2*self._area_A/self._line_h

            self._line_q = q
            
        return self._line_q

    def calc_h(self):
        if self._line_h == 0:
            if self._line a != 0 and self._line_ p != 0:
                h = math.sqrt(a**2-p**2)

            elif self._line_b != 0 and self._line_q != 0:
                h = math.sqrt(b**2-q**2)

            elif self._line_c != 0 and self._area_A != 0:
                h = (2*self._area_A)/self._line_c

            elif self._line_p != 0 and self._line_q != 0:
                h = math.sqrt(self._line_p*self._line_q)

            elif self._line_p != 0 and self._angle_beta != 0:
                h = self._line_p*math.cos(self._angle_beta)

            elif self._line_q != 0 and self._angle_alpha != 0:
                h = self._line_q*math.cos(self._angle_alpha)

            self._line_h = h
            
        return self._line_h

    def clac_A(self):
        if self._area_A == 0:
            if self._line_a != 0 and self._line_b != 0:
                A = 0.5*(self._line_a*self._line_b)

            if self._line_c != 0 and self._line_h != 0:
                A = 0.5*(self._line_c*self._line_h)

            self._area_A = A

        return self._area_A
    
    def calc_alpha(self):
        if self._angle_alpha == 0:
            if self._angle_beta != 0:
                alpha = (90 - self._angle_beta)

            elif self._line_a != 0 and self._line_c != 0:
                alpha = math.asin(self._line_a / self._line_c)

            elif self._line_h != 0 and self._line_b != 0:
                alpha = math.asin(self._line_h / self._line_b)

            self._angle_alpha = alpha

        return self._angle_alpha

    def calc_beta(self):
        if self._angle_beta == 0:
            if self._angle_alpha != 0:
                alpha = (90 - self._angle_alpha)

            elif self._line_a != 0 and self._line_c != 0:
                beta = math.asin(self._line_b / self._line_c)

            elif self._line_h != 0 and self._line_a != 0:
                beta = math.asin(self._line_h / self._line_a)

            self._angle_beta = beta

        return self._angle_beta
        

dreieck = Triangle()
dreieck.set_value([0, 0, 0, 0, 3, 0, 8, 0, 0])
print("Valid triangle: " + str(dreieck.valid_triangle))
print(dreieck.get_value())

