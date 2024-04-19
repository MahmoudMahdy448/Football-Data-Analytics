#!/bin/bash
#usage ./download_from_kaggle.sh .sh datasetname

# Installing python3 and pip and the dependencies
sudo apt update
sudo apt install -y python3 python3-dev python3-venv
sudo apt install -y wget unzip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

# Installing kaggle API
pip3 install kaggle

# updating $PATH
export PATH=$PATH:/home/$USER/.local/bin

#Import kaggle.json to the VM and copy it to .kaggle 
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# download the dataset 
echo "downloading dataset from: $1..."
kaggle datasets download -d $1

#unzip it
echo "unzipping file... "
 

for file in *.zip
do
unzip "$file" -d ./
done

# Set the bucket name to the existing bucket
bucket_name="football-data-analytics-bucket"

#upload it to GCS
echo "uploading to GCS..."
gsutil cp *.csv gs://$bucket_name

echo "upload complete ..."
# Note that the VM need to have GCS write access 