from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .views import about, ExamplesPageView, LibPageView, PrepPageView, listing,\
    register, my_login, user_logout, examples, lib_view, prep_view


urlpatterns = [
    path('', listing, name='home'),
    #path('about/', AboutPageView.as_view(), name='about'),
    path('about/', about, name='about'),
    #path('examples/', ExamplesPageView.as_view(), name='examples'),
    path('examples/', examples, name='examples'),
    #path('lib/', LibPageView.as_view(), name='lib'),
    #path('prep/', PrepPageView.as_view(), name='prep'),
    path('lib/', lib_view, name='lib'),
    path('prep/', prep_view, name='lib'),
    path('register/', register, name="register"),
    path('login/', my_login, name="login"),
    path('user-logout/', user_logout, name="user-logout"),
]
