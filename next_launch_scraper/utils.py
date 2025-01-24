import logging
import json
import boto3
from pathlib import Path
from .config import CONFIG
from google.cloud import storage


def export_data_to_s3(updated_data: list) -> None:
    try:
        logging.info(f'[+] Uploading updated data file to bucket {CONFIG.BUCKET_NAME} [...]')
        s3 = boto3.client('s3')
        s3.put_object(Bucket=CONFIG.BUCKET_NAME, Key=CONFIG.DATA_EXPORT_FILENAME, Body=json.dumps(updated_data))
        logging.info(f'[+] DONE!')
    except Exception as e:
        logging.warning(f'[!] Error uploading file to S3: {e}')


def export_data_to_json(updated_data: list) -> None:

    # Set export directory and file path, creating the directory if needed.
    current_dir = Path.cwd()
    export_dir = current_dir / CONFIG.DATA_DIR_NAME
    export_dir.mkdir(parents=True, exist_ok=True)
    export_file = export_dir / CONFIG.DATA_EXPORT_FILENAME

    try:
        logging.info(f'[+] Uploading updated data file to {export_file} [...]')
        with open(export_file, 'w', encoding='utf-8') as json_file:
            json.dump(updated_data, json_file, ensure_ascii=False, indent=4)
        logging.info(f'[+] DONE!')
    except Exception as e:
        logging.warning(f'[!] Error uploading file: {e}')


def export_data_to_gcp(updated_data: list) -> None:
    try:
        logging.info(f'[GCP] -> Uploading updated data file to bucket {CONFIG.BUCKET_NAME} [...]')
        client = storage.Client()
        bucket = client.get_bucket(CONFIG.BUCKET_NAME)
        blob = bucket.blob(CONFIG.DATA_EXPORT_FILENAME)
        blob.upload_from_string(
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        logging.info('[+] -> DONE!')
    except Exception as e:
        logging.warning(f'[!] -> Error uploading file to GCP bucket: {e}')
