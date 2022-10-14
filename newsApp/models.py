from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=250, null=True)
    img = models.ImageField(null=True)
    date = models.DateField(null=True, auto_now_add=True)
    shortText = models.CharField(max_length=250, null=True)
    content = RichTextUploadingField(null=True,
                                     extra_plugins=['youtube'],
                                     external_plugin_resources=[(
                                         'youtube',

                                         '/static/ckeditor/ckeditor/plugins/youtube/',
                                         'plugin.js',
                                     )],
                                     )

    def __str__(self):
        return self.title
