from django.urls import path
from content.views import (
    ContentUpdateView,
    ContentListView,
    ContentCreateView,
    home_view,
    ContentDeleteView,
)


urlpatterns = [
    path('',home_view, name='home'),
    path('muvi/', ContentListView.as_view(),name='all-muvi'),
    path('muvi/create/', ContentCreateView.as_view(),name='create-muvi'),
    path('muvi/<slug:slug>/', ContentUpdateView.as_view(),name='muvi-details'),
    path('muvi/delete/<slug:slug>', ContentDeleteView.as_view(),name='delete'),
    
    # path('create/',views.create,name='create'),
    # path('edit/<str:movie_id>',views.edit,name='edit'),
    # path('delete/<str:movie_id>',views.delete,name='delete'),
]
