from django.urls import path
from . import views 
urlpatterns = [
    path('api-auth/data_repo', views.data_repo),
    path('api-auth/lang_data', views.lang_data),


]