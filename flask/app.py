from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from elasticsearch import Elasticsearch

app = Flask(__name__)
CORS(app)

@app.route("/performQuery", methods = ["POST"])
def performQuery():
    # get post data
    m = request.get_json()
    x = json.dumps(m)
    y = json.loads(x)
    searchtarg = str((y["query"]["srch"]))
    # gets query results from elasticsearch
    indexName = "bindex"
    elastic_pass ="erYIt3NyBuJ44T6GczZP70c5"
    endpoint = "i-o-optimized-deployment-4ac6a9.es.us-west1.gcp.cloud.es.io:9243"
    connectionString = "https://elastic:" + elastic_pass + "@" + endpoint
    esConn = Elasticsearch(connectionString)
    # get top 10 results from query, sorted by greatest to least
    response = esConn.search(index=indexName, body={"query": {"match_phrase": {"html": searchtarg}}}, sort={'_score: {"order": "desc, "mode": "max"'}) 
    data = []

    for i, j in response['hits'].items():
        if i == 'hits':
            # j is a list of the query results, size = 10 max
            for scores in j:
                temp = []
                k = scores['_source']
                temp.append(scores['_score'])
                for key, value in k.items():
                    if key != 'html':
                        temp.append(value)
                data.append(temp)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)