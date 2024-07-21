# Generated by Django 5.0.7 on 2024-07-20 14:39
# Generated by Django 5.0.7 on 2024-07-20 14:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MediCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(max_length=20)),
                ('hospital_type', models.CharField(max_length=20)),
                ('symptom_type', models.CharField(max_length=20)),
                ('symptom_etc', models.CharField(max_length=20)),
                ('illness_etc', models.CharField(max_length=20)),
                ('medicine_etc', models.CharField(max_length=20)),
                ('etc', models.CharField(max_length=20)),
                ('ins_req1', models.CharField(max_length=20)),
                ('ins_req2', models.CharField(max_length=20)),
                ('hospital_fee', models.CharField(max_length=20)),
                ('document', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('medicard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='medicarrier.medicard')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('name_eng', models.CharField(max_length=20)),
                ('birthdate', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=20)),
                ('weight', models.CharField(max_length=20)),
                ('bloodtype', models.CharField(max_length=20)),
                ('pregnant', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MediInfo',
            fields=[
                ('medicard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='medicarrier.medicard')),
                ('condition', models.CharField(default='현재 증상 없음', max_length=20)),
                ('illness', models.CharField(default='없음', max_length=20)),
                ('medicine', models.CharField(default='복용하는 약 없음', max_length=20)),
                ('allergy', models.CharField(default='알레르기 없음', max_length=20)),
                ('diagnosis', models.CharField(default='근 n개월 이내 없음', max_length=20)),
                ('surgery', models.CharField(default='근 n개월 이내 없음', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=20)),
                ('hospital_category', models.CharField(max_length=20)),
                ('hospital_tel', models.IntegerField()),
                ('hospital_ratings', models.CharField(max_length=20)),
                ('hospital_open', models.BooleanField()),
                ('assist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicarrier.assist')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_type', models.CharField(max_length=20)),
                ('insturance_name', models.CharField(max_length=20)),
                ('insurance_call', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='medicard',
            name='country',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medicarrier.trip'),
        ),
    ]
