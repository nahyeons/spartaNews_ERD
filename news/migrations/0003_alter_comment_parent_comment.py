# Generated by Django 4.2 on 2024-09-19 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_comment_parent_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="parent_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recommen",
                to="news.comment",
            ),
        ),
    ]
