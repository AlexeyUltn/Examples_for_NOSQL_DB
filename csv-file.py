from keys import x
from elasticsearch import Elasticsearch
import glob
import csv
import sys
import os

## Настраиваю подключение к БД
es = Elasticsearch(['http://'], http_auth=('login', 'password'))

if es.ping:
  ptint('connected')
  
  
files = glob.glob("path/to/files/*.csv")

for file in files:
  print(file)
  with open(file, 'r', encoding='UTF-8') as to_read:
    file_reader = csv.DictReader(to_read, delimiter=',')
    counter = 0
      for row in file_reader:
        counter+= 1
        x['company_name'] = row['company']
        x['IPO_date'] = row['IPO']
        if counter %1000 ==0:
          sys.stdout.write("\r{}".format(counter))
        try:
          resp = es.index(index='index_name', body=x)
        except Exception as F:
          print(F)
      os.rename(file, file.replace(".csv", "_done.csv"))
