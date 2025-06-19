from rest_framework import serializers
from .models import Cliente, Ordine, DettaglioOrdine, Colore, Gruppo

class ColoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colore
        fields = '__all__'
        
class GruppoSerializer(serializers.ModelSerializer):
    colori = ColoreSerializer(many=True, read_only=True)
    class Meta:
        model = Gruppo
        fields = '__all__'
        read_only_fields = ('colori',)
        
class DettaglioOrdineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DettaglioOrdine
        fields = '__all__'
        
class OrdineSerializer(serializers.ModelSerializer):
    data_scadenza = serializers.DateField(write_only=True, required=False)
    dettagli = DettaglioOrdineSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ordine
        fields = ('id', 'cliente', 'data_consegna', 'data_comunicata', 'data_effettiva', 'data_scadenza', 'dettagli')
    
    def to_representation(self, instance):
        """Aggiunge data_scadenza calcolata in output"""
        ret = super().to_representation(instance)
        if instance.data_effettiva:
            ret['data_scadenza'] = instance.data_effettiva
        elif instance.data_comunicata:
            ret['data_scadenza'] = instance.data_comunicata
        else:
            ret['data_scadenza'] = instance.data_consegna
        return ret
    
    def update(self, instance, validated_data):
        """
        Se viene fornita 'data_scadenza' in input,
        aggiorna il campo corretto secondo la priorità:
        - Se esiste già data_effettiva → aggiorna quella
        - Altrimenti se esiste data_comunicata → aggiorna quella
        - Altrimenti → aggiorna data_consegna
        """
        nuova_data = validated_data.pop("data_scadenza", None)
        if nuova_data:
            if instance.data_effettiva is not None:
                instance.data_effettiva = nuova_data
            elif instance.data_comunicata is not None:
                instance.data_comunicata = nuova_data
            else:
                instance.data_consegna = nuova_data
                
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        
        return instance
        
class ClienteSerializer(serializers.ModelSerializer):
    # Annida la lista di ordini del cliente (relazione inversa definita in Ordine.cliente, es. related_name='ordini')
    ordini = OrdineSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ('ordini',)