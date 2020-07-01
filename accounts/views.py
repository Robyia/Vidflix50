from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render, redirect
from accounts.models import User, mailing
from course.models import category, language
from django.contrib import auth, messages

from vidflix.settings import *
from django.views import View
from django.core.mail import send_mail
import django.shortcuts
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from course.models import course, Lesson


def index(request):
    a = course.objects.all()
    categori = category.objects.all()
    lang = language.objects.all()
    context = {"a": a,
               "language": lang,
               "category": categori
               }
    return render(request, 'index.html', context)


def lessonList(request, slug):
    cource = course.objects.get(slug=slug)
    a = Lesson.objects.filter(base_course=cource)
    print(cource)
    categoris = category.objects.all()
    lang = language.objects.all()
    context = {
        'a': a,
        "course": cource,
        "language": lang,
        "category": categoris,
    }
    return render(request, 'mostwatched.html', context)


def courseVideos(request, slug):
    if request.user.is_authenticated:
        a = Lesson.objects.get(slug=slug)
        p = Lesson.objects.filter(base_course=a.base_course)
        context = {
            'a': a,
            'p': p
        }
        return render(request, 'single.html', context)
    else:
        return redirect('login')


def mostwatched(request):
    return render(request, 'mostwatched.html')


def search(request):
    return render(request, 'search.html')


def single(request):
    return render(request, 'single.html')


def showpassword(request):
    return render(request, 'forgot_password.html')


def showpaytm(request):
    return render(request, 'paytm.html')


def showprice(request):
    return render(request, 'price.html')


def showactivate(request):
    return render(request, 'activate_account.html')


def showcontact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        customer = mailing(name=name, email=email, message=message)
        customer.save()

        send_mail(
            name,
            message,
            email,
            ['vidflix.vf@gmail.com'],
            fail_silently=False
        )

        return render(request, 'index.html')
    else:
        return render(request, 'contact.html')


def showabout(request):
    return render(request, 'about.html')

def showterms(request):
    return render(request, 'terms.html')


class loginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            context = {
                'message': 'not able to login'
            }
            return render(request, 'accounts/login.html', {'message': 'not able to login'})

    def get(self, request):
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        un = request.POST['name']
        em = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            if User.objects.filter(username=un).exists():
                print('username exists!')
            elif User.objects.filter(email=em).exists():
                print('email exists!')
            else:
                user = User.objects.create_user(username=un, email=em, password=pass1)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)

                subject = 'Activate Your Account'

                message = render_to_string('activate_account.html', {
                    'user': user,
                    'domain': current_site.doamin,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                send_mail(
                    subject,
                    message,
                    EMAIL_HOST_USER,
                    [em],
                    fail_silently=False
                )
                return redirect('login')
        else:
            print(request, 'password not matched !')
    else:
        return render(request, 'signupView')


class logoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('index')


class signupView(View):
    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        allemails = User.objects.filter(is_active=True).values_list('email', flat=True)
        allusernames = User.objects.filter(is_active=True).values_list('username', flat=True)

        # user = User.objects.create_user(username = username, password = password,first_name = first_name, last_name = last_name,email=email)
        if password == confirm_password:
            if email in allemails:
                context = {
                    'message': 'account with this email already Exists. try forgot password!',
                }
                return render(request, 'accounts/signup.html', context)

            if username in allusernames:
                context = {
                    'message': 'account with this username already Exists. try another one!',
                }
                return render(request, 'accounts/signup.html', context)

            user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                            last_name=last_name, email=email)
            # put data into user table from here

            context = {
                'message': 'user created successfully,'
            }

            return render(request, 'price.html', context)
        else:
            context = {
                'message': 'password does not matched',
            }
            return render(request, 'accounts/signup.html', context)

    def get(self, request):
        context = {
            'message': 'Signup here!',
        }
        return render(request, 'accounts/signup.html', context)


def categoryfilter(request, pk):
    categori = category.objects.get(pk=pk)
    categoris = category.objects.all()
    lang = language.objects.all()
    a = course.objects.filter(Category=categori)
    context = {
        'a': a,

        "language": lang,
        "category": categoris,
        "title": f"Following are some results from your search: {categori.name}"
    }
    return render(request, 'filter.html', context)


def languagefilter(request, pk):
    categori = language.objects.get(pk=pk)
    categoris = category.objects.all()
    lang = language.objects.all()
    a = course.objects.filter(Language=categori)
    context = {
        'a': a,

        "language": lang,
        "category": categoris,
        "title": f"Following are some results from your search: {categori.name}"
    }
    return render(request, 'filter.html', context)


def activate(request, uid64, token, *args, **kwargs):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token(user, token):
        user.is_active = True
        user.save()
        loginView(request, user)
        messages.success(request, 'Your account have been confirmed.')
        return render(request, 'index.html')
    else:
        messages.warning(request, ' The confirmation link was invalid, possibly because it has already been used')
        return redirect('/Thanks')


class ActivateAccount(View):
    pass


