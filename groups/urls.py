from django.urls import path
from groups import views
from groups.views import JoinGroupView, LeaveGroupView

urlpatterns = [
    path('groups/', views.GroupList.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
    path('groups/<int:pk>/join/', JoinGroupView.as_view()),
    path('groups/<int:pk>/leave/', LeaveGroupView.as_view()),
]
