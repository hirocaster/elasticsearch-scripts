from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch("localhost:9200")
es.indices.get_aliases().keys()
