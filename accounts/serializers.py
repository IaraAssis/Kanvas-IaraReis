from rest_framework import serializers
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        if validated_data["is_superuser"]:
            account = Account.objects.create_superuser(**validated_data)
        else:
            account = Account.objects.create_user(**validated_data)
        return account
