# Automate OpenIndexMaps GeoJSON Creation
This project is inspired by the metadata transformation process Big Ten Academic Alliance (BTAA) Geoportal uses. One weakness of the geoportal is their scanned map atlas, which don’t include index maps for preview. 

*<a href="https://github.com/BTAA-Geospatial-Data-Project/indexmaps/tree/master">Original Repository</a>*

## Workflow
In order to automate the creation of [OpenIndexMaps](https://openindexmaps.org/) GeoJSONs for both county-shape and regular polygons, two Python scripts were created to accomplish it. Here’re the main differences between them:

- #### Raw data - *<a href="https://github.com/YijingZhou33/indexmaps/blob/main/data/03d-01/03d-01.csv">Sample</a>*

  The csv file borrows some fields from the Geoportal’s metadata schema, “***GeoBlacklight***”, which includes “**Title**”, “**Bounding Boxes**” and “**Identifier**”. 

  
- #### Python scripts

  It will create the GeoJSON files to deliver information for each index map. Here is the general structure of an OpenIndexMap GeoJSON:

  <img src="https://user-images.githubusercontent.com/66186715/109703921-a70fc100-7b5b-11eb-9013-5f31c9c38142.png" style="width:80%">
  
  The main difference between regular and irregular index maps is the “**coordinates**” property, 		which represents a geographic area. 

  **1. For regular index maps** - [***regularbbox.ipynb***](https://github.com/YijingZhou33/indexmaps/blob/main/regularbbox.ipynb)

    It directly queries the coordinates of bounding boxes from the csv files column “**Bounding Box**”.           

   **2. For irregular index maps -** [***countybbox.ipynb***](https://github.com/YijingZhou33/indexmaps/blob/main/countybbox.ipynb)

    In order to create the county-shape polygons, it needs to join the county GeoJSON based on the county name and fetch the coordinates. Therefore, it is necessary to           convert the county Shapefile into GeoJSON first - [***countygeojson.ipynb***](https://github.com/YijingZhou33/indexmaps/blob/main/countygeojson.ipynb). 


- #### Final products

  **1. Regular Index maps - *<a href="https://github.com/YijingZhou33/indexmaps/blob/main/data/03d-03/03d-03.geojson">Sample</a>***	<img src="https://user-images.githubusercontent.com/66186715/109705985-04a50d00-7b5e-11eb-8b84-fe996fd67501.png">

  **2. Irregular Index maps - *<a href="https://github.com/YijingZhou33/indexmaps/blob/main/data/03d-01/03d-01.geojson">Sample</a>***

  <img src="https://user-images.githubusercontent.com/66186715/109705809-cb6c9d00-7b5d-11eb-8f86-720e2a6ec6b8.png">
