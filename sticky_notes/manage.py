#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set default Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')

    try:
        # Import execute_from_command_line function from Django management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed or not available, raise an ImportError
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute administrative tasks from command line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
