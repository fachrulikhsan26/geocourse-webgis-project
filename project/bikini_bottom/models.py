#from django.db import models #Model database non spasial
from django.contrib.gis.db import models # Model database spasial
from django.contrib.auth.models import User

# Create your models here.
class Facility(models.Model):
    
    TYPE_CHOICES = [
        ('government', 'Pemerintahan'),
        ('public', 'Fasilitas Umum'),
        ('park', 'Taman'),
        ('restaurant', 'Restoran'),
        ('house', 'Rumah')
    ]

    STATUS_CHOICES = [
        ('proposed', 'Proposed'),
        ('under_review', 'Under Review'),
        ('planned', 'Planned'),
        ('construction', 'Under Construction'),
        ('completed', 'Completed')
    ]

    PRICES_CHOICES = [
        ('hourly', 'Per Jam'),
        ('daily', 'Per Hari'),
        ('weekly', 'Per Minggu'),
        ('monthly', 'Per Bulan'),
        ('annual', 'Per Tahun')
    ]

    name = models.CharField(max_length=50)
    types = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='proposed')
    open = models.BooleanField(default=False)
    location = models.PointField(srid=4326, spatial_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=15, choices=PRICES_CHOICES)
    photo = models.ImageField(upload_to='facility')
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    