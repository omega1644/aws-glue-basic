import boto3
import json
import logging

client = boto3.client('glue')

response = client.list_crawlers()

logging.warning(response['CrawlerNames'])

response2 = client.start_crawler(
    Name=response['CrawlerNames'][0]
)

print(json.dumps(response2, indent=4, sort_keys=True, default=str))