# Generated by Django 2.0.7 on 2018-07-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20180728_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
