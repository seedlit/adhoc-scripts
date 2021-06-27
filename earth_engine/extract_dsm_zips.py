import os
from dsm2dtm import main
import zipfile


def extract_zip(src_zip_file, out_dir):
    with zipfile.ZipFile(src_zip_file, "r") as zip_ref:
        zip_ref.extractall(out_dir)


def replace_point_from_tif_name(file_dir, in_file_path):
    filename = in_file_path.split("/")[-1].replace(".tif", "")
    filename = filename.replace(".", '_point_')
    dest_file_path = os.path.join(file_dir, filename + ".tif")
    os.rename(in_file_path, dest_file_path)
    return dest_file_path



if __name__ == "__main__":

    dsm_zips_dir = "/root/ee/repo/netherlands_dsm"    
    
    dsms_dir = "/root/dtm/extracted_dsms"
    out_dtm_dir = "/root/dtm/generated_dtms"
    os.makedirs(dsms_dir, exist_ok=True)
    os.makedirs(out_dtm_dir, exist_ok=True)
    temp_dir = "/root/dtm/temp_dir"
    os.makedirs(temp_dir, exist_ok=True)
    for zip_file in os.listdir(dsm_zips_dir):
        try:
            zip_path = os.path.join(dsm_zips_dir, zip_file)
            extract_zip(zip_path, temp_dir)
            for tif in os.listdir(temp_dir):
                src_tif_path = os.path.join(temp_dir, tif)
                dest_tif_path = os.path.join(dsms_dir, tif.replace(tif.split(".")[0], zip_file.replace(".zip", "")))
                os.rename(src_tif_path, dest_tif_path)
                updated_tif_path = replace_point_from_tif_name(dsms_dir, dest_tif_path)
                dtm_tif_path = main(updated_tif_path, out_dtm_dir)
                print("######################### generated dtm ", dtm_tif_path)
        except Exception as e:
            print("#############some error in ", zip_path)
            print("################error ", e)
            