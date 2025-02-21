class Repair_orders(models.Model):
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(
        max_length=15,
        choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')]
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    id_vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    entry_date = models.DateTimeField()
    estimated_delivery = models.DateTimeField()
    estimated_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    finish_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
