# Generated by Django 4.1 on 2022-08-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_mailing_messagemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField()),
                ('codmail', models.IntegerField()),
                ('tagmail', models.IntegerField()),
                ('timezoneclient', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='mailing',
            name='tagmail',
            field=models.TextField(),
        ),
    ]