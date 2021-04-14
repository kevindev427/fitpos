# Generated by Django 3.1.2 on 2021-04-14 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_auto_20210402_1113'),
        ('accounts', '0002_auto_20210402_1114'),
        ('main', '0008_stats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.detail')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Stats',
        ),
    ]
