import logging
import json
from pathlib import Path
from .config import CONFIG

# def export_data_to_s3(updated_data):
#     try:
#         logging.info(f'[+] Uploading updated data file to bucket {CONFIG.BUCKET_NAME}..')
#         s3 = boto3.client('s3')
#         s3.put_object(Bucket=CONFIG.BUCKET_NAME, Key=CONFIG.DATA_EXPORT_PATH, Body=json.dumps(updated_data))
#         logging.info(f'[+] DONE!')
#     except Exception as e:
#         logging.warning(f'[!] Error uploading file to S3: {e}')


def export_data_to_json(updated_data):
    export_dir = Path(CONFIG.DATA_DIR_NAME)

    if not export_dir.is_absolute():
        export_dir = Path(__file__).resolve().parent / export_dir

    export_dir.mkdir(parents=True, exist_ok=True)
    export_file = export_dir / CONFIG.DATA_EXPORT_FILENAME

    try:
        logging.info(f'[+] Uploading updated data file to {export_file}..')
        with open(export_file, 'w', encoding='utf-8') as json_file:
            json.dump(updated_data, json_file, ensure_ascii=False, indent=4)
        logging.info(f'[+] DONE!')
    except Exception as e:
        logging.warning(f'[!] Error uploading file: {e}')