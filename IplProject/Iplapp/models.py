from django.db import models

# Create your models here.
class Franchesis(models.Model):
    f_name = models.CharField(max_length=30)
    f_nickname = models.CharField(max_length=4)
    f_started_year = models.IntegerField()
    no_of_titles = models.IntegerField()
    f_logo = models.ImageField(upload_to='franchesis_logo/',blank=True,null=True)

    class Meta:
        db_table = 'franchesis'

    def __str__(self):
        return self.f_name

