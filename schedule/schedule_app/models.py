from django.db import models

# Create your models here.
class Job(models.Model):
    jobName = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.jobName

class Shift(models.Model):
    shiftName = models.CharField(max_length=255,unique=True)
    shiftStartTime = models.TimeField()
    shiftEndTime = models.TimeField()
    job = models.ForeignKey(Job)
    daysOfTheWeek = (('SUNDAY','Sunday'),('MONDAY','Monday'),('TUESDAY','Tuesday'),
    ('WEDNESDAY','Wednesday'),('THURSDAY','Thursday'),('FRIDAY','Friday'),
    ('SATERDAY','Saterday'))
    dayOfTheWeek = models.CharField(choices=daysOfTheWeek,max_length=255)

    def __str__(self):
        return self.shiftName

class Availability(models.Model):
    availabilityName = models.CharField(max_length=255,unique=True)
    sundayAvailabilityStartTime = models.TimeField(blank=True,null=True,default='00:00:00')
    sundayAvailabilityEndTime = models.TimeField(blank=True,null=True,default='00:00:00')
    mondayAvailabilityStartTime = models.TimeField(blank=True,null=True,default='00:00:00')
    mondayAvailabilityEndTime = models.TimeField(blank=True,null=True,default='00:00:00')
    tuesdayAvailabilityStartTime = models.TimeField(blank=True,null=True,default='00:00:00')
    tuesdayAvailabilityEndTime = models.TimeField(blank=True,null=True,default='00:00:00')
    wednesdayAvailabilityStartTime = models.TimeField(blank=True,null=True,default='00:00:00')
    wednesdayAvailabilityEndTime = models.TimeField(blank=True,null=True,default='00:00:00')
    thursdayAvailabilityStartTime = models.TimeField(blank=True,null=True,default='00:00:00')
    thursdayAvailabilityEndTime = models.TimeField(blank=True,null=True,default='00:00:00')
    fridayAvailabilityStartTime = models.TimeField(blank=True,null=True,default='00:00:00')
    fridayAvailabilityEndTime = models.TimeField(blank=True,null=True,default='00:00:00')
    saterdayAvailabilityStartTime = models.TimeField(blank=True,null=True,default='00:00:00')
    saterdayAvailabilityEndTime = models.TimeField(blank=True,null=True,default='00:00:00')

    def __str__(self):
        return self.availabilityName

class Worker(models.Model):
    workerName = models.CharField(max_length=255,unique=True)
    availability = models.ForeignKey(Availability)

    def __str__(self):
        return self.workerName

class Skill(models.Model):
    worker = models.ForeignKey(Worker)
    job = models.ForeignKey(Job)

    def __str__(self):
        display = str(self.worker) + " " + str(self.job)
        return display
