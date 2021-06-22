import matplotlib.pyplot as plt
import gdal


dtm_path = "/home/naman/Desktop/side_projects/dsm2dtm/generated_dtm/sample_dsm_ds_dtm.tif"
dtm = gdal.Open(dtm_path).ReadAsArray()

dsm_path = "data/iitgn/sample_dsm.tif"
dsm = gdal.Open(dsm_path).ReadAsArray()

plt.figure()
ax = plt.subplot(1,2,1)
ax.set_title("Input DSM (Digital Surface Model)")
plt.imshow(dsm, vmin=55, vmax=80)
plt.colorbar()


ax = plt.subplot(1,2,2)
ax.set_title("Generated DTM (Digital Terrain Model)")
plt.imshow(dtm, vmin=55, vmax=80)
plt.colorbar()

plt.show()