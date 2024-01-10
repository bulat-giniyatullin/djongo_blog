from django.views.generic import ListView, TemplateView
from .models import Post
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LoginForm


def listing(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "home.html", {"page_obj": page_obj})


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    context = {'registerform': form}
    return render(request, 'register.html', context=context)


def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)  # Redirect to the requested page
                else:
                    return redirect("about")

    context = {'loginform': form}
    return render(request, 'my-login.html', context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("home")


#@login_required(login_url="my-login")
'''class AboutPageView(TemplateView):
    template_name = 'about.html'
    '''


#@login_required(login_url="login")
def about(request):
    return render(request, 'about.html')


@login_required(login_url="login")
def examples(request):
    next_page = request.GET.get('next')
    context = {'next_page': next_page}
    return render(request, 'examples.html', context=context)


@login_required(login_url="login")
def lib_view(request):
    next_page = request.GET.get('next')
    context = {'next_page': next_page}
    return render(request, 'lib.html', context=context)


@login_required(login_url="login")
def prep_view(request):
    next_page = request.GET.get('next')
    context = {'next_page': next_page}
    return render(request, 'prep.html', context=context)
