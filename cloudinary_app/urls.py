from cloudinary_app.views import *

from django.urls import path

urlpatterns = [
    path('get-all-imgs/<str:folder>/', get_all_imgs, name="get_all_imgs"),
    path('upload-categorized-img/<str:folder>/', upload_categorized_img, name="upload_categorized_img"),
    path('get-img-with-effect/<str:folder>/<str:id>/', get_img_with_effect, name="get_img_with_effect"),
    path('get-categorized-img/', get_categorized_img, name="get_categorized_img"),
    path('delete-img/<str:folder>/<str:id>/', delete_img, name="delete_img")
]