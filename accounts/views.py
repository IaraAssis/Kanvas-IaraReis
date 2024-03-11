from rest_framework import generics
from .serializers import AccountSerializer
from .models import Account


class CreateAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
