#!/usr/bin/env python
#
# Setup script for the Natural Language Toolkit Data.
#
# Copyright (C) 2001-2020 NLTK Project
#
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

import boto3
from botocore.client import Config

class Space:
    def __init__(self, access_key_id, secret_access_key, region_name='sgp1'):
        # Initialize a session using DigitalOcean Spaces.
        self.session = boto3.session.Session()
        self.client = self.session.client('s3',
            region_name=region_name,
            endpoint_url=f'https://{region_name}.digitaloceanspaces.com',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key)

    def list_buckets():
        self.client.list_buckets()
