# crear un diccionario cuyas llaves sean los 1000 primeros numeros 
# naturales con sus raices

import math

def run():
    my_dict2={k:math.sqrt(k) for k in range(1,1001)}
    print(my_dict2)

if __name__ == '__main__':
    run()