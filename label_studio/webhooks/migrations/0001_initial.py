# Generated by Django 3.1.4 on 2021-06-08 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2048, verbose_name='URL of webhook')),
                ('send_payload', models.BooleanField(verbose_name='does webhook send the payload')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webhooks', to='webhooks.webhook')),
            ],
            options={
                'db_table': 'webhook',
            },
        ),
        migrations.CreateModel(
            name='WebhookAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[['PROJECT_CREATED', 'Project created'], ['PROJECT_PUBLISHED', 'Project published'], ['PROJECT_FINISHED', 'Project finished'], ['ANNOTATION_CREATED', 'Annotation created'], ['ANNOTATION_UPDATED', 'Annotation updated'], ['TASKS_IMPORTED', 'Tasks imported']], db_index=True, max_length=128, verbose_name='action of webhook')),
                ('webhook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='webhooks.webhook')),
            ],
            options={
                'db_table': 'webhook_action',
                'unique_together': {('webhook', 'action')},
            },
        ),
    ]