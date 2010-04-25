#!/usr/bin/env python3.1
'''
@author: stfischr
@modified: E.C.
'''

from decimal import *

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
        self.pi = Decimal(str('''3.1415926535897932384626433832
                          795028841971693993751058209749
                          445923078164062862089986280348
                          253421170679821480865132823066
                          470938446095505822317253594081
                          284811174502841027019385211055
                          596446229489549303819644288109
                          756659334461284756482337867831
                          652712019091456485669234603486
                          104543266482133936072602491412
                          737245870066063155881748815209
                          209628292540917153643678925903
                          600113305305488204665213841469
                          519415116094330572703657595919
                          530921861173819326117931051185
                          480744623799627495673518857527
                          248912279381830119491298336733
                          624406566430860213949463952247
                          371907021798609437027705392171
                          762931767523846748184676694051
                          320005681271452635608277857713
                          427577896091736371787214684409
                          012249534301465495853710507922
                          796892589235420199561121290219
                          608640344181598136297747713099
                          605187072113499999983729780499
                          510597317328160963185950244594
                          553469083026425223082533446850
                          352619311881710100031378387528
                          865875332083814206171776691473
                          035982534904287554687311595628
                          638823537875937519577818577805
                          321712268066130019278766111959
                          092164201989380952572010654858
                          632788659361533818279682303019
                          520353018529689957736225994138
                          912497217752834791315155748572
                          424541506959508295331168617278
                          558890750983817546374649393192
                          550604009277016711390098488240
                          128583616035637076601047101819
                          429555961989467678374494482553
                          797747268471040475346462080466
                          842590694912933136770289891521
                          047521620569660240580381501935
                          112533824300355876402474964732
                          639141992726042699227967823547
                          816360093417216412199245863150
                          302861829745557067498385054945
                          8858692699569092721079750930296'''
                              ).replace("\n", "").replace(" ",""))
        

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
