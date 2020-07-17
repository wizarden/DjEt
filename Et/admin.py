from django.contrib import admin

# Register your models here.

from .models import Izd
from .models import Harak

admin.site.register(Izd)

admin.site.register(Harak)

