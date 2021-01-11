# Generated by Django 3.1.5 on 2021-01-11 11:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='jiraid',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Jira ID'),
        ),
    ]
