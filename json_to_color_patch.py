import datamodel

def patchPCFWithJson(data, directory):
    for filename in data:
        particle = datamodel.load(directory + filename)
        # print('\n')
        # print(filename)
        particleFile = open(directory + filename, "r+b")

        for ele in particle.find_elements(elemtype="DmeParticleSystemDefinition"):
            if ele.name in data[filename]:
                # print('\n')
                # print(ele.name)
                if 'color_fade' in data[filename][ele.name]:
                    for operator in ele.get('operators'):
                        if(operator.name == "Color Fade"):
                            
                            # print("color_fade")
                            # print(operator['color_fade'].offset)
                            particleFile.seek(operator['color_fade'].offset)
                            for i in data[filename][ele.name]['color_fade']:
                                particleFile.write(bytes((int(i),)))
                            
                            # print(operator.get("color_fade")[0], end = '')
                            # print(", ", end = '')
                            # print(operator.get("color_fade")[1], end = '')
                            # print(", ", end = '')
                            # print(operator.get("color_fade")[2])
                            
                if 'color1' in data[filename][ele.name]:
                    for initializer in ele.get('initializers'):
                        if(initializer.name == "Color Random"):

                            # print("color1")
                            # print(initializer['color1'].offset)
                            particleFile.seek(initializer['color1'].offset)
                            for i in data[filename][ele.name]['color1']:
                                particleFile.write(bytes((int(i),)))
                            
                            # print(initializer.get("color1")[0], end = '')
                            # print(", ", end = '')
                            # print(initializer.get("color1")[1], end = '')
                            # print(", ", end = '')
                            # print(initializer.get("color1")[2])
                            
                            # print("color2")
                            print(initializer['color2'].offset)
                            particleFile.seek(initializer['color2'].offset)
                            for i in data[filename][ele.name]['color2']:
                                particleFile.write(bytes((int(i),)))
                            
                            # print(initializer.get("color2")[0], end = '')
                            # print(", ", end = '')
                            # print(initializer.get("color2")[1], end = '')
                            # print(", ", end = '')
                            # print(initializer.get("color2")[2])
                    
        particleFile.close()