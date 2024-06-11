# Generated by Django 5.0.6 on 2024-06-09 21:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_content_alter_note_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 6, 9, 21, 5, 8, 805874, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
