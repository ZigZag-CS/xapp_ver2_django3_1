# Generated by Django 3.0.8 on 2020-07-09 17:37

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='no_image_app_content.png', null=True, upload_to='client/', verbose_name='Avatar'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_traider',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
