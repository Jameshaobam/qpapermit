from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name = 'home'),
    path('upload-file',views.upload,name = 'upload'),
    path('search',views.search,name = 'search'),
    path('detail/post_id:<int:pk>/',views.detail,name = 'detail'),
    path('detail/edit/<int:pk>/',views.update,name = 'update'),
    path('detail/delete/<int:pk>/', views.delete, name='delete'),
    path('postanswer/<int:pk>/',views.postanswer,name = 'postanswer'),
    path('update-answer/<int:pk>/ans/<int:ans_id>/',views.update_ans,name = 'update_ans'),
    path('delete_ans/<int:pk>/ans/<int:ans_id>/',views.delete_ans, name = 'delete_ans'),
    path('about-page',views.aboutpage,name = 'aboutpage'),
    path('contact-page',views.contactme,name = 'contactme'),
]
