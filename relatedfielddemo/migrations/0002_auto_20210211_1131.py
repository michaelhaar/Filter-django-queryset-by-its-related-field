# Generated by Django 3.1.6 on 2021-02-11 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relatedfielddemo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatedfielddemo.questionset'),
        ),
    ]
