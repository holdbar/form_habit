# Generated by Django 2.0.6 on 2018-07-08 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterUniqueTogether(
            name='habit',
            unique_together={('name', 'owner')},
        ),
    ]
