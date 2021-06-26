# All these commands are to be run in the google colab notebook

# Mounting Google Drive
from google.colab import drive
drive.mount('/content/gdrive')

# Uploading kaggle API token json file
from google.colab import files
files.upload()

!pip install -q kaggle
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!ls ~/.kaggle
!chmod 600 /root/.kaggle/kaggle.json

# download data
!kaggle competitions download -c siim-covid19-detection -p /content/gdrive/My\ Drive/kaggle/covid

# unzip data
import os
os.chdir('/content/gdrive/MyDrive/kaggle/covid') 
!mkdir train  #create a directory named train/
!mkdir test  #create a directory named test/
!unzip -q \*.zip -d train/
