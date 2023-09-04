class Msg_sent:

    # set up for the construtor of the class Msg_sent. id initially set as None but value will be popluated later when saved to db
    # msg_template is the foreign key
    def __init__(self, recipient_name, recipient_email, msg_template, id = None):
        self.recipient_name = recipient_name
        self.recipient_email = recipient_email
        self.msg_template = msg_template
        self.id = id