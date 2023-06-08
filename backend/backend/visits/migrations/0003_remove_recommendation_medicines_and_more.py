# Generated by Django 4.2 on 2023-06-07 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visits', '0002_alter_visit_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='medicines',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='recommendation',
        ),
        migrations.AddField(
            model_name='medicine',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medicines', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='visit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='visits.visit'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recommendations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='visits_doctor', to=settings.AUTH_USER_MODEL),
        ),
    ]
