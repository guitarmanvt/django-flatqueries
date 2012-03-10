from django.shortcuts import render_to_response
from models import Query

def run(request, id):
    query = Query.objects.get(pk=id)
    headers = []
    rows = []
    tv = {
        'query': query,
        'headers': headers,
        'rows': rows,        
    }
    return render_to_response('flatqueries/run.html', tv)
