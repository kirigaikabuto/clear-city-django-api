from typing import Tuple
from rest_framework.routers import DefaultRouter

app_name = "applications"
router = DefaultRouter()
urlpatterns: Tuple = router.urls

applications_patterns: Tuple[str, ...] = (

)

urlpatterns += (
    applications_patterns
)
