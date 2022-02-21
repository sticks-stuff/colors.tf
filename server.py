import json_to_color_patch
import patch_vmts
from flask import Flask, request, send_file, after_this_request
from flask_cors import CORS
import shutil
import time
import vpk
import os
import io
from multiprocessing import Process
import glob

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/generate', methods=['POST'])
@cross_origin()
def generate():
    if request.method == 'POST':
        requestTime = str(int(time.time()))
        data = request.get_json()
        # shutil.rmtree("work/", ignore_errors=True)
        shutil.copytree("materials/", "work/" + requestTime + "/materials/")
        shutil.copytree("template/particles", "work/" + requestTime + "/particles/")

        # print('Data Received: "{data}"'.format(data=data))
        print("New request: " + requestTime);
        red_crit = data['material']['red_crit']['color']
        red_minicrit = data['material']['red_minicrit']['color']
        blue_crit = data['material']['blue_crit']['color']
        blue_minicrit = data['material']['blue_minicrit']['color']
        patch_vmts.patchVMTs(blue_crit, red_crit, red_minicrit, blue_minicrit, "work/" + requestTime + "/materials/")
        print("Patched vmts!");
        
        del data['material'] #clean up the stuff thats only for vmfs
        #hacky i know
        json_to_color_patch.patchPCFWithJson(data, "work/" + requestTime + "/particles/")
        print("Patched particles!");
        
        newpak = vpk.new("work/" + requestTime)
        newpak.save("colors.tf_" + requestTime + ".vpk")
        print("Packed files!");

        filename = "colors.tf_" + requestTime + ".vpk"
        
        
        return_data = io.BytesIO() #all this shit is literally just to remove the vpk after its sent
        with open(filename, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)    

        background_remove(filename) #see above
        
        shutil.rmtree("work/" + requestTime, ignore_errors=True) #clean up the directory we made too
    
        return send_file(return_data, as_attachment=True, attachment_filename=filename)

def background_remove(path):
    task = Process(target=rm(path))
    task.start()

    
def rm(path):
    os.remove(path)

if __name__ == "__main__":
#   app.run(port=3000)
  # if you need to make it live debuging add 'debug=True'
#   app.run(port=3000, debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
