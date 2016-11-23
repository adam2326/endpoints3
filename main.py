import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote


# create different kinds of responses
class text_response_only(messages.Message):
    """String that stores a message."""
    resp = messages.StringField(1)



# Create the API endpoints
@endpoints.api(name='statistical_tests', version='v1')
class statistical_tests(remote.Service):
    """statistical test API v1"""

    @endpoints.method(message_types.VoidMessage, text_response_only, path = "ttest", http_method='GET', name = "ttest_for_two_sample_means")
    def my_ttest(self, request):
      return text_response_only(resp="hello ttester")

app = endpoints.api_server([statistical_tests])
