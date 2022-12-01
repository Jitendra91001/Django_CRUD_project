from django.urls import path

from user import views

urlpatterns = [
    path('',views.home, name='indexdata'),
    path('delete/<int:id>/', views.datadelete, name='deletedata'),
    path('<int:id>/',views.dataupdate, name='updatedata'),
]
