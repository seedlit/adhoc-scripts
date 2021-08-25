# Note that you need to have an account on Google Earth Engine to use this.
# Limitation is that you can only download GeoTiff with max dimensions 10000*10000

import os
import ee
import urllib.request
import zipfile
import csv
import numpy as np
from multiprocessing import Pool


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


def get_value_at_point(data_url, ee_point_geom, band_name=None, start_date=None, end_date=None):
    if start_date and end_date:
        image_collection = ee.ImageCollection(data_url).filterDate(start_date, end_date).filterBounds(ee_point_geom)
    else:
        image_collection = ee.ImageCollection(data_url).filterBounds(ee_point_geom)
    img = image_collection.first()
    if band_name:
        data = img.select(band_name).reduceRegion(ee.Reducer.mean(),ee_point_geom,10).get(band_name)
    print(data)


def download_data(download_url, out_path):
    urllib.request.urlretrieve(download_url, out_path)


def extract_zip(src_zip_file, out_dir):
    with zipfile.ZipFile(src_zip_file, "r") as zip_ref:
        zip_ref.extractall(out_dir)

def main(left, bottom, top, right, out_dir):
    try:
        aoi = get_aoi(left, bottom, right, top)
        download_url = get_download_url(aoi)
        file_download_path = os.path.join(
            out_dir,
            "left_{}_right_{}_top_{}_bottom_{}.zip".format(
                left, right, top, bottom
            ),
        )
        download_data(download_url, file_download_path)
    except Exception as e:
        print("some error ", e)

if __name__ == "__main__":

    from time import time
    start_time = time()

    out_dir = "/home/naman/Desktop/side_projects/3d-maps/data/netherlands_all_dsms"
    os.makedirs(out_dir, exist_ok=True)
    ee.Initialize()

    error_txt_path = "errors.txt"
    error_csv_path = "errors.csv"

    error_list = []
    task_list = []
    for lat in np.arange(50.75, 53.56, 0.02):
        for lon in np.arange(3.36, 7.23, 0.02):
            try:
                # define bounds
                left = lon
                right = lon + 0.02
                bottom = lat
                top = lat + 0.02
                # aoi = get_aoi(left, bottom, right, top)
                # download_url = get_download_url(aoi)
                # file_download_path = os.path.join(
                #     out_dir,
                #     "left_{}_right_{}_top_{}_bottom_{}.zip".format(
                #         left, right, top, bottom
                #     ),
                # )
                # download_data(download_url, file_download_path)
                task_list.append([left, bottom, top, right, out_dir])
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

    print("total {} chips will get downloaded".format(len(task_list)))
    p = Pool(12)
    p.starmap(main, task_list)
    p.close()
    p.join()
    
    print("Took {} seconds in total".format(time() - start_time))