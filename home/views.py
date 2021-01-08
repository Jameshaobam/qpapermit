from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Question,Year,Answer
from .choices import trade_choices,sem_choices,exm_choices,subject_choices
from django.contrib import  messages
from .forms import UpdateForm
import datetime


from django.http import Http404
def home(r):
   if r.method == 'GET':
       fiels = Question.objects.all().order_by('-date_published')
       yr = Year.objects.all()

       return render(r,'index.html',{'fiels':fiels,'yr':yr,'sems':sem_choices,'trades':trade_choices,'exm':exm_choices,'subject':subject_choices})




def index(r):
    return redirect('home:home')


def upload(r):

    if r.method == 'GET':
        if r.user.is_authenticated:
            yr = Year.objects.all()
            return render(r,'upload.html',{'sems':sem_choices,'trades':trade_choices,'exm':exm_choices,'yr':yr,'subject':subject_choices})
        else:
            return render(r,'error.html')
    else:
        try:
            trade = r.POST.get('trade')
            sem = r.POST.get('sem')
            exm = r.POST.get('exm')
            up_file = r.FILES['up']
            up_year = r.POST.get('year_sec')
            up_subject = r.POST.get('sub_sec')
            x = datetime.datetime.now()

            col = Question(trade=trade,semester=sem,file=up_file,exam = exm,year_of_exm = up_year,subject = up_subject,owner = r.user,date_published = x)
            col.save()
            print("Your file has been uploaded successfully")
            messages.success(r, 'Your file has been uploaded successfully')
            return redirect('home:home')
        except Exception as e:

            print("Error in uploading")
            print(e)
            print(r)
            messages.error(r, 'Could not upload, try again')
            return redirect('home:upload')



