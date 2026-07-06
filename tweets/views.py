from django.shortcuts import render,redirect
from . models import Tweets
from . forms import tweet_form,UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def tweet_read(request):
    tweets=Tweets.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets': tweets})
    
@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = tweet_form(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = tweet_form()

    return render(request, 'tweet_form.html', {'form': form})
    

@login_required
def tweet_edit(request,tweet_id):
   tweet=get_object_or_404(Tweets,pk=tweet_id,user=request.user)
   if request.method=='POST' :
      form=tweet_form(request.POST,request.FILES,instance=tweet)
      if form.is_valid():
         tweet=form.save(commit=False)
         tweet.user=request.user
         tweet.save()
         return redirect('tweet_list')
   else:
      form=tweet_form(instance=tweet)
   return render(request,'tweet_form.html',{'form':form})
   
@login_required
def tweet_delete(request,tweet_id):
   tweet=get_object_or_404(Tweets,pk=tweet_id,user=request.user)
   if request.method=='POST':
      tweet.delete()
      return redirect('tweet_list')  
   return render(request,'tweet_delete_confirmation.html',{'tweet':tweet}) 


def register(request):
   if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
   else:
        form = UserRegistrationForm()

   return render(request, 'registration/register.html',{'form':form})