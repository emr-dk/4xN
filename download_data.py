'''
https://sentinelhub-py.readthedocs.io/en/latest/examples.html
'''

import os 
import datetime
import yaml

#import matplotlib.pyplot as plt
#import numpy as np
from sentinelhub import (
    CRS,
    BBox,
    DataCollection,
    DownloadRequest,
    MimeType,
    MosaickingOrder,
    SentinelHubDownloadClient,
    SentinelHubRequest,
    bbox_to_dimensions,
)

from sentinelhub import SHConfig

with open("credentials.yml", 'r') as cred:
    credentials = yaml.safe_load(cred)

user = credentials['sentinelhub']['user']
password = credentials['sentinelhub']['password']

config = SHConfig()

if not config.sh_client_id or not config.sh_client_secret:
    print("Warning! To use Process API, please provide the credentials (OAuth client ID and client secret).")

resolution = 10

# Bounding box of Copenhagen
cph_bbox = BBox(bbox=[12.521087, 55.638377, 12.575808, 55.673333], crs=CRS.WGS84)
cph_size = bbox_to_dimensions(cph_bbox, resolution=resolution)


