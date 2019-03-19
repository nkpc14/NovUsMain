# Generated by Django 2.1.4 on 2019-03-16 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rec_app', '0004_auto_20190316_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_block', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='recruitment',
            name='block',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rec_app.Block'),
        ),
    ]
