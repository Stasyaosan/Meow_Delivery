# Generated by Django 5.0.6 on 2024-05-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_meow', '0003_alter_user_login_alter_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.TextField(blank=True, null=True),
        ),
    ]