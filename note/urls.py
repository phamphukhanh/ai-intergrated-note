from django.urls import path
from . import views

urlpatterns = [
    path('edit', views.get_note, name='edit_note'),
    path('add', views.add_note, name='add_note'),
    path('save', views.edit_note, name='save_note'),
    path('delete', views.delete_note, name='delete_note'),
    path('summarize', views.summarize_note, name='summarize_note'),
]
