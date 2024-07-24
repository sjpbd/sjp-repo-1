from django.urls import path
from . import views
from .views import AlbumListView, AlbumDetailView, PhotoDetailView

app_name = 'home'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("slider/", views.slider, name="slider"),
    path("members/", views.members, name="members"),
    path("obituary/", views.obituary_view, name="obituary"),
    path("contact/", views.contact, name="contact"),
    path('detailed-about/', views.detailed_about, name='detailed_about'),
    path('detailed-holyones/', views.detailed_holyones, name='detailed_holyones'),
    path('api/saint/<int:saint_id>/', views.saint_detail_api, name='saint_detail_api'),
    path('school-table/', views.school_table, name='school_table'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('chapters/', views.chapter_list, name='chapter_list'),
    path('chapters/<int:pk>/', views.chapter_detail, name='chapter_detail'),
    path('album_list/', AlbumListView.as_view(), name='album_list'),
    # path('<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('albums/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('<slug:album_slug>/<slug:slug>/', PhotoDetailView.as_view(), name='photo_detail'),

]