# Generated by Django 3.1.7 on 2021-03-17 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
            },
        ),
    ]