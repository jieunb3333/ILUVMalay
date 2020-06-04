# Generated by Django 3.0.6 on 2020-05-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/%Y/%m/%d')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]