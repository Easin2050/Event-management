# Generated by Django 5.1.6 on 2025-03-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_participant_delete_perticipant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='event_participant', to='events.participant'),
        ),
    ]
