# Generated by Django 4.2 on 2023-06-01 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_delete_patient'),
        ('employees', '0002_delete_employee'),
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='allergies',
            field=models.ManyToManyField(blank=True, null=True, to='patients.allergy'),
        ),
        migrations.AddField(
            model_name='user',
            name='employed_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='employee_image',
            field=models.ImageField(blank=True, null=True, upload_to='employees/'),
        ),
        migrations.AddField(
            model_name='user',
            name='pesel',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=123456789, max_length=11, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.role'),
        ),
        migrations.AddField(
            model_name='user',
            name='specialization',
            field=models.CharField(blank=True, choices=[('Lekarz rodzinny', 'Family Doctor'), ('Pediatra', 'Pediatrician'), ('Dermatolog', 'Dermatologist'), ('Chirurg', 'Surgeon'), ('Stomatolog', 'Dentist'), ('Ortopeda', 'Orthopaedist'), ('Internista', 'Internist')], default='', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='title_of_degree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.degree'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_receptionist',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
