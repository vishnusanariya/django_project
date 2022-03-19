from django.http import HttpResponse
from django.shortcuts import redirect, render
from loginmodule.models import Profile, regis
from .models import jobs
from .models import History,deal
from django.db.models import Q


# Create your views here.
def index(request):
    username=request.session['uname']
    return render(request,'jobs/requirement-upload.html',{'username':username})

def jobUpload(request):
    if request.method == 'POST':
        username=request.session['uname']
        job=jobs()
        job.job_type=request.POST['job-type']
        job.job_title=request.POST['job-title']
        job.job_description=request.POST['job-description']
        job.job_amount=request.POST['amount']
        job.job_duration=request.POST['deadline']
        job.job_image=request.FILES['job-image']
        job.user=username
        user=regis.objects.get(uname=username)
        print(user)
        if Profile.objects.get(regis=user)!= None:
            p1=Profile.objects.get(regis=user)
            job.job_company=p1.companyname
            job.save()
            return render(request,'jobs/requirement-upload.html',{'job':jobs(),'username':username})
        else:
            return HttpResponse("please complete profilr details first")

        # message.success(request, 'job requirement submitted successfully')
    else:
        # message.error(request,'submission failure.')
        return render(request,'jobs/requirement-upload.html',{'job':jobs()})
    
def viewJob(request):
    # if request.method == 'GET':
    #     username=request.session['uname']
    #     job=jobs()
    #     # if request.method == 'POST':
    #     #     amount=request.POST['amnt']
    #     #     print(amount)
    #     data=jobs.objects.filter(job_type='textile')
    #     jobsend={'total_jobs':data,'job':job}
    #     return render(request,'jobs/search.html',jobsend)
    # else:
    #     job=jobs()
    #     jobsend={'job':job}
    return render(request,'jobs/search.html')

# def viewJob1(request):
#     if request.method == 'GET':
#         username=request.session['uname']
#         job=jobs()
#         data=jobs.objects.filter(job_type='ceramic')
#         print(data)
#         jobsend={'total_jobs':data,'job':job}
#         return render(request,'jobs/search.html',jobsend)
#     else:
#         job=jobs()
#         jobsend={'job':job}
#     return render(request,'jobs/search.html',jobsend)

# def viewJob2(request):
#     if request.method == 'GET':
#         username=request.session['uname']
#         job=jobs()
#         data=jobs.objects.filter(job_type='casting')
#         print(data)
#         jobsend={'total_jobs':data,'job':job}
#         return render(request,'jobs/search.html',jobsend)
#     else:
#         job=jobs()
#         jobsend={'job':job}
#     return render(request,'jobs/search.html',jobsend)

def amountFilter(request):
    if request.method == 'POST':
        jtype=request.POST['job-type']
        amount=request.POST['amnt']
        print(jtype,amount)
        j=jobs.objects.filter(job_type=jtype,job_amount__gte=amount).order_by('-id')
        print(j)
        jobsend={'total_jobs':j,'job':j}
        return render(request,'jobs/search.html',jobsend)


def detailofjob(request,i):
        if request.method == "GET":
            data=jobs.objects.filter(id=i)
            return render(request,'jobs/job-details.html',{'data':data})
        else:
            return HttpResponse("error in method")
def myjobs(request):
    if request.method=='GET':
        username=request.session['uname']
        jb=jobs()
        myjobs=jobs.objects.filter(user=username)
        jobsend={'total_jobs':myjobs,'job':jb}
        return render(request,'jobs/myjobs.html',jobsend)

def deletejob(request,i):
    if request.method == 'GET':
        jb=jobs.objects.filter(id=i)
        jb.delete()
        return redirect('myjobs')

def jobHistory(request,i):
    if request.method == "GET":
        t1=jobs.objects.get(id=i)
        worker=request.session['uname']
        title=t1.job_title
        amount=t1.job_amount
        a=History(job_id=t1.id,job_title=title,job_giver=t1.user,job_worker=worker,job_amount=amount)
        a.save()
        b=History.objects.filter(job_worker=worker)
        data={'history':b}
        t1.delete()
        return render(request,'jobs/history.html',data)
    else:
        return HttpResponse("ERROR in method")
    
def allHistory(request):
    username=request.session['uname']
    hist=History.objects.filter(Q(job_giver=username) | Q(job_worker=username))
    h={'history':hist}
    return render(request,'jobs/allhistory.html',h)

def dealrequest(request,i):
    username=request.session['uname']
    jid=jobs.objects.get(id=i)
    print(jid)
    d1=deal(deal=jid,job_worker=username)
    d1.save()
    d2=deal.objects.all()
    print(d2)
    jobsend={'total_jobs':d2}
    return redirect('viewjob')


def dealapprove(request,i,j):
    username=request.session['uname']
    j1=jobs.objects.get(id=j)
    if j1.user ==username:
        ap=True
        d2=deal.objects.get(deal_id=j,job_worker=i)
        d2.status=ap
        d2.job_creater_approval=ap
        print(d2)
        d2.save()
        t1=jobs.objects.get(id=j)
        worker=d2.job_worker
        title=t1.job_title
        amount=t1.job_amount
        a=History(job_id=t1.id,job_title=title,job_giver=t1.user,job_worker=worker,job_amount=amount)
        a.save()
        t1.delete()
        d=deal.objects.all()
        return render(request,'jobs/deal.html',{'total_jobs':d})
    else:
        return HttpResponse("yore not creater of this job")


def alldeal(request):
    username=request.session['uname']
    jb=jobs()
    # j1=jobs.objects.filter(user=username)
    # print(j1)
    de=deal.objects.filter(deal__user=username)
    print(de)
    dealsend={'total':de}
    return render(request,'jobs/deals.html',dealsend)

def viewJob_land(request):
    # if request.method == 'GET':
    #     username=request.session['uname']
    #     job=jobs()
    #     # if request.method == 'POST':
    #     #     amount=request.POST['amnt']
    #     #     print(amount)
    #     data=jobs.objects.filter(job_type='textile')
    #     jobsend={'total_jobs':data,'job':job}
    #     return render(request,'jobs/search.html',jobsend)
    # else:
    #     job=jobs()
    #     jobsend={'job':job}
    return render(request,'jobs/search1.html')

def amountFilter_land(request):
    if request.method == 'POST':
        jtype=request.POST['job-type']
        amount=request.POST['amnt']
        print(jtype,amount)
        j=jobs.objects.filter(job_type=jtype,job_amount__gte=amount)
        print(j)
        jobsend={'total_jobs':j,'job':j}
        return render(request,'jobs/search1.html',jobsend)