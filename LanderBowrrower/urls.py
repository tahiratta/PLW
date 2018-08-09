from django.conf.urls import include, url
from .views import home,single,SubmitRequest,profile,contact,HomeView,editProfile,editPassword
from LanderBowrrower  import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'borrower_register/', views.BorrowerRegister.as_view(), name='borrower_register'),
    url(r'register/', views.LanderRegister.as_view(), name='lander_register'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'index.html'}, name='logout'),
    url(r'home/', home, name='home'),
    url(r'profile/', profile, name='profile'),
    url(r'edit/profil/', editProfile, name='editprofile'),
    url(r'edit/password/', editPassword, name='editPassword'),
    url(r'single/', single, name='single'),
    url(r'request/', SubmitRequest, name='submitrequest'),
    url(r'contact/', contact, name='contact'),
    # url(r'^$', index, name='index'),
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),


]