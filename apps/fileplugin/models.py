import os

from django.core.files.storage import default_storage
from cms.plugins.file.models import File as CMSFile


class File(CMSFile):
    """
    Extend top make file work with S3
    """
    def file_exists(self):
        return default_storage.exists(self.file.name)

    def get_file_name(self):
        return os.path.basename(self.file.name)

    class Meta:
        proxy = True
