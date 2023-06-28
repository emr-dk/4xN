import rasterio as io
import os
import fnmatch
import numpy as np

CURR_DIR = os.getcwd()

def band_translator(band_number: int | str):
    '''
    This function is used to translate the band number to the band name. Just as a good measure the 
    abbreviations cover the following:
    blue, green, red, near infrared, mid infrared, shortwave infrared, shortwave infrared 2, panchromatic, cirrus, thermal infrared 1, thermal infrared 2
    '''
    band_dict = {
        1: 'blue',
        2: 'green',
        3: 'red',
        4: 'nir',
        5: 'mir',
        6: 'swir',
        7: 'swir2',
        8: 'pan',
        9: 'cirrus',
        10: 'tirs1',
        11: 'tirs2'
    }
    if type(band_number) == int:
        return band_dict[band_number]
    elif type(band_number) == str:
        for key, value in band_dict.items():
            if value == band_number:
                return key
        else:
            raise ValueError('Band number not found')
    else:
        raise ValueError('Band number must be int or str')

def output_sensor_array(wanted_band: str):
    '''
    Read a specific band and output it as np array. The wanted band is given
    as a string, such as 'red', 'nir', etc, or an integer.
    '''
    band_number = str(band_translator(wanted_band))
    padded_band = band_number.zfill(2)
    sentinel_band = "*_B" + padded_band + "_*"
    base_path = CURR_DIR + "/data/"
    for element in os.listdir(base_path):
        if fnmatch.fnmatch(element, sentinel_band):
            with io.open(base_path + element) as band:
                data = band.read(1)
            return data
        else:
            print("Band not found")

def ndvi():
    '''
    NDVI = (NIR - RED) / (NIR + RED)
    '''
    red = output_sensor_array("red")
    nir = output_sensor_array("nir")
    ndvi = np.divide(np.subtract(nir,red),np.add(nir,red))

    return ndvi

def ndbi(nir, swir):
    '''
    NDBI = (SWIR - NIR) / (SWIR + NIR) 
    '''
    swir = output_sensor_array("swir")
    nir = output_sensor_array("nir")
    ndbi = np.divide(np.subtract(swir,nir),np.add(swir,nir))

    return ndbi

def ndwi(green, nir):
    '''
    NDWI = (GREEN - NIR) / (GREEN + NIR)
    '''
    green = output_sensor_array("green")
    nir = output_sensor_array("nir")
    ndwi = np.divide(np.subtract(green,nir),np.add(green,nir))

    return ndwi

def ndmi(nir, mir):
    '''
    NDMI = (NIR - MIR) / (NIR + MIR)
    '''
    nir = output_sensor_array("nir")
    mir = output_sensor_array("mir")
    ndmi = np.divide(np.subtract(nir,mir),np.add(nir,mir))

    return ndmi
