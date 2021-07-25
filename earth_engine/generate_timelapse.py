import geemap
import os
import ee

ee.Initialize()
roi = ee.Geometry.Rectangle([20, 3, 20.1, 3.1])
# roi = ee.Geometry.Polygon(
#     [[[27, 75],
#       [27, 76],
#         [26, 76],
#         [26, 75],
#         [27, 75]]], None, False)

collection = geemap.landsat_timeseries(roi=roi, start_year=1985, end_year=2019, start_date='06-10', end_date='09-20')

print("collection size info", collection.size().getInfo())
# Define arguments for animation function parameters.
video_args = {
  'dimensions': 768,
  'region': roi,
  'framesPerSecond': 10,
  'bands': ['Red', 'Green', 'Blue'],
  'min': 0,
  'max': 4000,
  'gamma': [1, 1, 1]
}

out_gif_path = "test.gif"
geemap.download_ee_video(collection, video_args, out_gif_path)