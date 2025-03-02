# Generated by Django 4.2.19 on 2025-03-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.AddField(
            model_name='company',
            name='Company_about',
            field=models.TextField(default='good company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='Company_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='company',
            name='Company_type',
            field=models.CharField(choices=[('IT', 'IT'), ('Non - IT', 'Non - IT'), ('Networking', 'Networking')], default='IT', max_length=100),
            preserve_default=False,
        ),
    ]
