#!/usr/bin/env python
import os
import sys

sys.path.append('/var/www/vehicle-journal/vjournal')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vjournal.settings.prod")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
