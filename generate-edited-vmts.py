import os
import shutil
import re

# shutil.copytree("materials/", "work/materials")

f = open("material-template/template.vmt", "r")
template = f.readlines()
f.close()

template.insert(0, '    "$bluCritGlow" "[0 0 255]"\n')
template.insert(0, '	"$redCritGlow" "[255 0 0]"\n')
template.insert(0, '	"$redMiniCritGlow" "[255 120 120]"\n')
template.insert(0, '"$bluMiniCritGlow" "[120 120 255]"\n')

for root, dirs, files in os.walk("work/materials"):
    for file in files:
        if file.endswith(".vmt"):
            with open(os.path.join(root, file), 'r') as f:
                filedata = f.read()
                
                filedata = re.sub('\"ModelGlowColor((.|\n)*?)\}', '', filedata)
                filedata = filedata.replace('"Proxies"\n	{', ''.join(template))
                filedata = re.sub('"\$glowcolor".*\"*"', '"$glowcolor" "[1 1 1]"', filedata)
                
            with open(os.path.join(root, file), 'w') as f:
                f.write(filedata)