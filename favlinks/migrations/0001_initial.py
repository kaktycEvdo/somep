# Generated by Django 3.1.7 on 2021-03-30 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=150)),
                ('typel', models.IntegerField(default=1)),
                ('image', models.ImageField(height_field=300, upload_to='', width_field=400)),
                ('icon', models.ImageField(height_field=40, upload_to='', width_field=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favlinks.user')),
            ],
        ),
    ]
