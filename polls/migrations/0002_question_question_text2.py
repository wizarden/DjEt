# Generated by Django 3.0.8 on 2020-07-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
