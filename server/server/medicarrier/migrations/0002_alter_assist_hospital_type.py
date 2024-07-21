# Generated by Django 5.0.7 on 2024-07-21 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicarrier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assist',
            name='hospital_type',
            field=models.CharField(choices=[('내과', '내과'), ('외과', '외과'), ('정형외과', '정형외과'), ('이비인후과', '이비인후과'), ('응급실', '응급실'), ('산부인과', '산부인과'), ('피부과', '피부과'), ('치과', '치과'), ('안과', '안과'), ('비뇨기과', '비뇨기과'), ('신경외과', '신경외과'), ('항문외과', '항문외과'), ('성형외과', '성형외과'), ('정신건강의학과', '정신건강의학과')], default='내과', max_length=20),
        ),
    ]
