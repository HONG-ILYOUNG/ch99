from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [

    # ex) /blog/
    path('', views.PostLV.as_view(), name='index'),

    # ex) /blog/post/
    path('post/', views.PostLV.as_view(), name='post_list'),

    # ex) /blog/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # ex) /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # ex) /blog/archive/2019/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # ex) /blog/archive/2019/nov/
    path('archive/<int:year>/<int:month>/', views.PostMAV.as_view(month_format='%m'), name='post_month_archive'),

    # ex) /blog/archive/2019/nov/10/
    path('archive/<int:year>/<int:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # ex) /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    # ex) /blog/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

    # ex) /blog/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

    # ex) /blog/search/
    path('search/', views.SearchFormView.as_view(), name='search'),

    # ex) /blog/add/
    path('add/', views.PostCreateView.as_view(), name="add",),

    # ex) /blog/change/
    path('change/', views.PostChangeLV.as_view(), name="change",),

    # ex) /blog/99/update/
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name="update",),

    # ex) /blog/99/delete/
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete",),

]
