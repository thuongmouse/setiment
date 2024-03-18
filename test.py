from elasticsearch import Elasticsearch
import pandas as pd
client = Elasticsearch(['116.97.110.171', '9200'])

colunms = ['title']
scan = client.search(index='fb_post_*', size=1000)
data = []
for hit in scan['hits']['hits']:
    data.append([hit['_source'].get(column, '') for column in colunms])
    

df = pd.DataFrame(data, columns=colunms)
df.to_csv('/home/thuongpt/setiment/data/data.csv', index=False)