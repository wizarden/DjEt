# Generated by Django 3.0.8 on 2020-07-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Et', '0007_auto_20200717_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_choices', models.ManyToManyField(to='Et.Choices')),
            ],
        ),
        migrations.DeleteModel(
            name='Harak',
        ),
        migrations.DeleteModel(
            name='Izd',
        ),
        migrations.DeleteModel(
            name='Upak',
        ),
    ]
