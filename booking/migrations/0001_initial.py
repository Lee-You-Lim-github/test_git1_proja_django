# Generated by Django 3.2.12 on 2022-02-08 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('time', models.DateTimeField()),
                ('table_count', models.IntegerField(default=0)),
                ('visit_status', models.CharField(max_length=1)),
                ('method', models.CharField(max_length=1)),
                ('shop_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
