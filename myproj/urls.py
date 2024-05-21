from django.contrib import admin
from django.urls import path
from accounts.views import login_user, logout_user, signup
from student.views import PostCreateView, PostListView, index, post_detail, stage_form,transport_form,logement_form,stage_list,transport_list,LogementListView
from django.conf.urls.static import static
from myproj import settings


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('posts/', PostListView.as_view(), name='post_list'),  # Updated URL pattern for post_list
    path('<str:model_name>/<int:pk>/', post_detail, name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('stage_form/', stage_form, name='stage_form'),
    path('transport_form/', transport_form, name='transport_form'),
    path('logement_form/', logement_form, name='logement_form'),
    path('stage_list/', stage_list, name='stage_list'),
    path('transports/', transport_list, name='transport_list'),
    path('logements', LogementListView.as_view(), name='logement_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
