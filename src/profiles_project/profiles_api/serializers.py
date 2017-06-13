from rest_framework import serializers

class HelloSerealizer(serializers.Serializer):

    name = serializers.CharField(max_length=10)
