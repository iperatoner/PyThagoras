#!/usr/bin/env python3.1

'''Because there are vey similiar var-names in this module, here's a short
explanation:
var_list: Contains the names of the vars that can be given by the user
given_vars: Contains the names of the given vars (e.g. ['a', 'alpha'])
given_values: Contains the values of the given vars (e.g. ['3', '25'])
get_values: Contains the names of the vars given by the user
given_value_names: Same like get_values, without commas and spaces
value_name: One single 'value_name' of all 'given_value_names'
default_value: Contains the name of the var which value is now asked by the user
known_values: List with all given vars and values(e.g.['a', '3', 'alpha', '25'])

var: var is needed for creating the ->
final_list: which is committed to class 'triangle'
'''

var_list = ['a', 'b', 'c', 'p', 'q', 'h', 'A', 'alpha', 'beta']
def main():
    given_vars = [] # List with given Vars
    given_values = [] # List with given values
    get_values = input("Was ist gegeben? (Trennung erfolgt durch Kommata): ")
    given_value_names = get_values.replace(' ','').split(',') 
    for value_name in given_value_names:
        if value_name in var_list:
            given_vars.append(value_name) 

                
    for default_value in given_vars:
        given_values.append(input("Wert von %s: " %(default_value)))

    known_values = list(zip(given_vars,given_values))
    final_values = []
    for var in var_list:
        if var in known_values[0]:
            final_values.append(known_values[0][1])
        elif var in known_values[1]:
            final_values.append(known_values[1][1])
        else:
            final_values.append(0)


if __name__ == '__main__':
    main()
