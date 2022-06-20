from django.db import models

# Create your models here.

class Advertise(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان آگهی')
    price = models.CharField(max_length=100, verbose_name='قیمت')
    description = models.CharField(max_length=300, verbose_name='قیمت')
    advertise_url = models.URLField(verbose_name='لینک', null=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')
    slug = models.SlugField(default='', db_index=True, blank=True, verbose_name='عنوان در url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'آگهی'
        verbose_name_plural = 'آگهی ها'