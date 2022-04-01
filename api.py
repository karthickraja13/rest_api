import flask
from flask import request,jsonify

app = flask.Flask(__name__)
datas=[{"id":0,"name":"karthickraja",},{"id":1,"name":"mohankumar"},{"id":2,"name":"prathi"}]
@app.route('/',methods=['get'])
def text():
    return jsonify({"massage":"it works"})
@app.route("/data",methods=['get'])
def get():
    return jsonify({"datas":datas})

@app.route("/data/<int:id>",methods=["GET"])
def id(id):
    return jsonify({'datas':datas[id]})

@app.route("/data",methods=["post"])
def create():
    #data={"id":request.json["id"]}
    data={
        "id":3,
        "name":"mayavan"
    }
    datas.append(data)
    return jsonify({"datas":datas})

@app.route("/data/<int:id>",methods=["put"])
def put(id):
  updata=[up for up in datas
          if up["id"] == id ]
  updata[0]["id"]=request.json["id"]
  return jsonify({"up":updata[0]})


@app.route("/data/<int:id>",methods=["delete"])
def remove(id):
    move=[up for up in datas if up["id"] == id]
    datas.remove(move[0])
    return jsonify({"datas":True})
if __name__ == '__main__':
 app.run(debug=True,port=8000)

