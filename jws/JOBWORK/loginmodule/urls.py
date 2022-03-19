from django.contrib import admin
from django.urls import path,include


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',views.landing, name='landing'),
     path('login',views.login, name='login'),
     path('regis',views.registrations, name='regis'),
     path('homepage',views.homepage, name='homepage'),
     path('signup',views.signup, name='signup'),
     path('home',views.home, name='home'),
     path("otp",views.otp,name='otp'),
     path("otp1",views.otp1,name='otp1'),
     path("send_otp",views.send_otp,name='send_otp'),
     path("send_otp1",views.send_otp1,name='send_otp1'),
     path("profileedit",views.profileedit,name='profileedit'),
     path("profileedit1",views.profileedit1,name='profileedit1'),
     path("profilepage",views.profilepage,name='profilepage'),
     path("logout",views.logout,name='logout'),
     path("search",views.search,name='search'),
     path("gotochat",views.gotochat,name='gotochat'),
     path("chatsearch",views.chatsearch,name='chatsearch'),
     path("updatepass",views.updatepass,name='updatepass'),
     path("profilesearch/<str:username>",views.profilesearch,name='profilesearch'), 
     


    #  path("jobs",include(jobs.urls)),
    #  path("jobuploading",views.index,name='job_uploading'),

]