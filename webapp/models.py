from django.db import models

# Create your models here.

# Create your models here.
class Images(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(upload_to="video/%y")
	def __str__(self):
		return self.caption