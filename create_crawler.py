import boto3
import json

client = boto3.client('glue')

response = client.create_crawler(
    Name='S3-boto-crawler-2',
    Role='GlueFullAccess',
    DatabaseName='input',
    Targets={
        'S3Targets': [
            {
                'Path': 'https://sydney-bucket-city-data.s3.ap-southeast-2.amazonaws.com/input/customers/',
                'Exclusions': [
                    'string',
                ],
                'SampleSize': 2
            },
        ]
    },
    Schedule='cron(15 12 * * ? *)',
    SchemaChangePolicy={
        'UpdateBehavior': 'UPDATE_IN_DATABASE',
        'DeleteBehavior': 'DEPRECATE_IN_DATABASE'
    },
    RecrawlPolicy={
        'RecrawlBehavior': 'CRAWL_EVERYTHING'
    },
    LineageConfiguration={
        'CrawlerLineageSettings': 'DISABLE'
    }
)

response = json.dumps(response, indent=4, sort_keys=True, default=str)
print(response)