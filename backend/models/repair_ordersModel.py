from backend import db

class Repair_orders(db.Model):
    id_client = db.ForeignKey('Client', on_delete=models.CASCADE)
    start_date = db.DateTimeField()
    end_date = db.DateTimeField()
    status = db.CharField(
        max_length=15,
        choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')]
    )
    total = db.DecimalField(max_digits=10, decimal_places=2)
    id_vehicle = db.ForeignKey('Vehicle', on_delete=models.CASCADE)
    entry_date = db.DateTimeField()
    estimated_delivery = db.DateTimeField()
    estimated_total = db.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    finish_total = db.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
