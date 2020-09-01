from django.db import models
# from datetime import date

class BlogPost(models.Model):
    code = models.CharField(max_length=30, null=True, blank=True)
    # issue_date = models.DateField(default=date.today)
    # delivery_date = models.DateField(null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return str(self.code)
