from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
         return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT=0, 'draft'
        PUBLISHED=1, 'published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default='', unique=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Status")

    photo=models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, default=None, null=True)
    cat=models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
    tags=models.ManyToManyField('TagPost', blank='True', related_name='tags')
    husband=models.OneToOneField('Husband', on_delete=models.SET_NULL, null=True, blank=True, related_name='women')

    objects=models.Manager()
    published=PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Famous women'
        verbose_name_plural='Famous women'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

class Category(models.Model):
    name=models.CharField(max_length=255, db_index=True)
    slug=models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories '

class TagPost(models.Model):
    tag=models.CharField(max_length=255, db_index=True)
    slug=models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

class Husband(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    m_count=models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name

class UploadFiles(models.Model):
    file=models.FileField(upload_to='uploads_model')