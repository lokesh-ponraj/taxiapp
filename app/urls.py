from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name='home'),
  path('driverlogin/', views.driverLogin, name='driverLogin'),
  path('register/', views.register, name='register'),
  path('driverregister/', views.driverRegister, name="driverRegister"),
  path('bookings/', views.bookings, name="bookings"),
  path('makeBooking/', views.makeBooking, name='makeBooking'),
  path('mybookings/', views.mybookings, name='mybookings'),
  path('<int:id>', views.viewBooking, name="viewbooking"),
  path('driverbookingview/<int:id>',views.driverbookingView, name="driverbookingview"),
  path('billpage/<int:id>', views.billpage, name="billpage"),
  path('logout/', views.logoutApp, name='logout'),
]
