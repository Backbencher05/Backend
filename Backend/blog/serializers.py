from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        title = data.get('title')

        if Post.objects.filter(author=user, title=title).exists():
            raise serializers.ValidationError("You are already have a post with this title.")
        return data