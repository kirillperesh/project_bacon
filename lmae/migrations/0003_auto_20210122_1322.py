# Generated by Django 3.1.5 on 2021-01-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmae', '0002_auto_20210120_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('W', 'Female'), ('Mi-24', 'Attack Helicopter'), ('wtf', 'Not sure')], default='wtf', max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
