# Generated by Django 2.1.4 on 2018-12-28 07:25

from django.db import migrations, models
import django.db.models.deletion
import macaddress.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listele', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='birim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ip',
            fields=[
                ('tarih', models.DateTimeField(verbose_name='date published')),
                ('ip', models.GenericIPAddressField(db_index=True, primary_key=True, serialize=False)),
                ('eposta', models.CharField(max_length=50)),
                ('aciklama', models.CharField(max_length=250)),
                ('mac', macaddress.fields.MACAddressField(blank=True, integer=False, max_length=17)),
                ('kisisel', models.BooleanField(default=False)),
                ('elle_binding', models.BooleanField(default=False)),
                ('kablosuz', models.BooleanField(default=False)),
                ('aktif', models.BooleanField(default=True)),
                ('birim', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listele.birim')),
            ],
        ),
        migrations.RemoveField(
            model_name='ipler',
            name='birim',
        ),
        migrations.DeleteModel(
            name='birimler',
        ),
        migrations.DeleteModel(
            name='ipler',
        ),
    ]
