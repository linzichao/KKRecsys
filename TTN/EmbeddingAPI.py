import numpy as np
from datetime import datetime
from tqdm import tqdm
import os
from flask import request
from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/query": {"origins": "*"}})

@app.route("/query")
# query one song
def query():
    print("making query")
    dict = []
    t1 = datetime.now()
    query = request.args.get('name')
    print(query)
    num_candidate = 10
    index_q = querylist.index(query)
    score = np.dot(pretrain_model[index_q], pretrain_model.T)
    candidate = np.argsort(score)[-(num_candidate+1):-1][::-1]
    t2 = datetime.now()
    #print("query time: " + str(t2-t1))
    #print("top 10 related with " + query)
    for index in candidate:
        dict.append(querylist[index])
        #print(querylist[index] + ' ' + str(score[index]))

    result = jsonify(dict)
    return result

if __name__ == "__main__":

    In = open("ICN_song.embd")

    pretrain_model = np.zeros((9995,64))
    querylist = []
    index_line = 0

    print("building embedding matrix")
    for line in tqdm(In):
        embd_vector = line.split(" ")
        querylist.append(embd_vector.pop(0))
        pretrain_model[index_line] = embd_vector
        index_line += 1

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
