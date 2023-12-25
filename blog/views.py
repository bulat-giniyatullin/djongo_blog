from django.views.generic import ListView, TemplateView
from .models import Post
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from allauth.account.forms import SignupForm

'''class BlogListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-title']'''


def listing(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "home.html", {"page_obj": page_obj})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ExamplesPageView(TemplateView):
    template_name = 'examples.html'


class LibPageView(TemplateView):
    template_name = 'lib.html'


class PrepPageView(TemplateView):
    template_name = 'prep.html'
