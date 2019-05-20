from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def summary(self):
        return self.content[:100]

    def date_format(self):
        return self.date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title
