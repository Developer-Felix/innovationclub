# Generated by Django 2.2.16 on 2020-11-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_community_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='category',
            field=models.CharField(blank=True, choices=[('Patron', 'Patron'), ('Chaiperson', 'Chairperson'), ('Vice-Chairperson', 'Vice-Charperson'), ('Secretary', 'Secretary'), ('Organizing Sec', 'Organizing Sec'), ('Treasurer', 'Treasurer'), ('Auditor', 'Auditor'), ('AI $ IoT team Lead', 'AI $ IoT team Lead'), ('Cyber Security Lead', 'Cyber Security Lead'), ('Opensource Comm Lead', 'Opensource Comm Lead'), ('Future comm lead', 'Future comm lead')], max_length=100),
        ),
    ]