python
import os
import sys

path = '/home/jihoono335/my-first-blog' # 여러분의 유저네임을 여기에 적어주세요.
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())