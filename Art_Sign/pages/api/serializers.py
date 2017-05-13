from rest_framework import serializers

class MembershipSerializer(serializers.Serializer):

    name = serializers.CharField(),
	firstname = serializers.CharField(),
	birthdate = serializers.DateTimeField(),
	postal_code = serializers.IntegerField(max_value=5, min_value=5),
	city = serializers.CharField(),
	adress = serializers.CharField(),
	email_adress = serializers.EmailField(),
	mobile_phone = serializers.CharField(required=false)
	