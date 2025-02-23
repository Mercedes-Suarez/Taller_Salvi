from backend import db

class Payment(db.Model):
    id_invoice = db.ForeignKey('Invoice', on_delete=models.CASCADE)
    id_client = db.ForeignKey('Client', on_delete=models.CASCADE)
    amount = db.DecimalField(max_digits=10, decimal_places=2)
    payment_method = db.CharField(
        max_length=20,
        choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('Transferencia', 'Transferencia'), ('Otro', 'Otro')]
    )
    payment_date = db.DateTimeField()
    state = db.CharField(max_length=10, choices=[('Pendiente', 'Pendiente'), ('Cobrado', 'Cobrado')])
