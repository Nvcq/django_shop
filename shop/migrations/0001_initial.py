# Generated by Django 4.0.3 on 2022-03-03 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
