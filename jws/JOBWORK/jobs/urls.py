from . import views
from django.urls import path
from django.urls.conf import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index,name="Job"),
    path("jobUpload",views.jobUpload,name="jobUpload"),
    path("viewjob/",views.viewJob,name="viewjob"),
    path("viewjob_land/",views.viewJob_land,name="viewjob_land"),
    # path("viewjob1/",views.viewJob1,name="viewjob1"),
    # path("viewjob2/",views.viewJob2,name="viewjob2"),
    path("detailsofjob/<int:i>/",views.detailofjob,name="detailofjob"),
    path("history/<int:i>",views.jobHistory,name="history"),
    path("history",views.allHistory,name="allhistory"),
    path("filterd",views.amountFilter,name="filter"),
    path("myjobs",views.myjobs,name="myjobs"),
    path("dealreq/<int:i>",views.dealrequest,name="dealreq"),
    path("deals",views.alldeal,name="alldeals"),
    path("dealapproved/<str:i>/<int:j>",views.dealapprove,name="dealapprove"),
    path("deletejob/<int:i>",views.deletejob,name="dltjob"),
    path("filter_land",views.amountFilter_land,name="filter_land"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)