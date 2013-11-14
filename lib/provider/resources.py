from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class TransactionViewSet(ViewSet):
    """
    A universal payment provider transaction resource.

    This will support Bango and Zippy transactions with a consistent API.

    Note that in Bango you did this by posting to /bango/billing
    where the concept of starting a transaction was to
    retrieve a BillingConfigId.
    """

    def list(self, request):
        return Response({'not': 'implemented'})
