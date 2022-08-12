from catbreadbot.api.views import MessageViewSet, BotResponseViewSet, StatisticView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'stats', StatisticView, basename='statistics')
router.register(r'responses', BotResponseViewSet, basename='question')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = router.urls
