# Generated by Django 3.0.8 on 2020-07-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_question_question_text2'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
