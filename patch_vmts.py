import os
import re

def patchVMTs(bluCritColor, redCritColor, redMiniCritColor, bluMiniCritColor, directory):
    f = open("template/materials/template.vmt", "r")
    template = f.readlines()
    f.close()

    template.insert(0, f'    "$bluCritGlow" "[{bluCritColor[0]} {bluCritColor[1]} {bluCritColor[2]}]"\n')
    template.insert(0, f'	"$redCritGlow" "[{redCritColor[0]} {redCritColor[1]} {redCritColor[2]}]"\n')
    template.insert(0, f'	"$redMiniCritGlow" "[{redMiniCritColor[0]} {redMiniCritColor[1]} {redMiniCritColor[2]}]"\n')
    template.insert(0, f'"$bluMiniCritGlow" "[{bluMiniCritColor[0]} {bluMiniCritColor[1]} {bluMiniCritColor[2]}]"\n')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".vmt"):
                with open(os.path.join(root, file), 'r') as f:
                    filedata = f.read()
                    
                    filedata = re.sub('\"ModelGlowColor((.|\n)*?)\}', '', filedata)
                    filedata = filedata.replace('"Proxies"\n	{', ''.join(template))
                    filedata = re.sub('"\$glowcolor".*\"*"', '"$glowcolor" "[1 1 1]"', filedata)
                    
                with open(os.path.join(root, file), 'w') as f:
                    f.write(filedata)