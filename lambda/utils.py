<<<<<<< HEAD
import json
from os.path import exists
=======
import logging
import os

import boto3
from botocore.exceptions import ClientError
>>>>>>> main


CONFIG_FILE = "config.json"

<<<<<<< HEAD

def load_config() -> dict:
    if not exists(CONFIG_FILE):
        raise ValueError(f"Config file does not exist")

    with open(CONFIG_FILE) as f:
        return json.load(f)
=======
    :param object_name: string
    :return: Presigned URL as string. If error, returns None.
    """
    s3_client = boto3.client(
        "s3",
        region_name=os.environ.get("S3_PERSISTENCE_REGION"),
        config=boto3.session.Config(
            signature_version="s3v4", s3={"addressing_style": "path"}
        ),
    )
    try:
        bucket_name = os.environ.get("S3_PERSISTENCE_BUCKET")
        response = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_name},
            ExpiresIn=60 * 1,
        )
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response
>>>>>>> main
