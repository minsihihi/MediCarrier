# Generated by Django 5.0.7 on 2024-07-21 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicarrier', '0004_remove_hospital_assist_assist_recommended_hospitals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assist',
            name='facility',
            field=models.CharField(choices=[('약국', '약국'), ('병원', '병원')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='assist',
            name='hospital_type',
            field=models.CharField(choices=[('내과', '내과'), ('외과', '외과'), ('정형외과', '정형외과'), ('이비인후과', '이비인후과'), ('응급실', '응급실'), ('산부인과', '산부인과'), ('피부과', '피부과'), ('치과', '치과'), ('안과', '안과'), ('비뇨기과', '비뇨기과'), ('신경외과', '신경외과'), ('항문외과', '항문외과'), ('성형외과', '성형외과'), ('정신건강의학과', '정신건강의학과')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='assist',
            name='symptom_type',
            field=models.CharField(choices=[('콧물이 나요', '콧물이 나요'), ('열이 나요', '열이 나요'), ('인후통이 있어요', '인후통이 있어요'), ('귀가 아파요', '귀가 아파요'), ('기침을 해요', '기침을 해요')], default='', max_length=20),
        ),
    ]
