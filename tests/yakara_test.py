import unittest
from models.msg_sent import Msg_sent
from models.msg_template import Msg_template


class TestTask(unittest.TestCase):

    def setUp(self):
        self.msg_template = Msg_template("Hello", "This message is saying hello")    
        self.msg_sent = Msg_sent("Ms Tester Recipient", "tester@yakara.com", 2) 

    def test_msg_template_has_title(self):
        self.assertEqual("Hello", self.msg_template.msg_title)

    def test_msg_template_has_content(self):
        self.assertEqual("This message is saying hello", self.msg_template.msg_content)

    def test_sent_msg_has_recipient(self):
        self.assertEqual("Ms Tester Recipient", self.msg_sent.recipient_name)

    def test_sent_msg_has_email(self):
        self.assertEqual("tester@yakara.com", self.msg_sent.recipient_email)


