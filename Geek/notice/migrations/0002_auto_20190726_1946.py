# Generated by Django 2.2.3 on 2019-07-26 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='Notice_text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='pub_date',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='Notice_name',
            new_name='title',
        ),
    ]