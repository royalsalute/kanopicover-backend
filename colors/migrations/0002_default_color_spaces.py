# Generated by Django 3.2.7 on 2021-10-04 07:52

from django.db import migrations, models, transaction, IntegrityError
import django.db.models.deletion


def add_default_color_spaces(apps, schema_editor):
    ColorSpace = apps.get_model('colors', 'ColorSpace')
    ColorSpaceField = apps.get_model('colors', 'ColorSpaceField')

    data = [
        {
            'name': 'rgb',
            'fields': [
                {
                    'name': 'red',
                    'min_value': 0,
                    'max_value': 255,
                },
                {
                    'name': 'green',
                    'min_value': 0,
                    'max_value': 255,
                },
                {
                    'name': 'blue',
                    'min_value': 0,
                    'max_value': 255,
                }
            ]
        },
        {
            'name': 'hsl',
            'fields': [
                {
                    'name': 'hue',
                    'min_value': 0,
                    'max_value': 360,
                },
                {
                    'name': 'saturation',
                    'min_value': 0,
                    'max_value': 100,
                },
                {
                    'name': 'lightness',
                    'min_value': 0,
                    'max_value': 100,
                }
            ]
        }
    ]

    for _space in data:
        try:
            with transaction.atomic():
                space = ColorSpace.objects.create(name=_space['name'])
            for _field in _space['fields']:
                with transaction.atomic():
                    ColorSpaceField.objects.create(name=_field['name'], min_value=_field['min_value'], max_value=_field['max_value'], space_id=space.id)
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('colors', '0001_initial')
    ]

    operations = [
        migrations.RunPython(add_default_color_spaces)
    ]
