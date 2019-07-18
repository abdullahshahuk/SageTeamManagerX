# Generated by Django 2.2.3 on 2019-07-13 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamXapp', '0051_auto_20190713_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Some other name',
            },
        ),
        migrations.DeleteModel(
            name='WorkPattern',
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='scrum_team_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.ScrumTeam', verbose_name='Scrum team'),
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='scrum_team_roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.ScrumTeamRole', verbose_name='Roles'),
        ),
    ]