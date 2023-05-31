# Generated by Django 4.2 on 2023-05-31 18:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='نام')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='نام')),
                ('correspondence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='places', to=settings.AUTH_USER_MODEL, verbose_name='مسئول')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='نام')),
                ('last_name', models.CharField(max_length=64, verbose_name='نشان')),
                ('organization_id', models.CharField(max_length=12, verbose_name='شماره کارگزینی')),
                ('rank', models.PositiveSmallIntegerField(choices=[(7, 'ستوانسوم'), (8, 'ستواندوم'), (9, 'ستوانیکم'), (10, 'سرگرد'), (11, 'سرهنگ 2'), (12, 'سرهنگ تمام'), (13, 'سرتیپ 2'), (14, 'سرتیپ')], default=9, verbose_name='درجه')),
                ('monthly_mandatory_serve_time_hours', models.PositiveIntegerField(blank=True, null=True, verbose_name='ساعات خدمت موظف ماهیانه')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='core.major', verbose_name='تخصص')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='زمان تغییر')),
                ('time_step', models.PositiveSmallIntegerField(choices=[(0, 'روزانه'), (1, 'هفتگی'), (2, 'ماهانه')], default=2, verbose_name='بازه زمانی')),
                ('subject_rank', models.PositiveSmallIntegerField(choices=[(7, 'ستوانسوم'), (8, 'ستواندوم'), (9, 'ستوانیکم'), (10, 'سرگرد'), (11, 'سرهنگ 2'), (12, 'سرهنگ تمام'), (13, 'سرتیپ 2'), (14, 'سرتیپ')], default=9, verbose_name='درجه')),
                ('outpatient_visit_counts', models.PositiveSmallIntegerField(default=0, verbose_name='تعداد ویزیت سرپایی بیمار')),
                ('hospitalized_patients_counts', models.PositiveSmallIntegerField(default=0, verbose_name='تعداد بیمار بستری شده')),
                ('total_served_time', models.TimeField(default=datetime.time(0, 0), verbose_name='مجموع ساعات خدمت')),
                ('additive_served_time', models.TimeField(default=datetime.time(0, 0), verbose_name='مجموع ساعات اضافه کاری')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='core.subject', verbose_name='شخص')),
                ('subject_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='core.place', verbose_name='محل خدمت')),
            ],
        ),
    ]