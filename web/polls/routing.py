from django.conf.urls import url

from polls.consumers import VoteResultConsumer

websocket_urlpatterns = [
    url(r'^ws/vote_results$', VoteResultConsumer),
]
