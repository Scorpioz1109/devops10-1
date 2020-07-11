# Generated by Django 2.2 on 2020-07-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('staff_id', models.IntegerField(max_length=4, verbose_name='员工编号')),
                ('job_status', models.BooleanField(default=True, verbose_name='员工在职状态')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
                'db_table': 'user_profile',
            },
        ),
    ]