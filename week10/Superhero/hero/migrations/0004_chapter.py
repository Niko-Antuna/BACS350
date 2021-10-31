# Generated by Django 3.2.6 on 2021-10-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_auto_20211002_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(default='Default', max_length=200)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('markdown', models.TextField()),
                ('html', models.TextField()),
                ('document', models.CharField(max_length=200)),
            ],
        ),
    ]