def search(r):

    if r.method == "GET":

        values = r.GET

        try:
            if 'trade_sec' in r.GET and 'sem_sec' in r.GET and 'exm' in r.GET and 'year_sec' in r.GET and 'sub_sec' in r.GET:
                     trade = r.GET['trade_sec']
                     yr = r.GET['year_sec']
                     exm_c = r.GET['exm']
                     sem = r.GET['sem_sec']
                     sub = r.GET['sub_sec']
                     collection = Question.objects.filter(semester__iexact=sem,trade__iexact =trade,year_of_exm__iexact = yr,exam__iexact = exm_c,subject__iexact = sub).order_by('-date_published')
            elif 'trade_sec' in r.GET and 'sem_sec' in r.GET and 'exm' in r.GET and 'year_sec' in r.GET: 
                     trade = r.GET['trade_sec']
                     yr = r.GET['year_sec']
                     exm = r.GET['exm']
                     sem = r.GET['sem_sec']
                   
                     collection = Question.objects.filter(semester__iexact=sem,trade__iexact =trade,year_of_exm__iexact = yr,exam__iexact = exm,).order_by('-date_published')
            
            
            
            elif 'trade_sec' in r.GET and 'sem_sec' in r.GET and 'year_sec' in r.GET and 'sub_sec' in r.GET:
                     trade = r.GET['trade_sec']
                     yr = r.GET['year_sec']
                     sem = r.GET['sem_sec']
                     sub = r.GET['sub_sec']
                     collection = Question.objects.filter(semester__iexact=sem,trade__iexact =trade,year_of_exm__iexact = yr,subject__iexact = sub).order_by('-date_published')


            elif 'trade_sec' in r.GET and 'exm' in r.GET and 'sem_sec' in r.GET and 'sub_sec' in r.GET:
                     trade = r.GET['trade_sec']
                     exm = r.GET['exm']
                     sem = r.GET['sem_sec']
                     sub = r.GET['sub_sec']
                     collection = Question.objects.filter(exam__iexact=exm,trade__iexact =trade,semester=sem,subject__iexact = sub).order_by('-date_published')
            elif 'trade_sec' in r.GET and 'sub_sec' in r.GET and 'sem_sec' in r.GET:
                     trade = r.GET['trade_sec']
                     sub = r.GET['sub_sec']
                     sem = r.GET['sem_sec']
                     collection = Question.objects.filter(subject__iexact=sub,trade__iexact =trade,semester=sem).order_by('-date_published')

            elif 'trade_sec' in r.GET and 'exm' in r.GET and 'sem_sec' in r.GET:
                     trade = r.GET['trade_sec']
                     exm = r.GET['exm']
                     sem = r.GET['sem_sec']
                     collection = Question.objects.filter(exam__iexact=exm,trade__iexact =trade,semester=sem).order_by('-date_published')
            elif 'trade_sec' in r.GET and 'sub_sec' in r.GET:
                     trade = r.GET['trade_sec']
                     sub = r.GET['sub_sec']
                     collection = Question.objects.filter(trade__iexact=trade,subject__iexact = sub).order_by('-date_published')

            elif 'trade_sec' in r.GET and 'sem_sec' in r.GET :
                     trade = r.GET['trade_sec']
                     sem = r.GET['sem_sec']
                     collection = Question.objects.filter(semester__iexact=sem,trade__iexact =trade).order_by('-date_published')
            elif 'trade_sec' in r.GET and 'exm' in r.GET :
                     trade = r.GET['trade_sec']
                     exm = r.GET['exm']
                     collection = Question.objects.filter(exam__iexact=exm,trade__iexact =trade).order_by('-date_published')
            elif 'trade_sec' in r.GET and 'year_sec' in r.GET :
                     trade = r.GET['trade_sec']
                     yr = r.GET['year_sec']
                     collection = Question.objects.filter(year_of_exm__iexact = yr,trade__iexact =trade).order_by('-date_published')
            elif 'sem_sec' in r.GET and 'sub_sec' in r.GET and 'year_sec' in r.GET:
                sem = r.GET['sem_sec']
                sub = r.GET['sub_sec']
                yr = r.GET['year_sec']
                collection = Question.objects.filter(subject__iexact=sub, semester__iexact=sem,year_of_exm__iexact = yr).order_by('-date_published')
            elif 'sem_sec' in r.GET and 'exm' in r.GET and 'year_sec' in r.GET:
                sem = r.GET['sem_sec']
                exm = r.GET['exm']
                yr = r.GET['year_sec']
                collection = Question.objects.filter(exam__iexact=exm, semester__iexact=sem,year_of_exm__iexact = yr).order_by('-date_published')

            elif 'sem_sec' in r.GET and 'year_sec' in r.GET:
                sem = r.GET['sem_sec']
                yr = r.GET['year_sec']
                collection = Question.objects.filter(semester__iexact=sem,year_of_exm__iexact=yr).order_by('-date_published')

            elif 'sem_sec' in r.GET and 'sub_sec' in r.GET:
                sem = r.GET['sem_sec']
                sub = r.GET['sub_sec']
                collection = Question.objects.filter(subject__iexact=sub,semester__iexact=sem).order_by('-date_published')
            elif 'sem_sec' in r.GET:
                sem = r.GET['sem_sec']
                collection = Question.objects.filter(semester__iexact=sem).order_by('-date_published')
            elif 'trade_sec' in r.GET:
                trade = r.GET['trade_sec']
                collection = Question.objects.filter(trade__iexact=trade).order_by('-date_published')
            elif 'sub_sec' in r.GET:
                sub = r.GET['sub_sec']
                collection = Question.objects.filter(subject__iexact=sub).order_by('-date_published')
            elif 'exm' in r.GET:
                exam_choose = r.GET['exm']
                collection = Question.objects.filter(exam__iexact=exam_choose).order_by('-date_published')


            else:
                messages.error(r,'Select all the fields!!!')
                return redirect('home:home')

        except:
            print("=================================")
        all_year = Year.objects.all()


        return render(r,'result.html',{'fiels':collection,'values':values,'sems':sem_choices,'trades':trade_choices,'exm':exm_choices,'all_year':all_year,'subject':subject_choices})
    else:


        return redirect('home:home')


def detail(r,pk):
    detail = get_object_or_404(Question,id = pk)
    answers = Answer.objects.filter(post = detail).order_by('-date_published')
    return  render(r,'details.html',{'detail':detail,'answers':answers})

