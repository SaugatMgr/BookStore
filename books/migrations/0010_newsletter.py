# Generated by Django 4.2.1 on 2023-05-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_contact_rename_message_comment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
