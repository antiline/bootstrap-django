from django.urls import include, path

from apps.domains.hello_world import urls as hello_world_urls

urlpatterns = [
    path('hello-world/', include(hello_world_urls, namespace='hello_world')),
]
