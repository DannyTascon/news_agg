from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    published_date = models.DateTimeField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


