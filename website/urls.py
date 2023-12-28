from django.urls import path
from . import views
from django.conf.urls.static import static
from dcrm import settings

urlpatterns = [
    path("",views.home,name='home'),
    #path("login/",views.login_user,name='login'),
    path("logout/",views.logout_user,name='logout'),
    path("register/",views.register_user,name='register'),
    path("notif/",views.notif,name='notif'),
    path("myevents/", views.my_events, name='myevents'),
    path("record/<str:pk>", views.customer_record, name='record'),
    path("exponent/<str:pk>", views.customer_exp, name='exponent'),
    path("myrecord/<str:pk>", views.my_record, name='myrecord'),
    path("myexponents/<str:pk>", views.my_exp, name='myexponent'),
    path("delete_record/<str:pk>", views.del_record, name='del_record'),
    path("delete_exponent/<str:pk>", views.del_exp, name='del_exponent'),
    path("add_record/", views.add_record, name='add_record'),
    path("add_exponent/", views.add_exp, name='add_exponent')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)