from django.conf.urls import url
from schedule_app import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^createworker/$',views.CreateWorker.as_view(success_url="/"),name='createworker'),
    url(r'^createavailability/$',views.CreateAvailability.as_view(success_url="/"),name='createavailability'),
    url(r'^createjob/$',views.CreateJob.as_view(success_url="/"),name='createjob'),
    url(r'^createshift/$',views.CreateShift.as_view(success_url="/createshift/"),name='createshift'),
    url(r'^createskill/$',views.CreateSkill.as_view(success_url="/createskill/"),name='createskill'),
    url(r'^worker_list_view/$',views.WorkerListView.as_view(),name='listwork'),
    url(r'^shift_list_view/$',views.ShiftListView.as_view(),name='listshift'),
    url(r'^availability_list_view/$',views.AvailabilityListView.as_view(),name='listavailability'),
    url(r'^worker_list_view/(?P<pk>\d+)/$',views.WorkerDetail.as_view(),name="workerdetail"),
    url(r'^shift_list_view/(?P<pk>\d+)/$',views.ShiftDetail.as_view(),name="shiftdetail"),
    url(r'^availability_list_view/(?P<pk>\d+)/$',views.AvailabilityDetail.as_view(),name="availabilitydetail"),
    url(r'^availability_list_view/(?P<pk>\d+)/update/$',views.AvailabilityUpdate.as_view(success_url="/availability_list_view/"),name='availabilityupdate'),
]
