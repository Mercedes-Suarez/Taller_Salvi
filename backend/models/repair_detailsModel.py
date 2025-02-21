class Repair_details(models.Model):
    id_order = models.ForeignKey('RepairOrder', on_delete=models.CASCADE)
    description = models.TextField()
    id_replacement = models.ForeignKey('SparePartInventory', on_delete=models.CASCADE)
    amount = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   