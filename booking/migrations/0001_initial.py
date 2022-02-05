# Generated by Django 3.2.12 on 2022-02-05 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_num', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.DateField()),
                ('time', models.DateTimeField()),
                ('table_count', models.IntegerField(default=0)),
                ('visit_status', models.CharField(max_length=1)),
                ('method', models.CharField(max_length=1)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('shop_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
        ),
    ]
