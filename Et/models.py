from django.db import models


class Choices(models.Model):
       description = models.CharField(max_length=300)

class Profile(models.Model):
      #user = models.ForeignKey(Choices, blank=True, unique=True, verbose_name='user')
      the_choices = models.ManyToManyField(Choices)



# class Harak(models.Model):
#     color_cod       = models.CharField(max_length=4, default='9999', verbose_name='Код')
#     color_name      = models.CharField(max_length=100, default='Название', verbose_name='Цвет')
#     color_des       = models.CharField(max_length=100, default='', verbose_name='Примечание', blank=True)

#     class Meta:
#         ordering = ['color_name']
#         verbose_name = 'Свойства'
#         verbose_name_plural = 'Свойства'

#     def __str__(self):
#         return self.color_cod + ' ' + self.color_name 


# class Izd(models.Model):
#     izd_cod      = models.CharField(max_length=4, default='9999', verbose_name='Код')
#     izd_name     = models.CharField(max_length=100, default='Название', verbose_name='Номенклатура')
#     izd_des      = models.CharField(max_length=100, default='', verbose_name='Примечание', blank=True)
#     izd_col_upak = models.IntegerField(default=1, verbose_name='Кол-во упаковок')

    
  



#     class Meta:
#         ordering = ['izd_name']
#         verbose_name = 'Номенклатура'
#         verbose_name_plural = 'Номенклатура'

#     def __str__(self):
#         return self.izd_name


# class Upak(models.Model):
#     pass
#     num     = models.CharField(max_length=4, default='1', verbose_name='Номер')
#     tip     = models.CharField(max_length=4, default='ST', verbose_name='Тип')    
#     haraks  = models.ForeignKey(Harak, on_delete=models.CASCADE, verbose_name='Свойства')
#     izds    = models.ForeignKey(Izd, on_delete=models.CASCADE, verbose_name='Номенклатура')

#     class Meta:
#         ordering = ['num']
#         verbose_name = 'Упаковки'
#         verbose_name_plural = 'Упаковки'

#     def __str__(self):
#         return self.num







    

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)