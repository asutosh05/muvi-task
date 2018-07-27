from django.urls import path
from content.views import (
    ContentDetailView,
    ContentListView,
    content_createview,
    home_view,
)


urlpatterns = [
    path('',home_view, name='home_view'),
    path('muvi/', ContentListView.as_view(),name='muvi'),
    path('muvi/create/', content_createview),
    path('muvi/<slug:slug>/', ContentDetailView.as_view()),
    
    # path('create/',views.create,name='create'),
    # path('edit/<str:movie_id>',views.edit,name='edit'),
    # path('delete/<str:movie_id>',views.delete,name='delete'),
]
