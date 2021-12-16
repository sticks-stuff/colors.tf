from typing import List
import datamodel
import os

print('<link rel="stylesheet" href="style.css">')

for filename in os.listdir('particles'):
    particle = datamodel.load('particles/' + filename)
    # print(filename)
    print('<div>')
    print('<h1>' + filename + '</h1>')
    particles = {}
    for ele in particle.find_elements(elemtype="DmeParticleSystemDefinition"):
        # print(ele.name)
        thisParticle = ''
        if 'red' in ele.name:
            thisParticle += '<div class="red-particle">\n'
            thisParticle += '<h2>' + ele.name + '</h2>\n'
        else:
            thisParticle += '<div class="blue-particle">\n'
            thisParticle += '<h2>' + ele.name + '</h2>\n'
            
        # print('<div>')
        # print('<h2>' + ele.name + '</h2>')
        for operator in ele.get('operators'):
            if(operator.name == "Color Fade"):
                thisParticle += '<div>'
                # print("color_fade")
                # print("operator.get("color_fade")")
                thisParticle += '<h3> color_fade </h3>\n'
                thisParticle += "<div class='colour-display' style=\"background-color: rgb("
                thisParticle += str(operator.get("color_fade")[0])
                thisParticle += ", "
                thisParticle += str(operator.get("color_fade")[1])
                thisParticle += ", "
                thisParticle += str(operator.get("color_fade")[2])
                thisParticle += ");\"></div>\n"
                thisParticle += '</div>\n'
        for initializer in ele.get('initializers'):
            if(initializer.name == "Color Random"):
                thisParticle += '<div>\n'
                # thisParticle += "color1")
                thisParticle += '<h3> color1 </h3>\n'
                # thisParticle += initializer.get("color1"))
                thisParticle += "<div class='colour-display' style=\"background-color: rgb("
                thisParticle += str(initializer.get("color1")[0])
                thisParticle += ", "
                thisParticle += str(initializer.get("color1")[1])
                thisParticle += ", "
                thisParticle += str(initializer.get("color1")[2])
                thisParticle += ");\"></div>\n"
                thisParticle += '</div>\n'
                # thisParticle += "color2")
                thisParticle += '<div>\n'
                thisParticle += '<h3> color2 </h3>\n'
                # thisParticle += initializer.get("color1"))
                thisParticle += "<div class='colour-display' style=\"background-color: rgb("
                thisParticle += str(initializer.get("color2")[0])
                thisParticle += ", "
                thisParticle += str(initializer.get("color2")[1])
                thisParticle += ", "
                thisParticle += str(initializer.get("color2")[2])
                thisParticle += ");\"></div>\n"
                thisParticle += '</div>\n'
        thisParticle += '</div>\n'
                
        if 'red' in ele.name:
            if ele.name.replace('red', 'team') not in particles:
                particles[ele.name.replace('red', 'team')] = {}
            particles[ele.name.replace('red', 'team')]['red'] = thisParticle
        else:
            if 'blu_' in ele.name or ele.name.endswith('_blu'):
                if ele.name.replace('blu', 'team') not in particles:
                    particles[ele.name.replace('blu', 'team')] = {}
                particles[ele.name.replace('blu', 'team')]['blue'] = thisParticle
            else:
                if ele.name.replace('blue', 'team') not in particles:
                    particles[ele.name.replace('blue', 'team')] = {}
                particles[ele.name.replace('blue', 'team')]['blue'] = thisParticle
    for key, value in particles.items():
        print('<div class="both-class-colours">')
        for key2, value2 in value.items():
            print(value2)
        print('</div>')
    print('</div>')
    
