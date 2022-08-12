from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thomas', views.thomas, name='thomas'),
    path('<str:name>', views.greet, name='greet')
    # with this latest path, the greeting will name whatever letters given in the address bar
]
