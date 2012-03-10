# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
# Local imports
from models import Query

@login_required
def run(request, id):
    query = Query.objects.get(pk=id)
    if request.method=='POST':
        (headers, rows) = query.run()
    tv = {
        'query': query,
        'headers': headers,
        'rows': rows,        
    }
    return render_to_response('flatqueries/run.html', tv)
