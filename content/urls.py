from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home_view'),
    path('muvi/', views.ContentListView.as_view(),name='muvi'),
    path('muvi/<slug:slug>/', views.ContentDetailView.as_view()),
    # path('create/',views.create,name='create'),
    # path('edit/<str:movie_id>',views.edit,name='edit'),
    # path('delete/<str:movie_id>',views.delete,name='delete'),
]
