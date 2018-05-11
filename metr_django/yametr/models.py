from django.db import models
from django.utils import timezone
import datetime
#MY_DATE_FORMATS = ['%d/%m/%Y',]

#python manage.py createsuperuser
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver


class Siteurl(models.Model):
    def __str__(self):
        return self.link
    link = models.URLField('Ссылка', max_length=200)
    def count_sum(self):
        #return self.link__zapros_value.aggregate(c=Sum('count'))['c']
        sum_count = Siteurl.objects.get(link=self.link)
        return sum_count.zaproshistory_set.count()



class Zapros(models.Model):
    def __str__(self):
        return self.zapros_name
    zapros_name = models.CharField(max_length=200)
    
class Pubdate(models.Model):
    def __str__(self):
        #return self.pub_date
        return self.pub_date.strftime('%d.%m.%Y')
    pub_date = models.DateField('Дата')
    

class Zaproshistory(models.Model):
#    def __str__(self):
#        return self.zapros_name
    link = models.ForeignKey(Siteurl, verbose_name='Ссылка', on_delete = models.CASCADE)  
    zapros_name = models.ForeignKey(Zapros, verbose_name='Запрос', on_delete = models.CASCADE)  # related_name="rates_from"
    zapros_value = models.IntegerField('Поиск.переходы')
    views_value = models.IntegerField('Просмотры')
    fastrun_value = models.IntegerField('Отказы')
    #pub_date = models.DateField('Дата')#,auto_now_add=True
    pub_date = models.ForeignKey(Pubdate, verbose_name='Дата', on_delete = models.CASCADE)
   # def was_published_recently(self):
   #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
   # def half_date(self):
    #    return self.pub_date.strftime('%m-%Y')#[:3]
    #half_date.short_description = 'month'   



class WordstatStat(models.Model):
#    link = models.ForeignKey(Siteurl, verbose_name='Ссылка', on_delete = models.CASCADE)  
    zapros_name = models.ForeignKey(Zapros, verbose_name='Запрос', on_delete = models.CASCADE)  # related_name="rates_from"
    pub_date = models.ForeignKey(Pubdate, on_delete = models.CASCADE)
    ws_stat_value = models.IntegerField('Статистика запросов', default=-1)
    ws_quotes_value = models.IntegerField('Запрос в кавычках', default=-1)
    from_history = models.BooleanField('Собрано из статистики', default=1)
    #ws_date = models.DateField('Дата')#,auto_now_add=True



#по сигналу сохранение "пресэйв"
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date
@receiver(pre_save, sender=MyClass)
def pre_save_query(sender, instance=None, **kwargs):
    if instance:
         instance.month = date(year=instance.date.year, month=instance.date.month, day=1)
         
суммарное значение я бы сделал на странице Sitelink, поле бы сделал методом или функцией, как-то так:
def count_sum(self):
     return self.zapros2link_set.aggregate(c=Sum('count'))['c']         
        
https://rtfm.co.ua/django-primer-sozdaniya-prilozheniya-chast-3-panel-upravleniya/
 change list pagination, search boxes, filters, date-hierarchies и column-header-ordering можно настроить вид админпанели так, как вы этого хотите.
        
        
         """
         