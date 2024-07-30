from django.urls import path
from primeapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.register),
    path('login/',views.user_login),
    path('logout/',views.user_logout),
    path('home/',views.home),
    path('moviedetails/<int:id>/',views.movie_detail, name='movie_detail'),
    path('moviepage/', views.moviessection),
    path('seriespage/',views.tvshowssection),
    path('series/<int:id>/', views.series_detail, name='series_detail'),
    path('watch/<int:id>/', views.watchvideo, name='watchvideo'),
    path('video/<int:id>/', views.watchseries, name='seriesvideo'),
    path('action/',views.action),
    path('horror/',views.horror),
    path('comedy/',views.comedy),
    path('drama/',views.drama),
    path('romance/',views.romance),
    path('kids/',views.kids),
    path('mystery/',views.mystery),
    path('scifi/',views.scifi),

    #for payment 
     path('plans/', views.plans_view, name='plans'),
     path('payment/<str:plan_id>/<int:amount>/', views.payment_view, name='payment'),
] 
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)