def update(r,pk):

    yr = Year.objects.all() 
    to_update = Question.objects.get(id = pk) #get_object_or_404(Question,id = pk)
    if r.method == "GET":
        if   to_update.owner.id != r.user.id:
             # raise Http404
             print("You are not the user")
             return render(r, 'error.html')
        else:
          return render(r,'update.html',{'to_update':to_update,'sems':sem_choices,'trades':trade_choices,'exm':exm_choices,'yr':yr,'subject':subject_choices})
    else:
        if to_update.owner != r.user:
             # raise Http404
             return render(r, 'error.html')
        else:
            try:
                trade = r.POST.get('trade')
                sem = r.POST.get('sem')
                exm = r.POST.get('exm')
                up_file = r.FILES['up']
                up_year = r.POST.get('year_sec')
                up_subject = r.POST.get('sub_sec')
                owner = to_update.owner
                x =datetime.datetime.now()
                col = Question(id = pk,trade=trade,semester=sem,file=up_file,exam = exm,year_of_exm = up_year,subject = up_subject,owner = owner, date_published = x)
                col.save()
                messages.success(r, 'Successfully Updated')
                return redirect('home:home',to_update.id)
            except Exception as e:

                print('Error in updating')
                print(e)
                messages.error(r, 'Could not update, Try again')
                return redirect('home:detail',to_update.id)


def delete(r,pk):
    if r.method == "POST":
        to_delete = get_object_or_404(Question, pk=pk)
        if to_delete.owner != r.user:
            # raise Http404
            return render(r, 'error.html')
        else:

            to_delete.delete()
            messages.success(r,'Successfully deleted')
            return redirect('home:home')
    else:
        post =  get_object_or_404(Question, pk=pk)
        return redirect('home:detail',post.id)

def postanswer(r,pk):
    if r.method == 'POST':
        if r.user.is_authenticated:
            try:
                detail_post = get_object_or_404(Question, id=pk)
                context = r.POST['context']
                file = r.FILES['ans-file']
                owner = r.user
                post = detail_post
                date = datetime.datetime.now()
                answer = Answer(post=post,owner=owner,context=context,image=file,date_published=date)
                answer.save()
                messages.success(r,'Answers uploaded')
                return redirect('home:detail',detail_post.id )
            except Exception as e:
                messages.error(r,'Error in uploading, Try again')
                print("\nError in uploading answers\n")
                print(e)
                return redirect('home:detail',detail_post.id)
                
        else:
            messages.error(r,'You must login first to post answers')
            return  redirect('account:signin_user')

def update_ans(r,pk,ans_id):
    if r.method == "GET":
        answer = Answer.objects.get(id=ans_id)  # get_object_or_404(Answer,id = pk)
        if answer.owner.id == r.user.id:
            post = Question.objects.get(id=pk)

            return render(r,'ansupdate.html',{'ans':answer,'post':post})
        else:
            return render(r, 'error.html')
    else:
        try:
            post = Question.objects.get(id=pk)
            context = r.POST['context']
            file = r.FILES['ans-file']
            date = datetime.datetime.now()
            new_ans = Answer(id=ans_id,context=context,image=file,post=post,owner = r.user,date_published = date)
            new_ans.save()
            print("Answers saved!!!")
            messages.success(r,"Answers uploaded!")
            return redirect('home:detail',post.id)
        except Exception as e:
            print("Could not update the answers")
            print(e)
            messages.error(r,'   Could not update,  try again')
            return redirect('home:detail',post.id)



def delete_ans(r,pk,ans_id):
        if r.method == "POST":
            ans_to_delete = get_object_or_404(Answer,id = ans_id)
            if ans_to_delete.owner.id == r.user.id:
                post = Question.objects.get(id=pk)
                ans_to_delete.delete()
                messages.success(r,"Ans deleted successfully!")
                return redirect('home:detail',post.id)
            else:
                return render(r, 'error.html')
        else:
            ans_to_delete = get_object_or_404(Answer,id = ans_id)
            if ans_to_delete.owner.id == r.user.id:
                post = Question.objects.get(id=pk)
                return redirect('home:detail',post.id)

            else:
                return render(r, 'error.html')

def aboutpage(r):
    return render(r,'about.html')

def contactme(r):
    return render(r,'contactme.html')