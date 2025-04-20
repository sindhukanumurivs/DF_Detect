from django.urls import path
from .views import signup 
from .views import verify_otp,login,logout,submit_report,clear_history,detect,index,upload_video,imagedetect,history,get_history_details,metadatavideo,download_metadata# Import signup view
from django.conf import settings
from django.conf.urls.static import static
from .views import image_metadata, download_image_metadata 
from django.contrib.auth import views as auth_views
from  myapp import views
urlpatterns = [
    path('index/submit_report/', submit_report, name='submit_report'),
    path('signup', signup, name='signup'),
    path('', detect, name='detect'),
    path('verify_otp/', verify_otp, name='verify_otp'), 
    path('login/', login, name='login'),
    path('reset_done/login/', login, name='login'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('index/', index, name='index'),
    path('index/history/', history, name='history'),
    path('index/history/clear_history/', clear_history, name='clear_history'),
    path('index/history/get_history_details/<int:item_id>/', get_history_details, name='get_history_details'),
    path('index/upload_video/', upload_video, name='video'), 
    path('upload_video/', upload_video, name='upload_video'), 
    #path('index/metadata/', metadata, name='metadata'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
   
    path('index/imagedetect/', imagedetect, name='imagedetect'),
    path('index/imagemetadata/', image_metadata, name='metadataimage'),
    path("index/download_image_metadata/", download_image_metadata, name="download_image_metadata"),
    path('index/videometa/', metadatavideo, name='metadatavideo'),
# Default signup view

    path('index/download-metadata/', download_metadata, name='download_metadata'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)