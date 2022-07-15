from rest_framework import serializers

from api.models import Todo

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'