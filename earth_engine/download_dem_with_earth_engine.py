# This script downloads 30m SRTM DEM (Digital Elevation Model) using Google Earth Engine.
# Note that you need to have an account on Google Earth Engine to use this.
# Limitation is that you can only download GeoTiff with max dimensions 10000*10000

import os
import ee
import urllib.request
import zipfile


def get_aoi(left, bottom, right, top):
    aoi = ee.Geometry.Rectangle([left, bottom, right, top])
    return aoi


def get_download_url(aoi):
    # Import the USGS ground elevation image.
    elv = ee.Image("USGS/SRTMGL1_003")
    link = elv.getDownloadURL(
        {"scale": 30, "crs": "EPSG:4326", "fileFormat": "GeoTIFF", "region": aoi}
    )
    return link


def download_data(download_url, out_path):
    urllib.request.urlretrieve(download_url, out_path)


def extract_zip(src_zip_file, out_dir):
    with zipfile.ZipFile(src_zip_file, "r") as zip_ref:
        zip_ref.extractall(out_dir)


if __name__ == "__main__":

    # define bounds
    left = 80.0
    bottom = 30.0
    right = 81.0
    top = 31.0
    out_dir = "srtm_dem"

    os.makedirs(out_dir, exist_ok=True)
    ee.Initialize()
    aoi = get_aoi(left, bottom, right, top)
    download_url = get_download_url(aoi)
    file_download_path = os.path.join(out_dir, "dem.zip")
    download_data(download_url, file_download_path)
    extract_zip(file_download_path, out_dir)
    os.remove(file_download_path)
