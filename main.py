import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote


# create different kinds of responses
class textresponseonly(messages.Message):
    """String that stores a message."""
    resp = messages.StringField(1)

# Create the API endpoints
@endpoints.api(name='statisticaltests', version='v1')
class statistics(remote.Service):
    """statistical test API v1"""

    @endpoints.method(message_types.VoidMessage, textresponseonly, path = "ttest", http_method='GET', name = "ttest")
    def myttest(self, request):
        return textresponseonly(resp="hello ttester")

app = endpoints.api_server([statistics])
