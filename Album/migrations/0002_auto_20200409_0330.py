# Generated by Django 3.0.5 on 2020-04-09 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='Artist',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Catalogue_Number',
            new_name='catalogue_number',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Cover_Image',
            new_name='cover_image',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Label',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='Year',
            new_name='year',
        ),
    ]
