from keys import x
from elasticsearch import Elasticsearch
import glob
import json

## Настраиваю подключение к БД
es = Elasticsearch(['http://'], http_auth=('login', 'password'))

if es.ping:
  ptint('connected')
  
  
files = glob.glob("path/to/files/*.json")

for file in files:
  print(file)
  with open(file, 'r', encoding='UTF-8') as to_read:
    for row in to_read:
      row = json.loads(row)
      x['company_name'] = row['company']
      x['IPO_date'] = row['IPO']
      try:
        resp = es.index(index='index_name', body=x)
      except Exception as F:
        print(F)
