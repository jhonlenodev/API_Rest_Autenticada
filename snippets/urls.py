from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/<int:pk>/higlight/', views.SnippetHighlight.as_view()),

    path('api-auth/', include('rest_framework.urls')),

    path('user/', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('', views.api_root),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)