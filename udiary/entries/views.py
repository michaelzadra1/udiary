from rest_framework import permissions, viewsets
from rest_framework.response import Response

from entries.models import Entry
from entries.permissions import IsAuthorOfEntry
from entries.serializers import EntrySerializer
	
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.order_by('-created_at')
    serializer_class = EntrySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAuthorOfEntry(),)

def perform_create(self, serializer):
    instance = serializer.save(Account=self.request.user)

    return super(EntryViewSet, self).perform_create(serializer)



class AccountEntriesViewSet(viewsets.ViewSet):
    queryset = Entry.objects.select_related('Account').all()
    serializer_class = EntrySerializer

    def list(self, request, account_id=None):
        queryset = self.queryset.filter(Account__id=account_id)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)