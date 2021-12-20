import json_to_color_patch
import patch_vmts
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
	
        data = request.get_json()

        print('Data Received: "{data}"'.format(data=data))
        return "Request Processed.\n"

if __name__ == "__main__":
#   app.run(port=3000)
  # if you need to make it live debuging add 'debug=True'
  app.run(port=3000, debug=True)
