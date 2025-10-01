#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv
from torch import nn


load_dotenv()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    class MnistModel(nn.Module):
        def __init__(self, input_size, num_classes):
            super().__init__()
            self.linear = nn.Linear(input_size, num_classes)

        def forward(self, xb):
            xb = xb.reshape(-1, 784)
            return self.linear(xb)

    main()
