from rest_framework.routers import DefaultRouter

from .views import FeedbackViewset

router = DefaultRouter()
router.register("", FeedbackViewset)


urlpatterns = [] + router.urls
