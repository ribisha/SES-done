# Generated by Django 4.1 on 2023-05-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_studentapplication_contact_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentapplication',
            name='relationship_of_guardian',
            field=models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Step Guardian', 'Step Guardian'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Other', 'Other')], default='', max_length=200),
        ),
    ]