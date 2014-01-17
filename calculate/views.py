from django.http import HttpResponse
import json
from utils import product

ERROR_MSG_INVALID_INPUT = {'error': 'INVALID_INPUT', 'message': 'Invalid input provided.'}

def index(request):
    values_strings = request.GET.getlist('values')
    try:
        values_ints = map(int, values_strings)
    except ValueError as e:
        err_result = {'details': str(e) }
        err_result.update(ERROR_MSG_INVALID_INPUT)
        json_output = json.dumps(err_result)
        return HttpResponse(json_output, status=400)
    vsum = sum(values_ints)
    vproduct = product(values_ints)
    json_output = json.dumps({'sum': vsum, 'product': vproduct})
    return HttpResponse(json_output)

