# Generated by Django 2.0.2 on 2018-02-12 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('risk_types', '0002_risktype_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('risk_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_types.RiskType')),
            ],
        ),
    ]
