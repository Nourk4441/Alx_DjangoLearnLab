from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    # Dynamic fields for actor and target details
    actor = serializers.StringRelatedField()
    target_type = serializers.SerializerMethodField()
    target_id = serializers.IntegerField(source='target_object_id')
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target_type', 'target_id', 'target', 'timestamp']
        read_only_fields = ['recipient', 'timestamp', 'actor', 'verb', 'target_type', 'target', 'target_id']

    def get_target_type(self, obj):
        if obj.target_content_type:
            return obj.target_content_type.model
        return None

    def get_target(self, obj):
        if obj.target_content_type and obj.target_object_id:
            target_model = obj.target_content_type.model_class()
            target_instance = target_model.objects.filter(id=obj.target_object_id).first()
            return str(target_instance) if target_instance else None
        return None
