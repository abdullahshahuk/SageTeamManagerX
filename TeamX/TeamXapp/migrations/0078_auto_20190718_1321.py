# Generated by Django 2.2.3 on 2019-07-18 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamXapp', '0077_auto_20190718_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allmembers',
            name='scrum_team_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='TeamXapp.ScrumTeam', verbose_name='Scrum teams'),
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='scrum_team_roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='TeamXapp.ScrumTeamRole', verbose_name='Roles'),
        ),
    ]
