class Msg_sent:

    def __init__(self, recipient_name, recipient_email, msg_template, id = None):
        self.recipient_name = recipient_name
        self.recipient_email = recipient_email
        self.msg_template = msg_template
        self.id = id