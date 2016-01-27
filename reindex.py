from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch("localhost:9200")
for i in es.indices.get_aliases().keys():
  if i.find('nginx') > -1:
    new_name = "%s.reindex" % i
    try:
      helpers.reindex(es, i, new_name)
    except:
      next
    es.indices.delete(index=i)
