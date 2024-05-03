# Generated by Django 4.2.3 on 2023-10-10 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0017_remove_reserva_servicios_reserva_servicios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='codigo',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='servicios',
        ),
        migrations.CreateModel(
            name='ReservaServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.reserva')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.servicio')),
            ],
        ),
    ]