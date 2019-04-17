# Generated by Django 2.1.5 on 2019-04-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20190413_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_page_begin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_page_end',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='abstract',
            field=models.TextField(blank=True, help_text='You can enter the abstract later if you prefer.', null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pub_type',
            field=models.CharField(choices=[('A', 'Journal Article'), ('B', 'Book'), ('C', 'Book Chapter'), ('D', 'Dissertation'), ('O', 'Other Publication Type'), ('P', 'Presensation (Conference Talk, Course Lecture, etc.'), ('S', 'Student Work (Other than Dissertation'), ('W', 'Web Publication (Blog, etc.)')], max_length=1),
        ),
    ]