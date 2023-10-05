# Generated by Django 4.2.5 on 2023-10-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=30)),
                ('productImage', models.ImageField(default='', upload_to='static/images/')),
            ],
        ),
    ]