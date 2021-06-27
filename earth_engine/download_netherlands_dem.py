# Note that you need to have an account on Google Earth Engine to use this.
# Limitation is that you can only download GeoTiff with max dimensions 10000*10000

import os
import ee
import urllib.request
import zipfile
import csv
import numpy as np


def get_aoi(left, bottom, right, top):
    aoi = ee.Geometry.Rectangle([left, bottom, right, top])
    return aoi


def get_download_url(aoi):
    # Import the USGS ground elevation image.
    elv = ee.Image("AHN/AHN2_05M_RUW")
    link = elv.getDownloadURL(
        {"scale": 1, "crs": "EPSG:4326", "fileFormat": "GeoTIFF", "region": aoi}
    )
    return link

def download_data(download_url, out_path):
    urllib.request.urlretrieve(download_url, out_path)


def extract_zip(src_zip_file, out_dir):
    with zipfile.ZipFile(src_zip_file, "r") as zip_ref:
        zip_ref.extractall(out_dir)


if __name__ == "__main__":

    from time import time
    start_time = time()

    out_dir = "netherlands_dsm"
    os.makedirs(out_dir, exist_ok=True)
    ee.Initialize()

    error_txt_path = "errors.txt"
    error_csv_path = "errors.csv"

    error_list = []
    for lat in np.arange(53, 54, 0.02):
        for lon in np.arange(5, 6, 0.02):
            try:
                # define bounds
                left = lon
                right = lon + 0.02
                bottom = lat
                top = lat + 0.02
                aoi = get_aoi(left, bottom, right, top)
                download_url = get_download_url(aoi)
                file_download_path = os.path.join(
                    out_dir,
                    "left_{}_right_{}_top_{}_bottom_{}.zip".format(
                        left, right, top, bottom
                    ),
                )
                download_data(download_url, file_download_path)
                # extract_zip(file_download_path, out_dir)
                # os.remove(file_download_path)
            except Exception as e:
                print(
                    "some error for left: {}, right: {}, top :{}, bottom {}".format(
                        left, right, top, bottom
                    )
                )
                print("error: ", e)
                with open(error_txt_path, "a") as txt_file:
                    txt_file.write(
                        "some error for left: {}, right: {}, top :{}, bottom {}\n".format(
                            left, right, top, bottom
                        )
                    )
                    txt_file.write("error: {}\n".format(e))
                    error_list.append(
                        {
                            "left": left,
                            "right": right,
                            "top": top,
                            "bottom": bottom,
                            "error": e,
                        }
                    )

    field_names = ["left", "right", "top", "bottom", "error"]
    with open(error_csv_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(error_list)
    
    print("Took {} seconds in total".format(time() - start_time))