import datamodel
import os
import json

data = {}

for filename in os.listdir('particles'):
    particle = datamodel.load('particles/' + filename)
    print('\n')
    print(filename)
    particleFile = open('particles/' + filename, "r+b")
    data[filename] = {}
    for ele in particle.find_elements(elemtype="DmeParticleSystemDefinition"):
        print('\n')
        print(ele.name)
        for operator in ele.get('operators'):
            if(operator.name == "Color Fade"):
                if ele.name not in data[filename]:
                        data[filename][ele.name] = {}
                print("color_fade")
                print(operator['color_fade'].offset)
                particleFile.seek(operator['color_fade'].offset)
                particleFile.write(bytes((255,255,255)))
                
                data[filename][ele.name]['color_fade'] = "255 255 255"
                
                print(operator.get("color_fade")[0], end = '')
                print(", ", end = '')
                print(operator.get("color_fade")[1], end = '')
                print(", ", end = '')
                print(operator.get("color_fade")[2])
                
        for initializer in ele.get('initializers'):
            if(initializer.name == "Color Random"):
                if ele.name not in data[filename]:
                    data[filename][ele.name] = {}
                print("color1")
                print(initializer['color1'].offset)
                particleFile.seek(initializer['color1'].offset)
                particleFile.write(bytes((255,255,255)))
                
                data[filename][ele.name]['color1'] = "255 255 255"

                print(initializer.get("color1")[0], end = '')
                print(", ", end = '')
                print(initializer.get("color1")[1], end = '')
                print(", ", end = '')
                print(initializer.get("color1")[2])
                
                print("color2")
                print(initializer['color2'].offset)
                particleFile.seek(initializer['color2'].offset)
                particleFile.write(bytes((255,255,255)))
                
                data[filename][ele.name]['color2'] = "255 255 255"

                print(initializer.get("color2")[0], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[1], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[2])
                
    particleFile.close()
    # particle.write('particles/' + filename, "binary", 2)
    # particle.write('particles/' + filename, "binary", 2)
    
with open('output.json', 'w') as outfile:
    json.dump(data, outfile)