# Generated by Django 4.2.2 on 2023-09-22 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designcrafter', '0004_auto_20230920_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='id',
            field=models.IntegerField(null=True),
        ),
    ]