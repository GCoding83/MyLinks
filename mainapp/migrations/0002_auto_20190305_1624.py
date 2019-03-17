# Generated by Django 2.1.5 on 2019-03-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, help_text='If author only has one name (e.g. Aristotle), enter it as a last name', max_length=30, null=True),
        ),
    ]
