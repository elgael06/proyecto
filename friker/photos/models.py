from django.db import models

# Create your models here.


COPYRIGHT = 'RIG'
COPYLEFT = 'LEFT'
CREATE_COMMONS = 'C_C'

LICENSES = {
    (COPYRIGHT, 'COPYRIGHT'),
    (COPYLEFT, 'COPYLEFT'),
    (CREATE_COMMONS, 'CREATE_COMMONS'),
}


class Photo(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, default="")
    date = models.DateField(auto_now_add=True)
    date_mod = models.DateField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)
