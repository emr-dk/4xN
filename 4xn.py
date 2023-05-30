import rasterio as io

def ndvi(red, nir):
    '''
    NDVI = (NIR - RED) / (NIR + RED)
    '''
    return (nir - red) / (nir + red)

def ndbi(nir, swir):
    '''
    NDBI = (SWIR - NIR) / (SWIR + NIR) 
    '''
    return (nir - swir) / (nir + swir)


def ndwi(green, nir):
    '''
    NDWI = (GREEN - NIR) / (GREEN + NIR)
    '''
    return (green - nir) / (green + nir)

def ndmi(nir, mir):
    '''
    NDMI = (NIR - MIR) / (NIR + MIR)
    '''
    
    return (nir - mir) / (nir + mir)
