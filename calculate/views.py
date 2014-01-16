from django.http import HttpResponse
import json

def index(request):
    values_strings = request.GET.getlist('values')
    values_ints = map(int, values_strings)
    vsum = sum(values_ints)
    json_output = json.dumps({'sum': vsum})
    return HttpResponse(json_output)

