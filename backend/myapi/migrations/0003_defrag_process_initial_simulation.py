# Generated by Django 5.1.3 on 2024-12-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_utilizador_alter_defrag_process_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='defrag_process',
            name='initial_simulation',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
