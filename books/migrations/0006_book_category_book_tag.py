# Generated by Django 4.2.1 on 2023-05-24 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_rename_category_category_name_rename_tag_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='books.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(to='books.tag'),
        ),
    ]
