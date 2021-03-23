# Generated by Django 3.1.7 on 2021-03-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_cause_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('dob', models.DateTimeField(blank=True)),
                ('amount', models.BigIntegerField()),
                ('accountno', models.BigIntegerField()),
            ],
        ),
    ]
