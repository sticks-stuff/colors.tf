import datamodel
import os

print('<link rel="stylesheet" href="style.css">')

for filename in os.listdir('particles'):
    particle = datamodel.load('particles/' + filename)
    # print(filename)
    print('<h1>' + filename + '</h1>')
    for ele in particle.find_elements(elemtype="DmeParticleSystemDefinition"):
        # print(ele.name)
        print('<h2>' + ele.name + '</h2>')
        for operator in ele.get('operators'):
            if(operator.name == "Color Fade"):
                # print("color_fade")
                # print("operator.get("color_fade")")
                print('<h3> color_fade </h3>')
                print("<div style=\"background-color: rgb(", end = '')
                print(operator.get("color_fade")[0], end = '')
                print(", ", end = '')
                print(operator.get("color_fade")[1], end = '')
                print(", ", end = '')
                print(operator.get("color_fade")[2], end = '')
                print(");\"></div>")
        for initializer in ele.get('initializers'):
            if(initializer.name == "Color Random"):
                # print("color1")
                print('<h3> color1 </h3>')
                # print(initializer.get("color1"))
                print("<div style=\"background-color: rgb(", end = '')
                print(initializer.get("color1")[0], end = '')
                print(", ", end = '')
                print(initializer.get("color1")[1], end = '')
                print(", ", end = '')
                print(initializer.get("color1")[2], end = '')
                print(");\"></div>")
                # print("color2")
                print('<h3> color2 </h3>')
                # print(initializer.get("color1"))
                print("<div style=\"background-color: rgb(", end = '')
                print(initializer.get("color2")[0], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[1], end = '')
                print(", ", end = '')
                print(initializer.get("color2")[2], end = '')
                print(");\"></div>")
