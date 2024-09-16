from django.db import models

class Property(models.Model):
    STATUS_CHOICES = [
        ('for_sale', 'For Sale'),
        ('for_rent', 'For Rent'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
        ('co_living', 'Co-living'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='properties/', null=True, blank=True)
    added_date = models.DateField(auto_now_add=True, null=True, blank=True)  # Automatically sets date on creation
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='for_sale')
    square_footage = models.PositiveIntegerField()
    number_of_bedrooms = models.PositiveIntegerField()
    number_of_bathrooms = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title
