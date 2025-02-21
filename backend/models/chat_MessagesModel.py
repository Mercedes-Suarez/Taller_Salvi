class ChatMessage(db.Model):
    __tablename__ = 'chat_messages'

    id_message = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_client = db.Column(db.Integer, db.ForeignKey('clients.id_client'), nullable=False)
    id_employee = db.Column(db.Integer, db.ForeignKey('employees.id_employee'), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    shipping_date = db.Column(db.DateTime, nullable=False)
    ready = db.Column(db.Boolean, nullable=False)