import datamodel



import os
for filename in os.listdir('particles'):
	particle = datamodel.load('particles/' + filename)
	print(filename)
	for ele in particle.find_elements(elemtype="DmeParticleSystemDefinition"):
		print(ele.name)
		# print(ele.items)
		# print(dir(ele.items))
		for operator in ele.get('operators'):
			if(operator.name == "Color Fade"):
					print("color_fade")
					print(operator.get("color_fade"))
		for initializer in ele.get('initializers'):
			if(initializer.name == "Color Random"):
				print("color1")
				print(initializer.get("color1"))
				print("color2")
				print(initializer.get("color2"))
