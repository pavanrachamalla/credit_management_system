# Generated by Django 3.0.8 on 2020-09-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20200916_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tran',
            old_name='name',
            new_name='r_name',
        ),
        migrations.RenameField(
            model_name='tran',
            old_name='credit',
            new_name='t_credit',
        ),
        migrations.AddField(
            model_name='tran',
            name='s_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]