# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='first_published_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='First published at', db_index=True),
        ),
    ]
