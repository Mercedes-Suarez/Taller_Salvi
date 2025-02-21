class Payment(models.Model):
    id_invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20,
        choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('Transferencia', 'Transferencia'), ('Otro', 'Otro')]
    )
    payment_date = models.DateTimeField()
    state = models.CharField(max_length=10, choices=[('Pendiente', 'Pendiente'), ('Cobrado', 'Cobrado')])
