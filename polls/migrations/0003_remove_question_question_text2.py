# Generated by Django 3.0.8 on 2020-07-15 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_text2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text2',
        ),
    ]
