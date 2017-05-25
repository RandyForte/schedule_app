from django.contrib import admin

# Register your models here.
from schedule_app.models import Availability, Job, Shift, Skill, Worker

admin.site.register(Availability)
admin.site.register(Job)
admin.site.register(Shift)
admin.site.register(Skill)
admin.site.register(Worker)
