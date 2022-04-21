# Generated by Django 4.0.4 on 2022-04-16 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appstatico', '0003_profile_alter_demanda_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demanda',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
