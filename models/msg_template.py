class Msg_template:
    
# set up for the construtor of the class Msg_template. id initially set as None but value will be popluated later when saved to db
    def __init__(self, msg_title, msg_content, id = None):
        self.msg_title = msg_title
        self.msg_content = msg_content
        self.id = id