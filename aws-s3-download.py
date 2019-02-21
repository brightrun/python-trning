import boto3

BUCKET_NAME = '<ADD BUCKET NAME HERE>'
KEY = '<ADD PREFIX/KEY HERE>'

s3 = boto3.client('s3')


def get_matching_s3_keys(bucket, prefix='', suffix=''):
    """Get a list of keys in s3 bucket"""
    resp = s3.list_objects(Bucket=bucket,Prefix=prefix)

    for file in resp['Contents']:
        fname = file['Key'].rsplit('/', 1)
        print(fname)
        s3.download_file(bucket, file['Key'], '<ADD LOCAL PATH HERE>' + fname[1])


if __name__ == "__main__":
    get_matching_s3_keys(BUCKET_NAME, KEY)