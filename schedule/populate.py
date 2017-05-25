import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','schedule.settings')
import django
django.setup()
from schedule_app.models import Availability, Worker, Job, Shift, Skill

def populate():
    avail = Availability.objects.get_or_create()

if __name__ == '__main__':
    print("Populating server with test data")
    populate()
    print('Done')
