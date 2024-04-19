# Football-Data-Analytics
Interactive Dashboard for Football Kaggle dataset from Transfermarkt.

# download_from_kaggle.sh Script 

This script is designed to download datasets from Kaggle using the Kaggle API, unzip the downloaded files, and upload them to a specified Google Cloud Storage (GCS) bucket. It is intended to be run on a Google Cloud Platform (GCP) Virtual Machine (VM) using Debian Bash.

## Workflow

1. The script is initiated with the Kaggle dataset name and the GCS bucket name as arguments.

2. The Kaggle API token is used to download the specified dataset.

3. The downloaded `.zip` files are unzipped in the current directory.
   - The script iterates over each `.zip` file in the directory and unzips it.

4. The `bucket_name` variable is set to the name of the existing GCS bucket.

5. All `.csv` files in the current directory are uploaded to the specified GCS bucket.
   - The `gsutil cp` command is used to copy the files to the bucket.

6. A message is printed to the console when the upload is complete.

**Note:** The VM running this script needs to have write access to the GCS bucket.

## Running the Script on GCP VM

To run this script on a GCP VM, use the following command:

```bash
bash download_from_kaggle.sh <kaggle_dataset_name> <bucket_name>
```

# here comes the mage part 



