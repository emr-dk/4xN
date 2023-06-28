# 4xN
Just a quick example of four different analyses based on satellite imagery. These are commonly and easily used to analyse vegetation, water and urban areas.

The analyses will be as follows: 
- NDVI: Normalized Difference Vegetation Index, 
- NDBI: Normalized Difference Built-up Index, 
- NDWI: Normalized Difference Water Index, 
- NDMI: Normalized Difference Moisture Index.

They are all types of _normalized_ difference indices. This means that they are all calculated by taking the difference between two bands and dividing it by the sum of the two bands. As such:
* the resulting values range from -1 to 1. 
* The higher the value, the more of the feature there is in the area. The lower the value, the less of the feature there is in the area.

The thresholds will be dependent on the area being analysed. For example, a desert area will have a lower NDVI value than a forest area.


## NDVI
Normalized Difference Vegetation Index (NDVI) gives an indication of the amount of vegetation in an area. It is calculated by taking the difference between the near-infrared (NIR) and red light bands and dividing it by the sum of the NIR and red light bands. 


```{python}
def ndvi(red, nir):
    return (nir - red) / (nir + red)
```

## NDBI
Normalized Built-up Index (NDBI) gives an indication of the amount of built-up area in an area. It is calculated by taking the difference between the near-infrared (NIR) and shortwave infrared (SWIR) light bands and dividing it by the sum of the NIR and SWIR light bands. 

```
def ndbi(nir, swir):
    return (nir - swir) / (nir + swir)
```

## NDWI 
Normalized Difference Water Index (NDWI) gives an indication of the amount of water in an area. It is calculated by taking the difference between the green and near-infrared (NIR) light bands and dividing it by the sum of the green and NIR light bands. 

```
def ndwi(green, nir):
    return (green - nir) / (green + nir)
```

## NDMI
Normalized Difference Moisture Index (NDMI) gives an indication of the amount of moisture in an area. It is calculated by taking the difference between the near-infrared (NIR) and mid-infrared (MIR) light bands and dividing it by the sum of the NIR and MIR light bands.

```
def ndmi(nir, mir):
    return (nir - mir) / (nir + mir)
```