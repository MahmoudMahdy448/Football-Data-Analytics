from google.cloud import bigquery

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_bigquery(data_list, *args, **kwargs):
    # Create a BigQuery client
    client = bigquery.Client()

    # Define your BigQuery dataset
    dataset_id = 'football_data_analytics_dataset'

    for i, data in enumerate(data_list):
        # Define your BigQuery table
        table_id = f'players_{i}'

        # Specify the table schema
        schema = [bigquery.SchemaField(field_name, str(field_type)) for field_name, field_type in zip(data.columns, data.dtypes)]

        # Create a new table in the dataset
        table = bigquery.Table(f"{dataset_id}.{table_id}", schema=schema)
        table = client.create_table(table)

        # Load the DataFrame to the table
        job = client.load_table_from_dataframe(data, table_id)
        job.result()  # Wait for the job to complete

        print(f"Exported {job.output_rows} rows to {dataset_id}.{table_id}")