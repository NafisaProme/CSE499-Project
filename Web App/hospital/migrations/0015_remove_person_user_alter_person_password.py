# Generated by Django 4.0.5 on 2023-10-24 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_person_user_alter_person_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(default='123', max_length=100),
        ),
    ]