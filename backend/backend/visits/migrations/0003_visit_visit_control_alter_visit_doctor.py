# Generated by Django 4.2 on 2023-06-07 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visits', '0002_alter_visit_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='visit_control',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='visits_doctor', to=settings.AUTH_USER_MODEL),
        ),
    ]
