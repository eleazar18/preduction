from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index.html"),
    path('logement/',views.logement,name="logement"),
    path('predire/',views.predire,name="predire")
]