# Django imports
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
# Local imports
from flatqueries.models import Query

@permission_required('flatqueries.can_run_query')
def run(request, id):
    query = Query.objects.get(pk=id)
    if request.method=='POST':
        (headers, rows) = query.run()
    else:
        headers = rows = None
    tv = {
        'query': query,
        'headers': headers,
        'rows': rows,
    }
    return render(request, 'flatqueries/run.html', tv)
