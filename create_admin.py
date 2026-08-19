import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlinexam.settings")
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
    user.save()
    print("ADMIN USER CREATED SUCCESSFULLY")
else:
    print("ADMIN_USERNAME or ADMIN_PASSWORD is missing")