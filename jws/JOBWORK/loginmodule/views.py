# Create your views here.from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User,auth
from .models import regis
from .models import Profile
from django.core.mail import send_mail
import math, random
from chat.models import Message
from chat.models import Room
from django.db.models import Q
from jobs.models import deal,jobs

def landing(request):
    return render(request,'landing.html')

def login(request):
    return render(request,'login.html')

def registrations(request):
    return render(request,'regis.html')

def homepage(request):
    username = request.session['uname']
    # jb=jobs()
    # # j1=jobs.objects.filter(user=username)
    # # print(j1)
    de=deal.objects.filter(deal__user=username)
    rooms = Room.objects.all()
#print rooms 
    valid_rooms = []
    for room in rooms:
        if username in room.name:
            valid_rooms.append({'url':room.name, 'friend': room.name.replace(username, "").replace("-", "")})
    
    return render(request,'home.html',{'rooms': valid_rooms, 'username': username,'total':de})

def signup(request):
    print('---------------------------------------------------')
    print(request.method)
    print('---------------------------------------------------')
    if request.method=="POST":
        print("this is post")
        fname = request.POST['fname']
        lname = request.POST['lname']
        pswd1 = request.POST['password']
        pswd2 = request.POST['cpassword']
        email = request.POST['email']
        gst = request.POST['gstno']
        contact = request.POST['contact']
        uname = request.POST['username']
        
        if pswd1 == pswd2:
            if regis.objects.filter( fname = fname).exists():
                
             messages.error(request,'already taken')
             return render(request,'regis.html')

            elif regis.objects.filter(email = email).exists():
                 messages.error(request,'email already taken')
                 return render(request,'regis.html')
 
            else:
                user = regis( fname = fname,lname = lname,pswd = pswd1,email = email, gst =  gst, contact =  contact, uname = uname)
            user.save()
            return redirect(f'/otp1?email={email}')

        else:
            messages.error(request,"password does not match")
            return render(request,'regis.html')

    else:
         return render(request,'regis.html')

def home(request):
    if request.session.get('username') == None:
        if request.method == "POST":
            # analyse the form
            uname=request.POST['uname']
            pswd=request.POST['pswd']
            try:
                superUser = request.POST['superuser']
            except:
                superUser = None
            if superUser == "superuser":
                if uname == superuser_uname and pswd == superuser_pswd:
                    request.session['superuser'] = True
                    # return redirect(reverse("loginmodule:welcome"))
                    return render(request,"home.html")
                else:
                    messages.error(request,"You'r not authorize")
                    return render(request,"landing.html")
            else:
                #check user is register or not
                if regis.objects.filter(uname = uname).exists() and regis.objects.filter(pswd = pswd).exists():
                    request.session['uname'] = uname
                    print('------------------------------------')
                    print(request.session.get('uname'))
                    print('------------------------------------')
                    return render(request,'home.html')
                #user is  register then value of user is not None
                else:
                    #login access to user
                    messages.error(request,"Invalid username or password")
                    return redirect('/login')
        else:
            # first login
            return redirect('/login')
    else:
        return render(request,'home.html')


def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    email=request.POST.get("email")

    
    o=generateOTP()
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'sahilsheta67@gmail.com',[email],fail_silently=False,html_message=htmlgen)
    print('------------------------------------------------')
    print(o)
    print(email)
    print('-------------------------------------------------')
    return HttpResponse(o)
    

def otp(request):
    return render(request,'otp.html')


def generateOTP1() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_otp1(request):
    email=request.POST.get("email")
    
    o=generateOTP1()
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'sahilsheta67@gmail.com',[email],fail_silently=False,html_message=htmlgen)
    print('------------------------------------------------')
    print(o)
    print(email)
    print('-------------------------------------------------')
    return HttpResponse(o)

def otp1(request):
    email=request.GET.get("email")
    return render(request,'otp1.html',{'email':email})




def profileedit1(request):
    if request.session.get('uname') == None:
        messages.error(request,'You are not authorize')
        return redirect('/login')
    else:
        return render(request,'profileedit.html')


def profileedit(request):
    if request.session.get('uname') == None:
        messages.error(request,'You are not authorize')
        return redirect('/login')

    else:
        if request.method == "POST":
           
            companyname = request.POST['company-name']
            ownername = request.POST['owner-name']
           
            bio = request.POST['bio']
            address = request.POST['address']
            
            uname = (request.session.get('uname'))
            user= regis.objects.get(uname=uname)
            profile = Profile(companyname =companyname,  ownername=  ownername,   bio=  bio,address=address,regis=user) 
            profile.save()

            userid=user.pk
            profile=Profile.objects.get(regis_id=userid)
            # print(dir(profile))
            # print(type(profile))
            print(profile.bio)
            print(user.gst)
            print('-------------------------------------------------')
                 #to do send data
            return render(request,'profile.html',{"cname":profile.companyname,"oname":profile.ownername,"gst":user.gst,"bio":profile.bio,"add":profile.address,"contact":user.contact,"email":user.email})

