# Generated by Django 3.1.5 on 2021-01-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0003_auto_20210111_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]