from django.urls import path, include
from .views import AboutPageView, ExamplesPageView, LibPageView, PrepPageView, listing,\
    signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', BlogListView.as_view(), name='home'),
    path('', listing, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('examples/', ExamplesPageView.as_view(), name='examples'),
    path('lib/', LibPageView.as_view(), name='lib'),
    path('prep/', PrepPageView.as_view(), name='prep'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('/accounts', include('allauth.urls'))
]
