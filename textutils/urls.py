from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[ 
    path('admin/',admin.site.urls),
    path('',views.index, name='index'),
    path('analyze',views.analyze, name='analyze'),
    path('removepunc',views.analyze, name='analyze'),

    # path('capitalizefirst',views.capitalizefirst, name='capfirst'),
    # path('newlineremove',views.newlineremove, name='newlineremove'),
    # path('spaceremove',views.spaceremove, name='spaceremove'),
    # path('charcount',views.charcount, name='charcount'),
    

]