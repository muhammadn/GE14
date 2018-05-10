#!/usr/bin/env python
from elasticsearch import Elasticsearch

es = Elasticsearch()

res = es.search(index="ge14-index", body={"query": {"match_all": {}}})
# res = es.get(index='ge14-index', doc_type='message', id=1)
print res
