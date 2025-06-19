from rest_framework import viewsets
from django.db.models import Q, Exists, OuterRef
from .models import Ordine, Cliente, DettaglioOrdine, Colore, Gruppo
from .serializers import (
    OrdineSerializer,
    ClienteSerializer,
    DettaglioOrdineSerializer,
    ColoreSerializer,
    GruppoSerializer
)


class OrdineViewSet(viewsets.ModelViewSet):
    queryset = Ordine.objects.all()
    serializer_class = OrdineSerializer
    
    def get_queryset(self):
        ordini_base = Ordine.objects.exclude(Q(data_evaso_ordine__isnull=False) | Q(data_annullato_ordine__isnull=False))
        
        dettagli_invalidi = DettaglioOrdine.Objects.filter(
            Q(ordine=OuterRef('pk')) &
            (Q(ordine_chiuso=True) | Q(ordine_annullato=True))
        )
        return ordini_base.annotate(
                                    ha_dettagli_invalidi=Exists(dettagli_invalidi)).filter(ha_dettagli_invalidi=False)
        
class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DettaglioOrdineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DettaglioOrdine.objects.all()
    serializer_class = DettaglioOrdineSerializer

class ColoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Colore.objects.all()
    serializer_class = ColoreSerializer

class GruppoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gruppo.objects.all()
    serializer_class = GruppoSerializer