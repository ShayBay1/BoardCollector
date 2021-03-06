# Generated by Django 4.0.4 on 2022-04-28 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_bindings_board_bindings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bindings',
            new_name='Binding',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.board')),
            ],
        ),
    ]
