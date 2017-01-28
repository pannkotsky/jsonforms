from __future__ import unicode_literals

from django.db import models

from jsonfield import fields as json_fields


class Posting(models.Model):
    title = models.CharField(max_length=100)
    context = json_fields.TypedJSONField()
