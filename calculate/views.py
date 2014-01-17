from django.http import HttpResponse
import json
from utils import product

def index(request):
    values_strings = request.GET.getlist('values')
    values_ints = map(int, values_strings)
    vsum = sum(values_ints)
    vproduct = product(values_ints)
    json_output = json.dumps({'sum': vsum, 'product': vproduct})
    return HttpResponse(json_output)

