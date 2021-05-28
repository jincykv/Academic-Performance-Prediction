from django.urls import path
from projectapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
	path('',views.index_fun),
	path('register/',views.register),
	path('login/',views.login),
	path('admin_login/',views.admin_login),
	path('Edu_logout/',views.Edu_logout),
	path('pending/',views.view),
	path('approve/',views.approve),
	path('reject/',views.reject),
	path('delete/',views.delete),
	path('view_profile/',views.view_profile),
	path('update/',views.update),
	path('stud_dataset/',views.upload),
	path('prediction/',views.predict),
	
] 
if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

