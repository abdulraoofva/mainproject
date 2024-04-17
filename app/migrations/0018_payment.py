# Generated by Django 4.2.6 on 2024-03-20 03:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_checkout_checkoutitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('accessory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.caraccessory')),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.checkout')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]