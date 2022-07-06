# Automate OpenIndexMaps GeoJSON Creation
This repository includes Python scripts that will create [OpenIndexMaps](https://openindexmaps.org/) from a CSV file.

#### GeoJSON format

OpenIndexMaps use the GeoJSON format.=
Here is the general structure of an OpenIndexMap GeoJSON:

  <img src="https://user-images.githubusercontent.com/66186715/109703921-a70fc100-7b5b-11eb-9013-5f31c9c38142.png" style="width:80%">

## Workflow

**create-indexmap** scripts require a CSV file that contains a spatial field to generate the index map polygons. This field can be either:

- bounding box coordinates (`w,s,e,n`)

OR

- county names 


- #### Raw data

  At a minimum, the input CSV file must include “**Title**”, “**Bounding Box**”, and “**Identifier**”. 

  **1. For regular index maps** 

    It directly queries the coordinates of bounding boxes from the csv files column “**Bounding Box**”.           

   **2. For irregular index maps** 

    In order to create the county-shape polygons, it needs to join the county GeoJSON based on the county name and fetch the coordinates. Therefore, it is necessary to           convert the county Shapefile into GeoJSON first. 


- #### Final products

  **1. Regular Index maps**<img src="https://user-images.githubusercontent.com/66186715/109705985-04a50d00-7b5e-11eb-8b84-fe996fd67501.png">

  **2. Irregular Index maps**

  <img src="https://user-images.githubusercontent.com/66186715/109705809-cb6c9d00-7b5d-11eb-8f86-720e2a6ec6b8.png">
