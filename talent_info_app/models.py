from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=264,unique=True)
    orgnisation = models.CharField(max_length=264, default='Unknown')
    email = models.CharField(max_length=264, default='Unknown')
    skill = models.CharField(max_length=264, default='Unknown')
    skill_level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     name = models.CharField(max_length=264,unique=True)
#     url = models.URLField(unique=True)
#
#     def __str__(self):
#         return self.name
#
# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
#     date = models.DateField()
#
#     def __str__(self):
#         return str(self.date)
