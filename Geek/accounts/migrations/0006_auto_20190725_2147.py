# Generated by Django 2.1.5 on 2019-07-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190725_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='is_freshman',
            field=models.NullBooleanField(verbose_name='是否为本校新生'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='is_school',
            field=models.NullBooleanField(verbose_name='是否为本校学生'),
        ),
    ]