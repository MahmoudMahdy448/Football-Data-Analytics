from google.cloud import storage
import pandas as pd
import pyarrow.parquet as pq
import io

@data_loader
def load_data_from_gcs(bucket_name, prefix):
    # Create a client
    client = storage.Client()

    # Get the bucket
    bucket = client.get_bucket(bucket_name)

    # Get blobs in the directory
    blobs = bucket.list_blobs(prefix=prefix)

    # Load each Parquet file
    data = {}
    for blob in blobs:
        # Download the blob to a bytes object
        blob_bytes = blob.download_as_bytes()

        # Create a BytesIO object
        blob_io = io.BytesIO(blob_bytes)

        # Load the Parquet file
        df = pq.read_table(blob_io).to_pandas()

        # Add the DataFrame to the dictionary
        data[blob.name] = df

    return data

# Usage:
data = load_data_from_gcs('football-data-analytics-bucket', 'appearances_data')