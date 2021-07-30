from rest_framework import serializers

class RepoSerializer(serializers.Serializer):
    name = serializers.CharField()
    language = serializers.CharField()
    url = serializers.URLField()
 