# Generated by Django 2.2.6 on 2020-02-20 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_gambar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('id_article',)},
        ),
    ]
