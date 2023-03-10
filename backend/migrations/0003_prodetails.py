# Generated by Django 4.0.3 on 2022-12-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_categorysave'),
    ]

    operations = [
        migrations.CreateModel(
            name='proDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]
