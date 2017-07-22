from django.shortcuts import render
from django.views.generic import (TemplateView, View, CreateView, DetailView,
ListView, UpdateView)
from django.http import HttpResponse#testing only
# Create your views here.
from schedule_app import models

class IndexView(View):
    template_name = 'schedule/index.html'
    def get(self,request):
        return render(request,'schedule_app/index.html')

    def post(self,request):
        shifts = models.Shift.objects.all()#get all the shifts
        FINAL = {}#the final dict that is passed as context to the page
        day = None
        job = None
        timeStart = None
        timeEnd =  None
        worker_list = []#temp list that is used for when a worker is able to work
        for shift in shifts:
            if shift.dayOfTheWeek == 'SUNDAY':#TODO make this code look better
                day = 'sunday'
            elif shift.dayOfTheWeek == 'MONDAY':
                day = 'monday'
            elif shift.dayOfTheWeek == 'TUESDAY':
                day = 'tuesday'
            elif shift.dayOfTheWeek == 'WEDNESDAY':
                day = 'wednesday'
            elif shift.dayOfTheWeek == 'THURSDAY':
                day = 'thursday'
            elif shift.dayOfTheWeek == 'FRIDAY':
                day = 'friday'
            elif shift.dayOfTheWeek == 'SATERDAY':
                day = 'saterday'
            job = shift.job#get and set the job
            timeStart = shift.shiftStartTime#get and set the start time
            timeEnd = shift.shiftEndTime#get and set the end time
            print("job: " + str(job))#TODO Remove the debugging print statements
            print("Day of the week: "+ str(day))
            print("TimeStart:" + str(timeEnd))
            print("TimeEnd:" + str(timeStart))
            #get all the workers that can do the job for the shift
            possWorkers = models.Skill.objects.filter(job=job)
            tempWorkers = []#we need to get all the workers into a list
            for poss in possWorkers:
                tempWorkers.append(poss.worker)
                print(str(poss.worker))
            for temp in tempWorkers:#check the availability of the workers
                wrks = models.Worker.objects.filter(workerName=temp)
                for wrk in wrks:
                    if day == 'sunday':
                        print(wrk.availability.sundayAvailabilityStartTime)
                        print(wrk.availability.sundayAvailabilityEndTime)
                        if wrk.availability.sundayAvailabilityStartTime<=timeStart and wrk.availability.sundayAvailabilityEndTime>=timeEnd:
                            print(str(wrk) + " Can work")
                            print(shift.id)
                            worker_list.append(str(wrk))
                        else:
                            print(str(wrk) + " Can't work")
                    elif day == 'monday':
                        print(wrk.availability.mondayAvailabilityStartTime)
                        print(wrk.availability.mondayAvailabilityEndTime)
                        if wrk.availability.mondayAvailabilityStartTime<=timeStart and wrk.availability.mondayAvailabilityEndTime>=timeEnd:
                            print(str(wrk) + " Can work")
                            print(shift.id)
                            worker_list.append(str(wrk))
                        else:
                            print(str(wrk) + " Can't work")
                    elif day == 'tuesday':
                        print(wrk.availability.tuesdayAvailabilityStartTime)
                        print(wrk.availability.tuesdayAvailabilityEndTime)
                        if wrk.availability.tuesdayAvailabilityStartTime<=timeStart and wrk.availability.tuesdayAvailabilityEndTime>=timeEnd:
                            print(str(wrk) + " Can work")
                            print(shift.id)
                            worker_list.append(str(wrk))
                        else:
                            print(str(wrk) + " Can't work")
                    elif day == 'wednesday':
                        print(wrk.availability.wednesdayAvailabilityStartTime)
                        print(wrk.availability.wednesdayAvailabilityEndTime)
                        if wrk.availability.wednesdayAvailabilityStartTime<=timeStart and wrk.availability.wednesdayAvailabilityEndTime>=timeEnd:
                            print(str(wrk) + " Can work")
                            print(shift.id)
                            worker_list.append(str(wrk))
                        else:
                            print(str(wrk) + " Can't work")
                    elif day == 'thursday':
                        print(wrk.availability.thursdayAvailabilityStartTime)
                        print(wrk.availability.thursdayAvailabilityEndTime)
                        if wrk.availability.thursdayAvailabilityStartTime<=timeStart and wrk.availability.thursdayAvailabilityEndTime>=timeEnd:
                            print(str(wrk) + " Can work")
                            print(shift.id)
                            worker_list.append(str(wrk))
                        else:
                            print(str(wrk) + " Can't work")
                    elif day == 'friday':
                        print(wrk.availability.fridayAvailabilityStartTime)
                        print(wrk.availability.fridayAvailabilityEndTime)
                        if wrk.availability.fridayAvailabilityStartTime<=timeStart and wrk.availability.fridayAvailabilityEndTime>=timeEnd:
                            print(str(wrk) + " Can work")
                            print(shift.id)
                            worker_list.append(str(wrk))
                        else:
                            print(str(wrk) + " Can't work")
                    elif day == 'saterday':
                        print(wrk.availability.saterdayAvailabilityStartTime)
                        print(wrk.availability.saterdayAvailabilityEndTime)
                        if wrk.availability.saterdayAvailabilityStartTime<=timeStart and wrk.availability.saterdayAvailabilityEndTime>=timeEnd:
                            print(str(wrk) + " Can work")
                            print(shift.id)
                            worker_list.append(str(wrk))
                        else:
                            print(str(wrk) + " Can't work")
            FINAL[shift.shiftName] = worker_list
            worker_list = []
        print(FINAL)
        return render(request,'schedule_app/index.html',{'FINAL':FINAL})
