'''
Created on 2013-8-15

@author: young
'''
from django.http import HttpResponse

import datetime
from django.http.response import Http404

from django.template.loader import get_template
from django.template import Context



def hello(request):
    #html = current_datetime(request)
    t = get_template('index.html');
    now = datetime.datetime.now()
    html =t.render(Context({'abc':now}))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return html