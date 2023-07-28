# Generated by Django 4.2.3 on 2023-07-27 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('effect', models.CharField(choices=[('M', 'Monster'), ('S', 'Spell'), ('T', 'Trap')], default='M', max_length=1)),
                ('yugioh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.yugioh')),
            ],
        ),
    ]