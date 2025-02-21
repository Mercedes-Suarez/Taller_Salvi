class Session_tokens(models.Model):
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    expiration_date = models.DateTimeField()