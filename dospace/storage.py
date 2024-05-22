from storages.backends.s3boto3 import S3Boto3Storage


class CustomMediaS3Boto3Storage(S3Boto3Storage):
    file_overwrite = False

    def _save(self, name, content):
        public_directories = ['pimages/', 'pimages\\']
        if any(directory in name for directory in public_directories):
            self.default_acl = 'public-read'
        else:
            self.default_acl = 'private'

        return super()._save(name, content)


# class CustomStaticS3Boto3Storage(S3Boto3Storage):
#     location = 'static'
#     default_acl = 'public-read'
