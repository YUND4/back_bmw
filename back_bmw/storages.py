from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
import boto3
from botocore.exceptions import NoCredentialsError
from storages.utils import clean_name

class S3PresignedUrlStorage(S3Boto3Storage):
    
    def url(self, name, parameters=None, expire=3600):
        """
        Generate a presigned URL for the file.
        :param name: The name of the file.
        :param parameters: Additional parameters for the URL.
        :param expire: Time in seconds for the URL to expire.
        :return: A presigned URL.
        """
        # Ensure parameters is not None
        parameters = parameters or {}

        # Try to generate a presigned URL
        try:
            s3_client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                      region_name=settings.AWS_S3_REGION_NAME)

            presigned_url = s3_client.generate_presigned_url('get_object',
                                                             Params={
                                                                 'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                                                                 'Key': self._normalize_name(clean_name(name)),
                                                                 **parameters
                                                             },
                                                             ExpiresIn=expire)
            return presigned_url
        except NoCredentialsError:
            raise ValueError("AWS Credentials not found.")

        except Exception as e:
            raise ValueError(f"Failed to generate presigned URL: {str(e)}")
