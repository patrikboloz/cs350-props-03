# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models

class Property(models.Model):
    prop_type = models.CharField(max_length=96)
    address = models.CharField(max_length=512, null=True)
    zip_code = models.IntegerField(null=True)
    description = models.TextField()
    picture_url = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=3, max_digits=10)   

    def __str__(self):
        return self.prop_type + ' @ ' + self.address



