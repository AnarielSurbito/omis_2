from django.db import models

class Exponents(models.Model):
    name = models.CharField(max_length=50)
    name_of_company = models.CharField(max_length=100)
    price = models.IntegerField()
    desription = models.CharField(max_length=5000)
    image_of_exp1 = models.ImageField(upload_to='img/', blank=True)
    my_exp = models.BooleanField(default=False)



class Event(models.Model):
    #created_at = models.DateTimeField(auto_now_add=True)
    #id_of_event = models.IntegerField()
    name = models.CharField(max_length=100)
    data_begin = models.DateField()
    data_end = models.DateField()
    image_of_event = models.ImageField(upload_to='img/', blank=True)
    description = models.CharField(max_length=5000)
    exp = models.ManyToManyField("Exponents")
    my_eve = models.BooleanField()

# upload_to='img/'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    #def __str__(self):
        # if self == Event or self == Exponents:
        #     return(f"{self.Ename}")
        # else:
    #    return (f"{self.name}")

