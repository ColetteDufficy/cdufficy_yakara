class Msg_sent:

    def __init__(self, recipient_name, recipient_email, msg, id = None):
        self.recipient_name = recipient_name
        self.recipient_email = recipient_email
        self.msg = msg
        self.id = id