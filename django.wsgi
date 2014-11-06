import os,sys
sys.path.append('home/delr/study/ask/env/lib/python2.7')

sys.path.append('/home/delr/study/ask')

os.environ['DJANGO_SETTINGS_MODULE'] = 'cargo.settings'

import django.core.handles.wsgi
application = django.core.handlers.wsgi.WSGIHandler()