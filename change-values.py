import datamodel
import os

for filename in os.listdir('particles'):
    particle = datamodel.load('particles/' + filename)
    print(filename)
    for ele in particle.find_elements(elemtype="DmeParticleSystemDefinition"):
        print('\n')
        print(ele.name)
        for operator in ele.get('operators'):
            if(operator.name == "Color Fade"):
                print("\ncolor_fade")
                print(operator.get("color_fade")[0], end = '')
                print(", ", end = '')
                print(operator.get("color_fade")[1], end = '')
                print(", ", end = '')
                print(operator.get("color_fade")[2], end = '')
        for initializer in ele.get('initializers'):
            if(initializer.name == "Color Random"):
                print("\ncolor1")
                print(initializer.get("color1")[0], end = '')
                print(", ", end = '')
                print(initializer.get("color1")[1], end = '')
                print(", ", end = '')
                print(initializer.get("color1")[2], end = '')
                print("\ncolor2")
                print(initializer.get("color2")[0], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[1], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[2], end = '')
