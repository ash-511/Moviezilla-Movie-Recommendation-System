# Generated by Django 3.1.7 on 2021-04-09 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0008_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('drama', models.BooleanField(default=False, null=True)),
                ('thriller', models.BooleanField(default=False, null=True)),
                ('action', models.BooleanField(default=False, null=True)),
                ('comedy', models.BooleanField(default=False, null=True)),
                ('romance', models.BooleanField(default=False, null=True)),
                ('adventure', models.BooleanField(default=False, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
