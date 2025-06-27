from django.urls import path
from apps.blogs.views import *

urlpatterns = [
   path('blogs/', BlogListAPIFuncView, name='blog_list_api')
]