class CreateWorker(CreateView):
    fields = ('workerName','availability')
    model = models.Worker
    template_name = 'schedule_app/create_form.html'
class CreateAvailability(CreateView):
    fields = '__all__'
    model = models.Availability
    template_name = 'schedule_app/create_form.html'
class WorkerDetail(DetailView):
    context_object_name = 'worker_detail'
    model = models.Worker
    template_name = 'schedule_app/worker_detail.html'
    # def skill(self,request,pk):
        # return models.Skill.filter(Worker__pk=pk)
        # skills = models.Skill.objects.all()
        # skillList = []
        # for skill in skills:
        #     print(pk)
        #     print("--------------")
        #     print(skill.worker.pk,)
        #     if skill.worker.pk == pk:
        #         skillList.append(str(skill.job))
        # return skillList
    # def get_context_data(self,**kwargs):
    #     context = super(WorkerDetail,self).get_context_data(**kwargs)
    #     print("--------")
    #     print(kwargs['object'].pk)
    #     print("--------")
    #     context['skills'] = str(models.Skill.objects.filter(id=kwargs['object'].pk))
    #     return context
    def get_context_data(self,**kwargs):
        context = super(WorkerDetail,self).get_context_data(**kwargs)
        context["skill"] = models.Skill.objects.filter(worker = "Mike the Snake")
        print(context["skill"])
        return context
class ShiftDetail(DetailView):
    context_object_name = 'shift_detail'
    model = models.Shift
    template_name = 'schedule_app/shift_detail.html'
class AvailabilityDetail(DetailView):
    context_object_name = 'availability_detail'
    model = models.Availability
    template_name = 'schedule_app/availability_detail.html'
class WorkerListView(ListView):
    context_object_name = 'workers'
    model = models.Worker
class ShiftListView(ListView):
    context_object_name = 'shifts'
    model = models.Shift
class AvailabilityListView(ListView):
    context_object_name = 'availabilitys'
    model = models.Availability
class CreateJob(CreateView):
    fields = '__all__'
    model = models.Job
    template_name = 'schedule_app/create_form.html'
class CreateSkill(CreateView):
    fields = '__all__'
    model = models.Skill
    template_name = 'schedule_app/create_form.html'
class CreateShift(CreateView):
    fields = '__all__'
    model = models.Shift
    template_name = 'schedule_app/create_form.html'
class AvailabilityUpdate(UpdateView):
    model = models.Availability
    fields = '__all__'
    template_name = 'schedule_app/availability_update.html'
