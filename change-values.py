import datamodel
import os

for filename in os.listdir('particles'):
    particle = datamodel.load('particles/' + filename)
    print('\n')
    print(filename)
    particleFile = open('particles/' + filename, "r+b")
    for ele in particle.find_elements(elemtype="DmeParticleSystemDefinition"):
        print('\n')
        print(ele.name)
        for operator in ele.get('operators'):
            if(operator.name == "Color Fade"):
                # white = datamodel.Color([25, 25, 25, 25])
                # print(type(operator['color_fade']))
                # data = list([0, 4, 8, 9])
                # operator['color_fade'] = datamodel.make_array([ [0.0, 0.0, 0.5, 0.5] ] , datamodel.Color)
                print(operator['color_fade'].offset)
                particleFile.seek(operator['color_fade'].offset)
                particleFile.write(bytes((255,255,255)))
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
                print(initializer['color1'].offset)
                particleFile.seek(initializer['color1'].offset)
                particleFile.write(bytes((255,255,255)))
                
                print("\ncolor2")
                print(initializer.get("color2")[0], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[1], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[2], end = '')
                
                print(initializer['color2'].offset)
                particleFile.seek(initializer['color2'].offset)
                particleFile.write(bytes((255,255,255)))
    particleFile.close()
    # particle.write('particles/' + filename, "binary", 2)
    # particle.write('particles/' + filename, "binary", 2)
