from flask import Flask
from flask import request,jsonify
from flask import render_template,send_from_directory
import json


app = Flask(__name__)

#list device 
#ffmpeg -list_devices true -f dshow -i dummy
#USB2.0 UVC HD Webcam
#play webcam
#ffplay -f dshow -video_size 1280x720 -i video="device name"
#push stream
#ffmpeg -f dshow -i video="USB2.0 UVC HD Webcam" -profile:v high -pix_fmt yuvj420p -level:v 4.1 -preset ultrafast -tune zerolatency -vcodec libx264 -r 10 -b:v 512k -s 640x360 -acodec aac -ac 2 -ab 32k -ar 44100 -f flv -flush_packets 0 rtmp://192.168.1.103:1935/live/test

def print_request():
    req_data = {}
    req_data['method'] = request.method
    req_data['cookies'] = request.cookies
    req_data['data'] = request.data
    req_data['headers'] = dict(request.headers)
    req_data['args'] = request.args
    req_data['form'] = request.form
    req_data['remote_addr'] = request.remote_addr
    print(str(json.dumps(req_data,default=str)))
    #return req_data

@app.after_request
def apply_caching(response):
    print_request()
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/upload',methods=['POST'])
def upload():
    print(request.files)
    for x in request.files.keys():
        print('key:',x)
        f = request.files.get(x)
        print(f.filename)
        f.save(x)
    print('len:',len(request.files))
    return jsonify({'code':200,'msg':'success'})

@app.route('/on_publish',methods=['POST'])
def on_publish():
    print('======on_publish=====')
    return jsonify({'code':10,'msg':'success'}),200,{'Content-Type':'text/plain'}
    
@app.route('/on_publish_done',methods=['POST'])
def on_publish_done():
    print('=====on_publish_done121======')
    return jsonify({'code':10,'msg':'success'}),200,{'Content-Type':'text/plain'}

@app.route('/users',methods=['GET'])
def users():
    return jsonify([
        {'id':1,'name':'aa'},
        {'id':2,'name':'bb'},
        {'id':3,'name':'cc'}
    ])

def main():
    app.run(host='0.0.0.0',port=9001,debug=True)

if __name__ == '__main__':
    main()