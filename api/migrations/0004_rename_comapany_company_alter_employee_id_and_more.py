# Generated by Django 4.1.4 on 2022-12-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comapany',
            new_name='Company',
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]