from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField()
    code = models.CharField(max_length=5, unique=True, blank=True, null=True, validators=[RegexValidator(regex="[a-z][a-z][0-9][0-9][en]", message="Company code not in correct format.")])
    strength = models.IntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.code}"
    
