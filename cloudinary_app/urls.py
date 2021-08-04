from cloudinary_app.views import *

from django.urls import path

urlpatterns = [
    path('get-all-imgs/<str:folder>/', get_all_imgs, name="get_all_imgs")
]