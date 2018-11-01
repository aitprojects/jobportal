# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-11-01 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20181030_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresume',
            name='resume',
            field=models.FileField(default='defaults.doc', max_length=128, upload_to='resume/uploaded/', verbose_name='resume'),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, default='Which Degree Did You Earn ?', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='descriptions',
            field=models.CharField(blank=True, default='Description about education', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='univercity',
            field=models.CharField(blank=True, default='Where Did You Learn ?', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='experiance',
            name='company',
            field=models.CharField(blank=True, default='Where Did You Work', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='experiance',
            name='description',
            field=models.CharField(blank=True, default='Say Something About Your Job', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='about_company',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='closing_date',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='contract_duration',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='contract_type',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='duties_responsibilities',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='education',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='extension_passibility',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='functional_area',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='gender',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='item_id',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_description',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='jobs_location',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='nationality',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='number_vacancies',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='open_date',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='open_ended',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='organization',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='probation_period',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='qualification',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='reference',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary_range',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='skills',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='submission_email',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='submission_guideline',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='title',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='website',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='work_type',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='year_of_expirence',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='about_company',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='closing_date',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='contract_duration',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='contract_type',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='duties_responsibilities',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='education',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='extension_passibility',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='functional_area',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='gender',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='item_id',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='job_description',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='jobs_location',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='nationality',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='number_vacancies',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='open_date',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='open_ended',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='organization',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='probation_period',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='qualification',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='reference',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='salary_range',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='skills',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='submission_email',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='submission_guideline',
            field=models.CharField(default='0', max_length=8000),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='title',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='website',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='work_type',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='spiderdata',
            name='year_of_expirence',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='userorbrowserseen',
            name='token',
            field=models.CharField(default='0', max_length=512),
        ),
        migrations.AlterField(
            model_name='userresume',
            name='address',
            field=models.CharField(blank=True, default='no address', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userresume',
            name='direction',
            field=models.CharField(blank=True, default='nod', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='userresume',
            name='email',
            field=models.CharField(blank=True, default='YourEmail@example.com', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='userresume',
            name='interst_and_activites',
            field=models.CharField(blank=True, default='say something about yourself ', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userresume',
            name='phone',
            field=models.CharField(blank=True, default='9300', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='userresume',
            name='profession',
            field=models.CharField(blank=True, default='Proffession ?', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userresume',
            name='tags',
            field=models.CharField(blank=True, default='no tags', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='usershortlisted',
            name='token',
            field=models.CharField(default='0', max_length=512),
        ),
    ]