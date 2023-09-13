import uuid


from django.utils import timezone


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly

# Create your views here.
from .models import Gateway , Payment
from subscriptions.models import Package, Subscription


from .serializers import GatewaySerializer

class GatewayView(APIView):
    def get(self , request):
        gateways = Gateway.objects.filter(is_enable=True)
        seializer = GatewaySerializer(gateways , many=True)
        return Response(seializer.data)

class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self , request):
        gateway_id = request.query_params.get('gateway')
        package_id = request.query_params.get('package')

        try:
            package = package.objects.get(pk = package_id , is_enable = true)
            gateway = gateway.objects.get(pk = gateway_id , is_enable = true)
        except (Package.DoesNotExist , Gateway.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        payment = Payment.objects.create(
            user=request.user,
            package=package,
            gateway=gateway,
            price=package.price,
            phone_number=request.user.phone_number,
            token=str(uuid.uuid4())
        ) 

        return Response({'token' : payment.token , 'callback_url' : 'https://my-site.com/payments/pay/'})

    def post(self , request):
        token = request.data.get('token')
        st = request.data.get('status')

        try:
            payment = Payment.objects.get(token=token)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if st != 10:
            payment.status = Payment.STATUS_CANCEL
            payment.save()
            return Response({'detail' : 'Payment verification failed.'},status=status.HTTP_400_BAD_REQUEST)

        r = requests.post('bank_verify_url' , data={})
        if r.status_code // 100 != 2:
            payment.status = Payment.STATUS_ERROR
            payment.save()

            return Response({'detail' : 'Payment verification failed.'})
        
        payment.status = Payment.STATUS_PAID
        payment.save()

        Subscription.objects.create(
            user=payment.user,
            package=payment.package,
            expire_time=timezone.now() + timezone.timedelta(days=payment.package.duration.days)
        )

        return Response({'detail' : "Payment is successful"})

        