# Generated by Django 3.0.8 on 2021-12-29 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelmanagement', '0007_auto_20211216_2229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parcelstatus',
            options={'ordering': ('-dateStatus', 'parcel_number')},
        ),
        migrations.AddField(
            model_name='parcelstatus',
            name='added',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parcelstatus',
            name='status_c',
            field=models.CharField(choices=[('01 : Nadano', '01 : Nadano'), ('02 : W drodze', '02 : W drodze'), ('03 : Uszkodzona', '03 : Uszkodzona'), ('04 : Zniszczona całkowicie', '04 : Zniszczona całkowicie'), ('05 : Dostarczona', '05 : Dostarczona'), ('06 : Błąd adresu', '06 : Błąd adresu'), ('07 : Pozostawiona w magazynie', '07 : Pozostawiona w magazynie'), ('08 : W trakcie wyjaśniania', '08 : W trakcie wyjaśniania'), ('09 : Przekierowana', '09 : Przekierowana')], max_length=300),
        ),
    ]
