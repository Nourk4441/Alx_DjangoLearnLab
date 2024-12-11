def create_notification(recipient, actor, verb, target=None):
    from notifications.models import Notification
    from django.contrib.contenttypes.models import ContentType

    target_ct = ContentType.objects.get_for_model(target) if target else None
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=target_ct,
        target_object_id=target.id if target else None
    )
from rest_framework.generics import ListAPIView
from .serializers import NotificationSerializer

class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.request.user.notifications.order_by('-timestamp')
