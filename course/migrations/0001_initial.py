# Generated by Django 3.0.6 on 2020-05-30 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=20)),
                ('Description', models.TextField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='videos/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.category')),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('Description', models.TextField(max_length=200)),
                ('video_url', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('image', models.ImageField(null=True, upload_to='course_thumbnail/')),
                ('allowed_memberships', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='membership.Membership')),
                ('base_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.language'),
        ),
        migrations.AddField(
            model_name='course',
            name='allowed_memberships',
            field=models.ManyToManyField(to='membership.Membership'),
        ),
    ]