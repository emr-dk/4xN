# 4xN
Just a quick example of four different analyses based on satellite imagery. These are commonly and easily used to analyse vegetation, water and urban areas.

The analyses will be as follows: 
- NDVI: Normalized Difference Vegetation Index, 
- NDBI: Normalized Difference Built-up Index, 
- NDWI: Normalized Difference Water Index, 
- NDMI: Normalized Difference Moisture Index.


## NDVI
Normalized Difference Vegetation Index (NDVI) gives an indication of the amount of vegetation in an area. It is calculated by taking the difference between the near-infrared (NIR) and red light bands and dividing it by the sum of the NIR and red light bands. The resulting values range from -1 to 1. The higher the value, the more vegetation there is in the area. The lower the value, the less vegetation there is in the area. 

Therefore, there is no vegetation in areas where the NDVI value is less than 0.1. There is some vegetation in areas where the NDVI value is between 0.1 and 0.3. There is a lot of vegetation in areas where the NDVI value is greater than 0.3. But this is also dependent on the area being analysed. For example, a desert area will have a lower NDVI value than a forest area.

def ndvi(red, nir):
    return (nir - red) / (nir + red)


## NDBI
Normalized Built-up Index (NDBI) gives an indication of the amount of built-up area in an area. It is calculated by taking the difference between the near-infrared (NIR) and shortwave infrared (SWIR) light bands and dividing it by the sum of the NIR and SWIR light bands. The resulting values range from -1 to 1. The higher the value, the more built-up area there is in the area. The lower the value, the less built-up area there is in the area.

Therefore, there is no built-up area in areas where the NDBI value is less than 0.1. There is some built-up area in areas where the NDBI value is between 0.1 and 0.3. There is a lot of built-up area in areas where the NDBI value is greater than 0.3. But this is also dependent on the area being analysed. For example, a desert area will have a lower NDBI value than a forest area.

def ndbi(nir, swir):
    return (nir - swir) / (nir + swir)


## NDWI 
Normalized Difference Water Index (NDWI) gives an indication of the amount of water in an area. It is calculated by taking the difference between the green and near-infrared (NIR) light bands and dividing it by the sum of the green and NIR light bands. The resulting values range from -1 to 1. The higher the value, the more water there is in the area. The lower the value, the less water there is in the area.

Therefore, there is no water in areas where the NDWI value is less than 0.1. There is some water in areas where the NDWI value is between 0.1 and 0.3. There is a lot of water in areas where the NDWI value is greater than 0.3. But this is also dependent on the area being analysed. For example, a desert area will have a lower NDWI value than a forest area.

def ndwi(green, nir):
    return (green - nir) / (green + nir)


## NDMI
Normalized Difference Moisture Index (NDMI) gives an indication of the amount of moisture in an area. It is calculated by taking the difference between the near-infrared (NIR) and mid-infrared (MIR) light bands and dividing it by the sum of the NIR and MIR light bands. The resulting values range from -1 to 1. The higher the value, the more moisture there is in the area. The lower the value, the less moisture there is in the area.

Therefore, there is no moisture in areas where the NDMI value is less than 0.1. There is some moisture in areas where the NDMI value is between 0.1 and 0.3. There is a lot of moisture in areas where the NDMI value is greater than 0.3. But this is also dependent on the area being analysed. For example, a desert area will have a lower NDMI value than a forest area.

def ndmi(nir, mir):
    return (nir - mir) / (nir + mir)
