#!/bin/sh
password="erYIt3NyBuJ44T6GczZP70c5"
endpoint="https://i-o-optimized-deployment-4ac6a9.es.us-west1.gcp.cloud.es.io:9243"
username="elastic"
indexname="bindex"
# create our elasticsearch index
curl -X PUT -u $username:$password "$endpoint/$indexname?pretty" -H "Content-Type: application/json" -d "{\"settings\": {\"analysis\": {\"analyzer\": {\"htmlStripAnalyzer\": {\"type\": \"custom\",\"tokenizer\": \"standard\",\"filter\": [\"lowercase\"],\"char_filter\": [ \"html_strip\" ]}}}},\"mappings\": {\"properties\": {\"html\": {\"type\": \"text\",\"analyzer\": \"htmlStripAnalyzer\"}}}}"

# bulk upload the documents
#curl -X POST -u $username:$password "$endpoint/$indexname/_bulk" -H "Content-Type: application/x-ndjson" --data-binary @data.json

#curl -X GET -u $username:$password "$endpoint/$indexname/_search?pretty" -H "Content-Type: application/json" -d"{\"query\": {\"match_phrase\": {\"html\": \"Harden\"}}}"

#curl -X GET -u $username:$password "$endpoint/$indexname/_search?pretty" -H "Content-Type: application/json" -d"{\"query\": {\"match\": {\"html\": \"Harden\"}}}\"sort\":[{\"_score\":{\"order\":\"desc\",\"mode\":\"max\"}}]"

