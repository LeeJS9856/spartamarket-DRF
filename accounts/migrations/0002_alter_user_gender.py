# Generated by Django 4.2 on 2024-04-27 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '남자'), ('F', '여자')], max_length=1, null=True),
        ),
    ]