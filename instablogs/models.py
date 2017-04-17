from django.db import models

# Create your models here.
class Topic(models.Model):
    """ the topic of each blog """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ return text """
        return self.text

class Entry(models.Model):
    """ the post of specific topic """
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ return text """
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text