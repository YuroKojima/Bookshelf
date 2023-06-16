from django.db import models

CATEGORY = (('business','ビジネス'),('life','生活'),('entartainment','娯楽'),('other','その他'))

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
    )
    purchase=models.CharField(max_length=10000, null=True)
    
    def __str__(self):
        return self.title