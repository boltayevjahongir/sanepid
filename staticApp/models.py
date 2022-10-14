from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Menutext(models.Model):
    name = models.CharField(null=True, max_length=100)
    content = RichTextUploadingField(null=True,
                                     extra_plugins=['youtube'],
                                     external_plugin_resources=[(
                                         'youtube',

                                         '/static/ckeditor/ckeditor/plugins/youtube/',
                                         'plugin.js',
                                     )],
                                     )
