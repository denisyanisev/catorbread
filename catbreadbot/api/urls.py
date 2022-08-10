from catbreadbot.api.views import MessageViewSet, BotResponseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'chat', DialogView, basename='chat')
router.register(r'responses', BotResponseViewSet, basename='question')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = router.urls
