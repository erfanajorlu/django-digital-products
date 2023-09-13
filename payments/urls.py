from django.urls import path

from .views import GatewayView , PaymentView

urlpatterns = [
    path('payment/' , PaymentView.as_view()),
    path('gateway/' , GatewayView.as_view())
]