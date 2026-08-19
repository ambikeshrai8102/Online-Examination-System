import os
import sys

# Django project folder को Python path में जोड़ना
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, "onlinexamination")
sys.path.insert(0, PROJECT_DIR)

# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlinexam.settings")

import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("ADMIN_USERNAME")
password = os.environ.get("ADMIN_PASSWORD")

if username and password:
    user, created = User.objects.get_or_create(username=username)

    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()

    if created:
        print("ADMIN USER CREATED SUCCESSFULLY")
    else:
        print("ADMIN USER UPDATED SUCCESSFULLY")
else:
    print("ADMIN_USERNAME or ADMIN_PASSWORD is missing")