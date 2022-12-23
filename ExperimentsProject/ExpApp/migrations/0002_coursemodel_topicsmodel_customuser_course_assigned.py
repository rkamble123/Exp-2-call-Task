# Generated by Django 4.1.4 on 2022-12-23 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExpApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopicsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('topic_url', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExpApp.coursemodel')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='course_assigned',
            field=models.ManyToManyField(blank=True, to='ExpApp.coursemodel'),
        ),
    ]
