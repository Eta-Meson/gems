# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=80000)),
            ],
        ),
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=10000)),
                ('postname', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to=b'documents/candidate_photos/%Y/%m/%d')),
                ('approved', models.BooleanField()),
                ('voteInfo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ChallengeStrings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challengeStr', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='CommentLikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=80000)),
                ('likes', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GlobalVariables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('varname', models.CharField(unique=True, max_length=128)),
                ('value', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eligibleGender', models.CharField(max_length=1)),
                ('eligibleCourse', models.CharField(max_length=5)),
                ('postCount', models.IntegerField()),
                ('postname', models.CharField(max_length=50)),
                ('info_fields', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='PublicKeys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publicKey', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document', models.FileField(upload_to=b'documents/other_uploads/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('voted', models.BooleanField()),
                ('department', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1)),
                ('hostel', models.CharField(max_length=30)),
                ('encryptedPrivateKey', models.CharField(max_length=4096)),
                ('plaintextPrivatekey', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plainText', models.CharField(max_length=50)),
                ('certificate', models.CharField(max_length=60)),
                ('challengeStr', models.ForeignKey(to='mainSite.ChallengeStrings')),
                ('publicKey', models.ForeignKey(to='mainSite.PublicKeys')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(to='mainSite.Users', null=True),
        ),
        migrations.AddField(
            model_name='commentlikes',
            name='comment',
            field=models.ForeignKey(to='mainSite.Comments'),
        ),
        migrations.AddField(
            model_name='commentlikes',
            name='user',
            field=models.ForeignKey(to='mainSite.Users'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='candidate',
            field=models.ForeignKey(to='mainSite.Users'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='comments',
            field=models.ManyToManyField(to='mainSite.Comments', blank=True),
        ),
    ]
