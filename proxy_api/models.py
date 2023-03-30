from django.db import models
from .ultis import generate_key
import os
from dotenv import load_dotenv
load_dotenv('.env')

secrect_key = os.environ['SECRECT_KEY']
salt_text = bytes(os.environ['SALT_STRING'].encode('utf-8'))
iterations = 100000
cipher = generate_key(secrect_key, salt_text, iterations)
# Create your models here.

class HostDomain(models.Model):
    name = models.CharField(unique=True, max_length=255)
    def __str__(self) -> str:
        return self.name
    

class KeyToken(models.Model):
    hostdomain = models.ForeignKey(HostDomain, on_delete=models.CASCADE, blank=False, to_field='name')
    api_key = models.TextField(unique=True)
    access_token = models.TextField(editable=False)

    def __str__(self) -> str:
        return 'API_KEY_'+self.hostdomain.name

    def save(self, *args, **kwargs):
        self.access_token = cipher.encrypt(self.api_key.encode())
        return super().save(*args, **kwargs)
    
