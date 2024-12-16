# Generated by Django 4.2.11 on 2024-05-20 13:42

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    def populate_request_types(apps, schema_editor):
        RequestType = apps.get_model('MainApp', 'RequestType')
        RequestType.objects.bulk_create([
            RequestType(type='GET_CHANNEL_BY_ID'),
            RequestType(type='GET_VIDEOS_BY_CHANNEL_ID'),
            RequestType(type='GET_VIDEO_BY_ID'),
            RequestType(type='GET_COMMENTS_BY_VIDEO_ID'),
            RequestType(type='GET_CHANNEL_BY_URL'),
            RequestType(type='GET_CHANNEL_BY_VIDEO_ID'),
            RequestType(type='COMMENTS_SIZE'),
            RequestType(type='GET_ANALYSIS_OF_TIME'),
            RequestType(type='GET_ANALYSIS_OF_LANGUAGES'),
            RequestType(type='GET_ANALYSIS_OF_EMOTION'),
            RequestType(type='GET_ANALYSIS_OF_LIKES_VS_REPLIES'),
            RequestType(type='GET_ANALYSIS_OF_NEQ_POS'),
            RequestType(type='GET_POPULARITY'),
            RequestType(type='GET_WORD_MAP'),
        ])

    operations = [
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
            ],
            options={
                'db_table': 'tb_request_type',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='yt_id',
            field=models.TextField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.requesttype'),
        ),
        migrations.RunPython(populate_request_types)
    ]