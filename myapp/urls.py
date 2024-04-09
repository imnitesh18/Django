from django.urls import path,re_path
from . import views
from myapp.views import MyView

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
    path('restro/', views.restro),
    path('restroo/<str:item>/', views.restroo, name='restroo'),
    path('home/', views.home, name='home'),
    path('about/', views.home, name='about'),
    path('food/', views.food, name='food'),
    # path('food2/<int:item_id>/', views.food2, name='food2'),
    path('food_detail/<str:item_name>/', views.food_detail, name='food_detail'),
    path('simpleform', views.simpleform, name='simpleform'),
    path('simpleform1', views.simpleform1, name='simpleform1'),
    path('simpleform3', views.simpleform3, name='simpleform3'),
    path('getform/',MyView.as_view(), name='getform'),
    path('postform/',MyView.as_view(), name='postform'),
    # path('css/',views.css,name='css')
    path('validation/',views.validation,name='validation'),
    path('val_django_form/',views.val_django_form),
    path('sign/',views.sign),
    path('sign1/',views.sign1),
    path('blogpost/',views.blogpost),
    path('set_cookie/',views.set_cookie, name='set_cookie'),
    path('success/',views.success_page, name='success_page'),
]
