from django.db import models

# Create your models here.
class Diary(models.Model):
    Entry = models.TextField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
            return self.Entry

    class Meta:
        verbose_name_plural = 'Diary_Entries'