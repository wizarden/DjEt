from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_text2 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    mylist = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','5'),
    )
    ml = models.CharField(max_length=200,choices=mylist)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)