variable "credentials_file_path" {
  description = "value of the credentials file"
  default     = "./keys/my-creds.json"

}

variable "project" {
  description = "project"
  default     = "football-data-analytics"

}

variable "region" {
  description = "Project region name"
  default     = "us-central1"

}


variable "location" {
  description = "Project location name"
  default     = "US"

}

variable "bq_dataset_name" {
  description = "my bigquery dataset name"
  type        = string
  default     = "football_data_analytics_dataset" // replace hyphens with underscores
}

variable "gcs_bucket_name" {
  description = "my storage bucket name"
  default     = "football-data-analytics-bucket"
}

variable "gcs_storage_class" {
  description = "bucket storage class"
  default     = "STANDARD"
}