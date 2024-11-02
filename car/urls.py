
from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.Add_Car,name='addcar'),
    path('details/<int:id>/' ,views.DetailCarView.as_view(),name='detailcar'),
    path('Signup/',views. SignUp.as_view(),name='signup'),
    path('login/', views.UserloginView.as_view(), name='login'),
    path('Profile/', views.UserProfile, name='Profile'),
    path('Profile/edit/user/data/<int:id>/', views.UserProfileEdit.as_view(), name='EditUserData'),
    path('Logout/', views.UserProfileLogout.as_view(), name='logout'),
    path('buycar/<int:Car_id>/',views.buy_now,name="buy_car"),
]
