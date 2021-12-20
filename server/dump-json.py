import datamodel
import os
import json

data = {}

for filename in os.listdir('template/particles'):
    particle = datamodel.load('template/particles/' + filename)
    print('\n')
    print(filename)
    particleFile = open('template/particles/' + filename, "r+b")
    data[filename] = {}
    for ele in particle.find_elements(elemtype="DmeParticleSystemDefinition"):
        print('\n')
        print(ele.name)
        for operator in ele.get('operators'):
            if(operator.name == "Color Fade"):
                if ele.name not in data[filename]:
                        data[filename][ele.name] = {}
                print("color_fade")                
                data[filename][ele.name]['color_fade'] = operator.get("color_fade")
                
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
                
                data[filename][ele.name]['color1'] = initializer.get("color1")

                print(initializer.get("color1")[0], end = '')
                print(", ", end = '')
                print(initializer.get("color1")[1], end = '')
                print(", ", end = '')
                print(initializer.get("color1")[2])
                
                print("color2")
                                
                data[filename][ele.name]['color2'] = initializer.get("color2")

                print(initializer.get("color2")[0], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[1], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[2])
                
    particleFile.close()
    
with open('../_data/colors.json', 'w') as outfile:
    json.dump(data, outfile)