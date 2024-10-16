# Generated by Django 4.2.16 on 2024-10-13 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('social_media', 'Social Media Post'), ('blog', 'Blog Post'), ('product_description', 'Product Description')], max_length=50)),
                ('prompt', models.TextField()),
                ('generated_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
