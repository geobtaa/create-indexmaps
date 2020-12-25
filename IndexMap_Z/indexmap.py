"""
Original created on Dec 1 2020
@author: Yijing Zhou @YijingZhou33
"""

import os
import pandas as pd
import json
import folium
import numpy as np

######################################

### Manual items to change!
## code and title of the metadata 
code = '05a-03'
title = 'Minnesota Plats'


## list of metadata fields from the GBL metadata template for open data portals desired in the final OpenIndexMap geojson.
collist = ['Title', 'Bounding Box', 'Identifier']

## convert the whole csv file to dataframe
df = pd.read_csv(os.path.join('data', code, code+'.csv'))

## check if the metadata contains 'Image' column, if so then add it to the list
## also more properties can be added here!
if 'Image' in df.columns:
    collist.append('Image')

## only extract fields required for OpenIndexMap geojson properties
df = df[collist]


## create regular bouding box coordinate pairs and round them to 2 decimal places
df = pd.concat([df, df['Bounding Box'].str.split(',', expand=True).astype(float).round(2)], axis=1).rename(
    columns={0:'minX', 1:'minY', 2:'maxX', 3:'maxY'})
df['maxXmaxY'] = df.apply(lambda row: [row.maxX, row.maxY], axis = 1)
df['maxXminY'] = df.apply(lambda row: [row.maxX, row.minY], axis = 1)
df['minXminY'] = df.apply(lambda row: [row.minX, row.minY], axis = 1)
df['minXmaxY'] = df.apply(lambda row: [row.minX, row.maxY], axis = 1)
df['coordinates'] = df[['maxXmaxY', 'maxXminY', 'minXminY', 'minXmaxY', 'maxXmaxY']].values.tolist()

## concatenate landing page links
df['websiteURL'] = 'https://geo.btaa.org/catalog/' + df['Identifier']

## clean up unnecessary columns
df_clean = df.drop(columns =['minX', 'minY', 'maxX', 'maxY', 'maxXmaxY', 'maxXminY', 'minXminY', 'minXmaxY', 'Bounding Box'])


## create_geojson_features 
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
                'coordinates':[row['coordinates']]
            },
            'properties': {
                'label': row['Title'],
                'title': row['Title'],
                'recordIdentifier': row['Identifier'],
                'websiteUrl': row['websiteURL']
            }
        }
        ### add more properties here if applicable
        if 'Image' in df.columns:
            feature['properties']['thumbnailUrl'] = row['Image']

        features.append(feature)
    return geojson

data_geojson = create_geojson_features(df_clean)


## create geojson file
with open(os.path.join('data', code, code+'.geojson'), 'w') as txtfile:
    json.dump(data_geojson, txtfile)
print('> Creating GeoJSON file...')

