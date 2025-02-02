# Generated by Django 5.1.1 on 2024-10-20 03:11

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('descripcion', models.TextField(default='Sin descripción disponible')),
                ('imagen_seccion', models.ImageField(blank=True, default='default_image.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=200)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen_seccion', models.ImageField(blank=True, default='default_image.png', null=True, upload_to='')),
                ('imagen_detalle', models.ImageField(blank=True, null=True, upload_to='static/images/detalle_pics')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('horario_atencion', models.CharField(blank=True, max_length=100)),
                ('ubicacion', models.CharField(blank=True, max_length=255)),
                ('servicios', models.TextField(blank=True)),
                ('email_contacto', models.EmailField(blank=True, max_length=254)),
                ('telefono_contacto', models.CharField(blank=True, max_length=20)),
                ('link1', models.URLField(blank=True, null=True)),
                ('link1_title', models.CharField(blank=True, max_length=255, null=True)),
                ('link2', models.URLField(blank=True, null=True)),
                ('link2_title', models.CharField(blank=True, max_length=255, null=True)),
                ('categoria', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='post.category')),
            ],
        ),
    ]
