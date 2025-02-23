from backend import db

class Session_tokens(db.Model):
    id_user = db.ForeignKey('User', on_delete=models.CASCADE)
    token = db.CharField(max_length=255)
    creation_date = db.DateTimeField()
    expiration_date = db.DateTimeField()