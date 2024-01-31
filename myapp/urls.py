from django.urls import path,re_path
from . import views
urlpatterns =[
    path('hello/',views.hello),
    path('home/',views.home),
    path('dish/',views.menuitem),
    path('menu/',views.menuitems),
    path('great/<str:name>', views.great),
    path('addition/<int:num1>/<int:num2>', views.addition),
    path('add/',views.add),
    re_path(r'^user/(?P<username>[a-zA-Z]+)/$',views.user_profile),
    re_path(r'^item/(?P<item_id>\d+)/$',views.items),
    re_path(r'^info/(?P<month>\d{2})/(?P<year>\d{4})/$',views.info),
    # re_path(r'^post/(?P<post>[\w-]+)/$', views.post),
    
    re_path(r'^restaurant/(?P<category>[\s\w$-%]*)/?(?P<subcategory>[\w]*)/?$',views.restuarant),
    path('about/',views.about),
    path('menus/',views.menus),
    path('menu1/',views.menu1),
]
