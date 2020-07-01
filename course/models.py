from django.db import models
from membership.models import Membership
from django.urls import reverse
class category(models.Model):
    name = models.TextField(max_length=50)


class language(models.Model):
    name = models.TextField(max_length=50)

    
class course(models.Model):
    slug=models.SlugField()
    title = models.CharField(max_length=20)
    Description = models.TextField(max_length=200)
    allowed_memberships = models.ManyToManyField(Membership)
    image  = models.ImageField(upload_to='videos/',null = True)
    Category = models.ForeignKey('category',on_delete=models.CASCADE)
    Language = models.ForeignKey('language',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course:detail', kwargs={'slug':self.slug})

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    slug=models.SlugField()
    title = models.CharField(max_length=120)
    Description = models.TextField(max_length=200)
    video_url = models.FileField(upload_to='videos/', null=True, verbose_name="")
    allowed_memberships = models.ForeignKey(Membership,on_delete=models.SET_NULL,null=True)
    base_course = models.ForeignKey(course,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course_thumbnail/',null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course:lesson-detail',
                       kwargs={
                           'course_slug': self.course.slug,
                           'lesson_slug': self.slug
                       })

