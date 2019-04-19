# Generated by Django 2.1.7 on 2019-04-02 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ToppingAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(choices=[(1, 'Regular'), (2, 'Double'), (3, 'Triple')], default=1)),
                ('pizza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topping_amounts', to='pizzas.Pizza')),
                ('topping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topping_amounts', to='pizzas.Topping')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(related_name='pizzas', through='pizzas.ToppingAmount', to='pizzas.Topping'),
        ),
    ]