def profilepage(request):
    if request.session.get('uname') == None:
        messages.error(request,'You are not authorize')
        return redirect('/login')
    else:
       
        uname = (request.session.get('uname'))
        user=  regis.objects.get(uname=uname)
        userid=user.pk
        print(uname)
        print('------------------------------------------------')
        print(userid)
        print('------------------------------------------------')
        # if userid != None:
        try:
            profile=Profile.objects.get(regis_id=userid)

        except:
            profile = None
            # print(dir(profile))
             # print(type(profile))
            print('---------------------------------------')
            print(profile)
            print('---------------------------------------')

        if profile == None:
            text = "you are new user here so to create your profile info click on edit"
            context ={'editt':text }
            return render(request, 'profile.html',context)

        else:
         print('-------------------------------------------------')
         print(profile.bio)
         print(user.gst)
         print(profile.companyname)
         print('-------------------------------------------------')
        #to do send data
         return render(request,'profile.html',{"cname":profile.companyname,"oname":profile.ownername,"gst":user.gst,"bio":profile.bio,"add":profile.address,"contact":user.contact,"email":user.email})
        # else:
        #      return render(request,'profile.html')

def logout(request):
    if 'uname' in request.session:
        del request.session['uname']
    # if 'superuser' in request.session:
    #     del request.session['superuser']
    messages.success(request,'You are logged out!')
    return redirect('/')


def search(request):
     if request.session.get('uname') == None:
        messages.error(request,'You are not authorize')
        return redirect('/login')

     else:
            # return render(request,'Bookmodule/issueBook.html')
            if 'search' in request.POST:
                query = request.POST['search']
                search_category = request.POST['search_cat']


                if search_category == "username":
                   suname = regis.objects.all().filter((Q(uname__icontains = query))).exclude(uname= request.session.get('uname'))
                 
                   if len(suname)== 0:
                    return render(request,"search.html",{'error':'not found'})
                
                   return render(request,"search.html",{'usernamelist':suname})

                if search_category == "companyname":
                    uname = (request.session.get('uname'))
                    user=  regis.objects.get(uname=uname)
                    userid=user.pk
                    profile=Profile.objects.get(regis_id=userid)
                    scname =Profile.objects.all().filter((Q(companyname__icontains = query))).exclude(companyname=profile.companyname)
                    print('--------------------------------')
                    print(scname)
                    print('--------------------------------')

                    if len(scname)== 0:
                       return render(request,"search.html",{'error':'not found'})

                    return render(request,"search.html",{'companynamelist':scname})

def gotochat(request):
    username = request.session.get('uname')
    rooms = Room.objects.all()
#print rooms 

    valid_rooms = []
    
    for room in rooms:
        if username in room.name:
            valid_rooms.append({'url':room.name, 'friend': room.name.replace(username, "").replace("-", "")})
    
       
           
    return render(request,'chat.html', {'rooms': valid_rooms, 'username': username})
   
   # return render(request,'chat.html',{'room_names':room_details})


def chatsearch(request):
     if request.session.get('uname') == None:
        messages.error(request,'You are not authorize')
        return redirect('/login')

     else:
            # return render(request,'Bookmodule/issueBook.html')
            if 'search' in request.POST:
                query = request.POST['search']
                search_category = request.POST['search_cat']


                if search_category == "username":
                   suname = regis.objects.all().filter((Q(uname__icontains = query))).exclude(uname= request.session.get('uname'))
                   runame= request.session.get('uname')
                 
                if len(suname)== 0:
                     return render(request,"chatsearch.html",{'error':'not found'})
          
                
            return render(request,"chatsearch.html",{'usernamelist':suname,'runame':runame})

def updatepass(request):
    if request.method=='POST':
        uname = request.POST['username']
        npass = request.POST['password']
        ncpass = request.POST['con_password']

        if npass == ncpass:
            u=regis.objects.get(uname__exact=uname)
            u.pswd=npass
            u.save()
        
def profilesearch(request,username):
        uname=username
        user=  regis.objects.get(uname=uname)
        userid=user.pk
        profile=Profile.objects.get(regis_id=userid)

        return render(request,'searchprofile.html',{"cname":profile.companyname,"oname":profile.ownername,"gst":user.gst,"bio":profile.bio,"add":profile.address,"contact":user.contact,"email":user.email})
    






