# Generated by Django 4.2.5 on 2023-09-15 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='pbrand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='pname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='pprice',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='pstock',
            new_name='stock',
        ),
    ]