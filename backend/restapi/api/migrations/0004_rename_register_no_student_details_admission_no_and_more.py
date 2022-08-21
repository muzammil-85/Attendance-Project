# Generated by Django 4.1 on 2022-08-21 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_student_details_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_details',
            old_name='register_no',
            new_name='admission_no',
        ),
        migrations.RemoveField(
            model_name='student_attendance',
            name='register_no',
        ),
        migrations.AddField(
            model_name='student_attendance',
            name='admission_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.student_details'),
        ),
        migrations.AddField(
            model_name='student_attendance',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.teacher_details'),
        ),
        migrations.CreateModel(
            name='SubjectTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.teacher_details')),
            ],
        ),
    ]