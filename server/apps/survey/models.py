from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    questions = models.ManyToManyField('Question', null=True, blank=True)

    def __str__(self):
        return "%s" % self.name


QUESTION_TYPE_CHOICES = (
    ('text', 'Text'),
    ('textarea', 'Text Area'),
    ('single-select', 'Single Select'),
    ('multi-select', 'Multi Select'),
    ('location', 'Location'),
)

class Option(models.Model):
    text = models.CharField(max_length=254)
    label = models.SlugField(max_length=64) 
   
    def __str__(self):
        return "%s" % self.text

class Question(models.Model):
    title = models.TextField()
    label = models.CharField(max_length=254)
    slug = models.SlugField(max_length=64)
    type = models.CharField(max_length=20,choices=QUESTION_TYPE_CHOICES,default='text')
    options = models.ManyToManyField(Option, null=True, blank=True)

    def __str__(self):
        return "%s" % self.label