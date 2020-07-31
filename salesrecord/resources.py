from import_export import resources
from .models import Salesrecord

class SalesResource(resources.ModelResource):
    class Meta:
        model = Salesrecord
