from django.urls import path
from .views import homepageView, DocumentsModelUpload, gallery, addLaptopView, showLaptopView
# from .views import simple_upload

urlpatterns=[
    path('',homepageView, name='home'),
    # path('upload/', simple_upload, name='upload'),
    path('addlaptop/', addLaptopView, name='addlaptop'),
    path('showlaptop/', showLaptopView, name='showlaptop'),

    path('dupload/', DocumentsModelUpload, name='dupload'),
    path('showfiles/', gallery, name='showfiles'),

]

