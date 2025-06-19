# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from decimal import Decimal


class Cliente(models.Model):
    id = models.AutoField(db_column='IDCliente', primary_key=True)  # Field name made lowercase.
    ragione_sociale = models.CharField(db_column='Cliente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codice = models.CharField(db_column='CodiceCliente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rappresentante = models.CharField(db_column='Rappresentante', max_length=50, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    indirizzo = models.CharField(db_column='Indirizzo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cap = models.CharField(db_column='CAP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    citta = models.CharField(db_column='Città', max_length=50, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paese = models.CharField(db_column='Paese', max_length=50, blank=True, null=True)  # Field name made lowercase.
    esposizione = models.DecimalField(db_column='Esposizione', max_digits=18, decimal_places=4, blank=True, null=True, default=Decimal('0.0000'))  # Field name made lowercase.
    rappresentanza = models.DecimalField(db_column='Rappresentanza', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    viaggio = models.DecimalField(db_column='Viaggio', max_digits=18, decimal_places=4, blank=True, null=True, default=Decimal('0.0000'))  # Field name made lowercase.
    codicemisurazione1 = models.CharField(db_column='CodiceMisurazione1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codicemisurazione2 = models.CharField(db_column='CodiceMisurazione2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codicemisurazione3 = models.CharField(db_column='CodiceMisurazione3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codicemisurazione4 = models.CharField(db_column='CodiceMisurazione4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idrappresentante = models.IntegerField(db_column='IDRappresentante', blank=True, null=True)  # Field name made lowercase.
    noteprivate = models.TextField(db_column='NotePrivate', blank=True, null=True)  # Field name made lowercase.

    class Meta:        
        db_table = 'tblClienti'


class Colore(models.Model):
    id = models.AutoField(db_column='IDColore', primary_key=True)  # Field name made lowercase.
    descrizione = models.CharField(db_column='DescrizioneColori', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, db_column='IDCliente',
                                related_name='colori', blank=True, null=True)
    note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nascosto = models.BooleanField(db_column='nascosto', default=False)

    class Meta:        
        db_table = 'Colori'


class Gruppo(models.Model):
    id = models.AutoField(db_column='IDGruppo', primary_key=True)  # Field name made lowercase.
    descrizione = models.CharField(db_column='DescrizioneGruppo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    piastre = models.BooleanField(db_column='Piastre', blank=True, null=True)  # Field name made lowercase.
    idfornpiastre = models.IntegerField(db_column='IDFornPiastre', blank=True, null=True)  # Field name made lowercase.
    fornpiastre = models.CharField(db_column='FornPiastre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sottovuoto = models.BooleanField(db_column='Sottovuoto', blank=True, null=True)  # Field name made lowercase.
    idfornsottovuoto = models.IntegerField(db_column='IDFornSottovuoto', blank=True, null=True)  # Field name made lowercase.
    fornsottovuoto = models.CharField(db_column='FornSottovuoto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    catena = models.BooleanField(db_column='Catena', blank=True, null=True)  # Field name made lowercase.
    idforncatena = models.IntegerField(db_column='IDFornCatena', blank=True, null=True)  # Field name made lowercase.
    forncatena = models.CharField(db_column='FornCatena', max_length=50, blank=True, null=True)  # Field name made lowercase.
    retorsa = models.BooleanField(db_column='Retorsa', blank=True, null=True)  # Field name made lowercase.
    idfornretorsa = models.IntegerField(db_column='IDFornRetorsa', blank=True, null=True)  # Field name made lowercase.
    fornretorsa = models.CharField(db_column='FornRetorsa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    palissone = models.BooleanField(db_column='Palissone', blank=True, null=True)  # Field name made lowercase.
    idfornpalissone = models.IntegerField(db_column='IDFornPalissone', blank=True, null=True)  # Field name made lowercase.
    fornpalissone = models.CharField(db_column='FornPalissone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telaio = models.BooleanField(db_column='Telaio', blank=True, null=True)  # Field name made lowercase.
    idforntelaio = models.IntegerField(db_column='IDFornTelaio', blank=True, null=True)  # Field name made lowercase.
    forntelaio = models.CharField(db_column='FornTelaio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bottalatura = models.BooleanField(db_column='Bottalatura', blank=True, null=True)  # Field name made lowercase.
    idfornbottalatura = models.IntegerField(db_column='IDFornBottalatura', blank=True, null=True)  # Field name made lowercase.
    fornbottalatura = models.CharField(db_column='FornBottalatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codicemisurazione1 = models.CharField(db_column='CodiceMisurazione1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codicemisurazione2 = models.CharField(db_column='CodiceMisurazione2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codicemisurazione3 = models.CharField(db_column='CodiceMisurazione3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codicemisurazione4 = models.CharField(db_column='CodiceMisurazione4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smeriglio = models.BooleanField(db_column='Smeriglio', blank=True, null=True)  # Field name made lowercase.
    idfornsmeriglio = models.IntegerField(db_column='IDFornSmeriglio', blank=True, null=True)  # Field name made lowercase.
    fornsmeriglio = models.CharField(db_column='FornSmeriglio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colla = models.BooleanField(db_column='Colla', blank=True, null=True)  # Field name made lowercase.
    idforncolla = models.IntegerField(db_column='IDFornColla', blank=True, null=True)  # Field name made lowercase.
    forncolla = models.CharField(db_column='FornColla', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notepiastre = models.CharField(db_column='NotePiastre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notesottovuoto = models.CharField(db_column='NoteSottovuoto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notepalissone = models.CharField(db_column='NotePalissone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notebottalatura = models.CharField(db_column='NoteBottalatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notesmeriglio = models.CharField(db_column='NoteSmeriglio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notecolla = models.CharField(db_column='NoteColla', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, db_column='IDCliente',
                                related_name='gruppi', blank=True, null=True)
    rappresentanza = models.DecimalField(max_digits=18, decimal_places=4, db_column='Rappresentanza',
                                        blank=True, null=True, default=Decimal('0.0000'))
    fisse = models.DecimalField(db_column='Fisse', max_digits=18, decimal_places=4, blank=True, null=True, default=Decimal('0.0000'))  # Field name made lowercase.
    viaggio = models.DecimalField(db_column='Viaggio', max_digits=18, decimal_places=4, blank=True, null=True, default=Decimal('0.0000'))  # Field name made lowercase.
    idprocedura = models.IntegerField(db_column='IDProcedura', blank=True, null=True)  # Field name made lowercase.
    datacreazione = models.DateField(db_column='DataCreazione', blank=True, null=True)  # Field name made lowercase.
    leadtime = models.IntegerField(db_column='LeadTime', blank=True, null=True)  # Field name made lowercase.
    ritardo_lead_time = models.IntegerField(blank=True, null=True, default=0)
    applica_ritardo = models.BooleanField(db_column='applica_ritardo', default=False)

    class Meta:        
        db_table = 'Gruppi'
        
        
class Ordine(models.Model):
    id = models.AutoField(db_column='IDOrdine', primary_key=True)  # Field name made lowercase.
    origine_ordine = models.IntegerField(db_column='OrigineOrdine', blank=True, null=True)  # Field name made lowercase.
    numero_ordine = models.IntegerField(db_column='Nordine', blank=True, null=True)  # Field name made lowercase.
    data_ordine = models.DateField(db_column='Del', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, db_column='IDCliente',
                                related_name='ordini', blank=True, null=True)
    ragione_sociale = models.CharField(db_column='Cliente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rappresentante = models.CharField(db_column='Rappresentante', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data_consegna = models.DateField(db_column='DataCons', blank=True, null=True)  # Field name made lowercase.
    data_comunicata = models.DateField(db_column='DataComunicata', blank=True, null=True)  # Field name made lowercase.
    data_effettiva = models.DateField(db_column='DataEffettiva', blank=True, null=True)  # Field name made lowercase.
    riferimento_ordine = models.CharField(db_column='RifOrd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    evaso = models.BooleanField(db_column='Evaso', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    selezionato = models.BooleanField(db_column='Selezionato', default=False)  # Field name made lowercase.
    pagato = models.BooleanField(db_column='Pagato', default=False)  # Field name made lowercase.
    id_rappresentante = models.IntegerField(db_column='IDRappresentante', blank=True, null=True)  # Field name made lowercase.
    urgenza = models.CharField(db_column='UrgenzaOrdine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esportato = models.BooleanField(db_column='Esportato', default=False)  # Field name made lowercase.
    note_commerciali = models.TextField(db_column='NoteCommerciali', blank=True, null=True)  # Field name made lowercase.
    documento = models.TextField(db_column='Documento', blank=True, null=True)  # Field name made lowercase.
    note_calendario = models.TextField(blank=True, null=True)
    ordine_default = models.BooleanField(db_column='ordine_default', default=False)
    annullato = models.BooleanField(db_column='annullato', default=False)
    is_conto_visione = models.BooleanField(db_column='is_c_visione', default=False)
    data_evaso_ordine = models.DateField(b_column='data_evaso_ordine', blank=True, null=True)
    data_annullato_ordine = models.DateField(db_column='data_annullato_ordine', blank=True, null=True)

    class Meta:        
        db_table = 'tblOrdini'



class DettaglioOrdine(models.Model):
    id = models.AutoField(db_column='IDDettOrd', primary_key=True)  # Field name made lowercase.
    ordine = models.ForeignKey(Ordine, on_delete=models.CASCADE, db_column='IDOrdine',
                                related_name='dettagli', blank=True, null=True)
    gruppo = models.ForeignKey(Gruppo, on_delete=models.PROTECT, db_column='IDGruppo',
                                related_name='dettagli', blank=True, null=True)  # Field name made lowercase.
    articolo = models.CharField(max_length=50, db_column='Articolo', blank=True, null=True)
    colore = models.ForeignKey(Colore, on_delete=models.PROTECT, db_column='IDColore',
                                related_name='dettagli', blank=True, null=True)
    nome_colore = models.CharField(db_column='Colore', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quantita = models.DecimalField(db_column='Quantità', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prezzo = models.DecimalField(db_column='Prezzo', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    id_variante = models.IntegerField(db_column='IDVariante', blank=True, null=True)  # Field name made lowercase.
    lead_time = models.IntegerField(db_column='LeadTime', blank=True, null=True)  # Field name made lowercase.
    id_rev_colore = models.IntegerField(db_column='id_rev_colore', blank=True, null=True)
    ritardo_lead_time = models.IntegerField(db_column='ritardo_lead_time', blank=True, null=True, default=0)
    costo_mq = models.DecimalField(max_digits=18, decimal_places=4, db_column='costo_mq', blank=True, null=True)
    note = models.TextField(db_column='note', blank=True, null=True)
    ordine_chiuso = models.BooleanField(db_column='ordine_chiuso', default=False)
    ordine_annullato = models.BooleanField(db_column='ordine_annullato', default=False)
    non_fatturare = models.BooleanField(db_column='non_fatturare', default=False)
    data_chiusura_ordine = models.DateField(db_column='data_chiusura_ordine', blank=True, null=True)
    data_non_fatturare_ordine = models.DateField(db_column='data_non_fatturare_ordine', blank=True, null=True)

    class Meta:
        db_table = 'tblDettOrdini'

