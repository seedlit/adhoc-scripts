# Useful tools - Whiteboxtools - https://jblindsay.github.io/wbt_book/python_scripting/example.html
#              - lastools - https://github.com/LAStools/LAStools
#              - lidar2dem - https://applied-geosolutions.github.io/lidar2dems/doc/installation.html
#              - pdal - https://pdal.io/

# Notes about PDAL:
# 1. Unable to install in venv. Getting pep 517 error.
# 2. Install globally with: sudo apt-get update; sudo apt-get install pdal

# Useful tutorials on pdal - 
# 1. https://paulojraposo.github.io/pages/PDAL_tutorial.html
# 2. https://www.simonplanzer.com/articles/lidar-chm/

# Run pdal in command line with appropriate jsons.
# some sample jsons are here in the same directory.
# syntax: pdal pipeline pdal_las_to_dsm.json

# Sample point cloud datasets - 
# 1. https://cloud.rockrobotic.com/share/f42b5b69-c87c-4433-94f8-4bc0d8eaee90#lidar