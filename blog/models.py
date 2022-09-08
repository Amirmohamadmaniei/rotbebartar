from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from user.models import ConsultantProfile, CustomUser


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    body = models.TextField(verbose_name='توضیحات مقاله')
    image = models.ImageField(upload_to='img/blog', verbose_name='عکس مقاله')
    author = models.ForeignKey(ConsultantProfile, on_delete=models.CASCADE, related_name='blogs',
                               verbose_name='نویسنده', null=True, blank=True)

    status = models.BooleanField(default=False, verbose_name='انتشار')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(blank=True, allow_unicode=True)

    ipaddress = models.ManyToManyField(IPAddress, blank=True, related_name='views', verbose_name='ادرس ای پی')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Blog, self).save(*args, **kwargs)


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')


# class BlogHits(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
