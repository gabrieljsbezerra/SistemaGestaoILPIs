# Generated by Django 4.2.4 on 2025-05-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("estoque", "0002_imagem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="imagem", old_name="produto", new_name="remedio",
        ),
        migrations.AlterField(
            model_name="imagem",
            name="imagem",
            field=models.ImageField(upload_to="imagem_remedio"),
        ),
    ]
