# Generated by Django 2.2.6 on 2020-02-23 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200220_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.AutoField(primary_key=True, serialize=False)),
                ('kategori', models.CharField(max_length=50)),
                ('deskripsi', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('id_kategori',),
            },
        ),
    ]
