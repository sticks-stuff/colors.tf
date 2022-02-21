from typing import List
import datamodel
import os

f = open("intro.html", "r")
print(f.read())
f.close()

for filename in os.listdir('template/particles'):
    if filename == 'particles_manifest.txt': #hardcoding shit fuck you
        continue;
    particle = datamodel.load('template/particles/' + filename)
    # print('<div>')
    print('<div class="collapsible layer1">')
    # print('<h1>' + filename + '</h1>')
    print('<button type="button">' + filename + '</button>')
    print('<div class="content">')
    particles = {}
    for ele in particle.find_elements(elemtype="DmeParticleSystemDefinition"):
        # print(ele.name)
        thisParticle = ''
            
        # print('<div>')
        # print('<h2>' + ele.name + '</h2>')
        for operator in ele.get('operators'):
            if(operator.name == "Color Fade"):
                thisParticle += '<div>'
                # print("color_fade")
                # print("operator.get("color_fade")")
                thisParticle += '<h3> color_fade </h3>\n'
                ogcolor = str(operator.get('color_fade'))
                thisParticle += f"<div class='colour-display' jsonpath='{filename},{ele.name},color_fade' ogcolour='{ogcolor}' style=\"background-color: rgb("
                thisParticle += str(operator.get("color_fade")[0])
                thisParticle += ", "
                thisParticle += str(operator.get("color_fade")[1])
                thisParticle += ", "
                thisParticle += str(operator.get("color_fade")[2])
                thisParticle += ");\"></div>\n"
                thisParticle += '</div>\n'
        for initializer in ele.get('initializers'):
            # i love violating "dont repeat yourself"
            if(initializer.name == "Color Random"):
                thisParticle += '<div>\n'
                # thisParticle += "color1")
                thisParticle += '<h3> color1 </h3>\n'
                # thisParticle += initializer.get("color1"))
                ogcolor = str(initializer.get('color1'))
                thisParticle += f"<div class='colour-display' jsonpath='{filename},{ele.name},color1' ogcolour='{ogcolor}' style=\"background-color: rgb("
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
                ogcolor = str(initializer.get('color2'))
                thisParticle += f"<div class='colour-display' jsonpath='{filename},{ele.name},color2' ogcolour='{ogcolor}' style=\"background-color: rgb("
                thisParticle += str(initializer.get("color2")[0])
                thisParticle += ", "
                thisParticle += str(initializer.get("color2")[1])
                thisParticle += ", "
                thisParticle += str(initializer.get("color2")[2])
                thisParticle += ");\"></div>\n"
                thisParticle += '</div>\n'
        if len(thisParticle) < 1:
            continue
        thisParticle += '</div>\n'
                
        if 'red' in ele.name:
            # thisParticle = '<h2>' + ele.name + '</h2>\n' + thisParticle 
            thisParticle = '<div class="red-particle">\n' + thisParticle
            thisParticle = '<button type="button">' + ele.name.replace('red', '').replace('__', '_') + '</button>' + '\n<div class="content">' + thisParticle 
            # this sucks but we used to do it at the creation of the string
            # which made more sense but then we cant check if nothing usefuls been added
            if ele.name.replace('red', 'team') not in particles:
                particles[ele.name.replace('red', 'team')] = {}
            particles[ele.name.replace('red', 'team')]['red'] = thisParticle
        else:
            # thisParticle = '<h2>' + ele.name + '</h2>\n' + thisParticle
            thisParticle = '<div class="blue-particle">\n' + thisParticle
            if 'blu_' in ele.name or ele.name.endswith('_blu'):
                #awful hack because sometimes its 'blue' and sometimes its 'blu'
                if ele.name.replace('blu', 'team') not in particles:
                    particles[ele.name.replace('blu', 'team')] = {}
                particles[ele.name.replace('blu', 'team')]['blue'] = thisParticle
            else:
                if ele.name.replace('blue', 'team') not in particles:
                    particles[ele.name.replace('blue', 'team')] = {}
                particles[ele.name.replace('blue', 'team')]['blue'] = thisParticle
    for key, value in particles.items():
        if len(value.items()) > 1: #exclude objects that dont have team colours
            # print('<div class="both-class-colours">')
            print('<div class="collapsible layer2">')
            print(value['red'])
            print(value['blue'])
            print('</div>')
            print('</div>')
    print('</div>')
    print('</div>')
    
f = open("outro.html", "r")
print(f.read())
f.close()