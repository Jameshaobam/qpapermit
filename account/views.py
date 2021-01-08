from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def signup_user(r):
    if r.method == 'GET':
       return render(r,'accounts/register.html')
    else:
        username = r.POST['username']
        firstname = r.POST['firstname']
        lastname = r.POST['lastname']
        email = r.POST['email']
        email_low = email.lower()
        password1 = r.POST['password1']
        password2 = r.POST['password2']
        if len(password1.strip()) < 8:
            print('Password is too short,at least there must be 8 characters')
            messages.error(r,'Password must be at least 8 characters containing special characters')
            return redirect('account:signup_user')
        else:
        
                if password1 == password2:
                    try:
                        if User.objects.filter(username = username).exists():
                            print('Username taken!')
                            messages.error(r,"Username taken!Try different username")
                            return redirect('account:signup_user')
                        elif User.objects.filter(email = email_low).exists():
                            print('Email taken!')
                            messages.error(r,"Email taken!Try different email")
                            return redirect('account:signup_user')
                        else:
                            user = User.objects.create_user(username = username,email = email_low,first_name = firstname,last_name = lastname,password = password2)
                            user.save()
                            # messages.success(r,'User saved')
                            msg = "User successfully registered with username "+ str(user.username)
                            messages.success(r,msg)
                            print("User saved!")
                            return redirect('account:signin_user')
                    except Exception as e:
                            print(e)
                            messages.error(r, 'Error in registration')
                            return redirect('account:signup_user')
                else:
                    messages.error(r,"Password not match!")
                    return redirect('account:signup_user')


def signin_user(r):
    if r.method == 'GET':


        return render(r, 'accounts/signin.html')
    else:
        username = r.POST['username'].lower()
        password = r.POST['password']
        user = authenticate(r,username=username,password=password)

        if user is not  None:
            login(r,user)
            messages.success(r,f"You have successfully login as {user.username}")
            return  redirect('home:home')
        else:
            error = 'Error occur!Email and password does not match'
            messages.error(r,error)
            return redirect('account:signin_user')


def logout_user(r):
    if r.method != 'GET':
        if r.user.is_authenticated:
            logout(r)
            messages.success(r,'Logout successfully')
            return redirect('home:home')
        else:
            return HttpResponse('You already logout')
    else:
            if r.user.is_authenticated:
                return render(r,'error.html')
            else:
                print("You can't go to logout directly")
                messages.error(r,'You need to login first to logout')
                return redirect('account:signin_user')
