# Generated by Django 5.0 on 2023-12-13 19:47

import ckeditor.fields
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('create_day', models.DateField(auto_now_add=True)),
                ('create_time', models.TimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('create_day', models.DateField(auto_now_add=True)),
                ('create_time', models.TimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Taglar',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('create_day', models.DateField(auto_now_add=True)),
                ('create_time', models.TimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='news')),
                ('video', models.FileField(upload_to='news_video')),
                ('view_count', models.BigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='home.tags')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
