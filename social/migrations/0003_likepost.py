# Generated by Django 5.0.6 on 2024-06-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
