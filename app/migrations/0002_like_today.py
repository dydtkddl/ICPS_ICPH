# Generated by Django 4.1.1 on 2023-05-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="like",
            name="today",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
