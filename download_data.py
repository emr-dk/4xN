'''
https://sentinelhub-py.readthedocs.io/en/latest/examples.html
'''

import os 
import datetime

import matplotlib.pyplot as plt
import numpy as np

from sentinelhub import (
    CRS,
    BBox,
    DataCollection,
    DownloadRequest,
    MimeType,
    MosaickingOrder,
    SentinelHubDownloadClient,
    SentinelHubRequest,
    bbox_to_dimensions
)

from sentinelhub import SHConfig

config = SHConfig()

if not config.sh_client_id or not config.sh_client_secret:
    print("Warning! To use Sentinel Hub services, please provide the credentials (client ID and client secret).")

resolution = 10
cph_bbox = BBox(bbox=[12.521087, 55.638377, 12.575808, 55.673333], crs=CRS.WGS84)
cph_size = bbox_to_dimensions(cph_bbox, resolution=resolution)


