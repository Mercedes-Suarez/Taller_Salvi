from backend import db

class Repair_details(db.Model):
    id_order = db.ForeignKey('RepairOrder', on_delete=models.CASCADE)
    description = db.TextField()
    id_replacement = db.ForeignKey('SparePartInventory', on_delete=models.CASCADE)
    amount = db.IntegerField()
    unit_price = db.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   