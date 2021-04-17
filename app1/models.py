from django.db import models

# Create your models here.
class Ques(models.Model):
	symbol = models.CharField(max_length=200, null=True, blank=True)
	date = models.DateField(null=True, blank=True)
	open1 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
	high = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
	low = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
	close = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
	vol = models.IntegerField(null=True, blank=True)
	adj = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)

	
	

	def __str__(self):
		return self.symbol


