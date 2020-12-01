import os
import pandas as pd
import json

##### Manually changed items #####
code = '03d-03'
title = 'Original Land Survey Maps: Iowa'

df = pd.read_csv(os.path.join('data', code, code+'.csv'))[['Title', 'Bounding Box', 'Information', 'Identifier']]
df.head()

df = pd.concat([df, df['Bounding Box'].str.split(',', expand=True).astype(float)], axis=1).rename(
    columns={0:'minX', 1:'minY', 2:'maxX', 3:'maxY'})
df['maxXmaxY'] = df.apply(lambda row: [row.maxX, row.maxY], axis = 1)
df['maxXminY'] = df.apply(lambda row: [row.maxX, row.minY], axis = 1)
df['minXminY'] = df.apply(lambda row: [row.minX, row.minY], axis = 1)
df['minXmaxY'] = df.apply(lambda row: [row.minX, row.maxY], axis = 1)
df['websiteURL'] = 'https://geo.btaa.org/catalog/' + df['Identifier']
df_clean = df.drop(columns =['minX', 'minY', 'maxX', 'maxY'])
df_clean.head()

# create_geojson_features 
def create_geojson_features(df):
    print('> Creating GeoJSON features...')
    features = []
    geojson = {
        'type': 'FeatureCollection',
        'title': title,
        'features': features
    }
    for _, row in df.iterrows():
        feature = {
            'type': 'Feature',
            'id': row['Identifier'],
            'geometry': {
                'type':'Polygon', 
                'coordinates':[[row['maxXmaxY'], row['maxXminY'], row['minXminY'], row['minXmaxY'], row['maxXmaxY']], ]
            },
            'properties': {
                'label': row['Title'],
                'title': row['Title'],
                'recordIdentifier': row['Identifier'],
                'websiteUrl': row['websiteURL'],
                'information': row['Information']
            }
           }

        features.append(feature)
    return geojson

data_geojson = create_geojson_features(df_clean)

# create geojson file
with open(os.path.join('data', code, code+'.geojson'), 'w') as txtfile:
    json.dump(data_geojson, txtfile)
print('> Creating GeoJSON file...')

