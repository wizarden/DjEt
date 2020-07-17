from django.db import models

class Harak(models.Model):
    color_cod       = models.CharField(max_length=4, default='9999')
    color_name      = models.CharField(max_length=100, default='Название')
    color_des       = models.CharField(max_length=100, default='')
    

    class Meta:
        ordering = ['color_name']

    def __str__(self):
        return self.color_name
        
class Izd(models.Model):
    izd_cod       = models.CharField(max_length=4, default='9999')
    izd_name      = models.CharField(max_length=100, default='Название')
    izd_des       = models.CharField(max_length=100, default='')
    haraks = models.ManyToManyField(Harak)

    class Meta:
        ordering = ['izd_name']

    def __str__(self):
        return self.izd_name



    

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)