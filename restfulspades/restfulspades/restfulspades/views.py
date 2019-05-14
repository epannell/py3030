from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'rules': reverse('rule-list', request=request, format=format),
        'game': reverse('play-game', request=request, format=format),
    })