'''
Created on 25.04.2010

@author: stfischr
'''
from optparse import OptionParser
from decimal import *
import math
import os.path

def main():
    
    parser = OptionParser("usage: %prog [options]     Start interactive "
                           "mode if no Options are given")
    
    parser.set_description("This Programm is used to calculate right "
                            "triangles. The triangle has many values to be "
                            "calculated, wich are discribed as fallows:\n\n"
                            "            /|\\\n"
                            "         /_ga\\\n"
                            "        /  |  \\\n"
                            "       /   |   \\\n"
                            "      /    |    \\\n"
                            "     /    h|     \\a\n"
                            "   b/      |      \\\n"
                            "   /       |       \\\n"
                            "  /        |        \\\n"
                            " / \\      /|       / \\\n"
                            "/_al\\__p_/_|____q_/be_\\\n"
                            "            c\n"
                            "Angle Gamma is always 90°")
    
    parser.add_option("-a", "--line_a",
                      action="store", type="string", dest="line_a",
                      help="Give the value for line a in the triangle.")
    
    parser.add_option("-b", "--line_b",
                      action="store", type="string", dest="line_b",
                      help="Give the value for line b in the triangle.")
    
    parser.add_option("-c", "--line_c",
                      action="store", type="string", dest="line_c",
                      help="Give the value for line c in the triangle.")
    
    parser.add_option("-p", "--line_p",
                      action="store", type="string", dest="line_p",
                      help="Give the value for line p in the triangle.")
    
    parser.add_option("-q", "--line_q",
                      action="store", type="string", dest="line_q",
                      help="Give the value for line q in the triangle.")
    
    parser.add_option("-i", "--line_h",
                      action="store", type="string", dest="line_h",
                      help="Give the value for line h (the height) in the "
                      "triangle.")
    
    parser.add_option("-l", "--al", "--angle_alpha",
                      action="store", type="string", dest="angle_alpha",
                      help="Give the value for angle Alpha in the triangle.")
    
    parser.add_option("-t", "--be", "--angle_beta",
                      action="store", type="string", dest="angle_beta",
                      help="Give the value for angle Beta in the triangle.")
    
    #parser.add_option("-m", "--ga","--angle_gamma",
    #                  action="store", type="string", dest="angle_gamma",
    #                  help="Give the value for angle Gamma in the triangle. "
    #                  "This has currently no function because we only support "
    #                  "right triangles, therefor 90° is assumed for Gamma.")
    
    parser.add_option("-r", "--precision",
                      action="store", type="string", dest="precision",
                      help="An INTEGER describing the precision to use during "
                      "calculation and for display.", metavar="INTEGER")
    
    parser.add_option("-f", "--file",
                      action="store", type="string", dest="filename",
                      help="Write results to FILE", metavar="FILE")
    
    (options, args) = parser.parse_args()
    
    # errorhandling for precision
    if len(args) != 0:
        parser.error("Too many arguments, type \"%prog -h\" for help.")
        return 1
    else:
        opt_dic = options.__dict__

        if opt_dic['precision'] is None:
            opt_dic.pop('precision')
            precision = int("16")
        else:
            try:
                precision = int(opt_dic.pop('precision'))
            except:
                parser.error("Precision must be an integer greater than 0")
                return 1
            if precision <= 0:
                parser.error("Precision must be an integer greater than 0")
                return 1
            
    # errorhandling for filename
    opt_dic['filename'] = "/home/stfischr/colors.txt"
    if opt_dic['filename'] is None:
        filename = None
        opt_dic.pop('filename')
    elif len(str(opt_dic['filename'])) > 0:
        filename = str(opt_dic.pop('filename'))
        try:
            print("hrr")
            if not os.path.isfile(filename):
                if not os.path.exists(filename): #hier muss noch auf den
                                    #Verzeichnisnamen beschnitten werden
                    parser.error("Bad filename")
                    return 1
                #Verzeichnis existiert aber Datei muss angelegt werden
            parser.error("Bad filename")
        except:
            print("uh?")
    else:
        parser.error("Bad filename")
        return 1

    # sicherstellen, dass min 2 Werte übergeben werden    
    not_none_count = 0
    for val in opt_dic.values():
        if val is not None:
            not_none_count += 1
    # wenn in options alle None sind, interaktive Console aufrufen
   
    
    
    #hier die Klasse instanzieren und die Werte übergeben, auf Rückgabe
    #warten und dann ergebnise anzeigen oder Fehlermeldung.
    #print(options)


if __name__ == "__main__":
    main()
