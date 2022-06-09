from django.urls import path
from Posts import views as posts_views

urlpatterns = [
    # path('forum/<str:name>', posts_views.forum_blog, name='forum'),
    # path('/www.aravaliinsight.wordpress.com/', posts_views.edboard, name='edboard'),
    path('forum/sagar/', posts_views.sagar, name='sagar'),
    path('forum/vasundhara/', posts_views.vasundhara, name='vasundhara'),
    path('forum/srishti/', posts_views.srishti, name='srishti'),
    path('forum/himgiri/', posts_views.himgiri, name='himgiri'),
    path('forum/societies/', posts_views.societies, name='societies'),
    path('forum/amun/', posts_views.amun, name='amun'),
    path('forum/school/', posts_views.school, name='school'),
    path('forum/environment/', posts_views.environment, name='environment'),
    path('forum/socialinitiatives/', posts_views.socialinitiatives, name='socialinitiatives'),
    path('forum/roundsquare/', posts_views.roundsquare, name='roundsquare'),
    path('forum/sports/', posts_views.sports, name='sports'),
    path('<slug:slug_link>', posts_views.curpost, name='curpost'),
]
