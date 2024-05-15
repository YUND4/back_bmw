from rest_framework import routers
from .viewset import CapViewset


router = routers.DefaultRouter()

router.register(r'caps', CapViewset)