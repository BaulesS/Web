# Generated by Django 4.1.1 on 2022-09-19 03:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Anime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(blank=True, null=True, upload_to="anime"),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("role", models.CharField(blank=True, max_length=200, null=True)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Anime",
                "verbose_name_plural": "Animes",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("author", models.CharField(blank=True, max_length=200, null=True)),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("body", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="blog")),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Blog",
                "verbose_name_plural": "Blogs",
                "ordering": ["timestamp"],
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("author", models.CharField(blank=True, max_length=200, null=True)),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("body", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="review")),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Review",
                "verbose_name_plural": "Reviews",
                "ordering": ["timestamp"],
            },
        ),
    ]