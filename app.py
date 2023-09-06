from flask import Flask, render_template
from flask_mail import Mail, Message

from controllers.msg_template_controller import messages_blueprint

app = Flask(__name__)



app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'b33a25b498cb37'
app.config['MAIL_PASSWORD'] = '261eddc56c000d'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'c.dufficy@gmail.com'
# app.config['MAIL_PASSWORD'] = ''
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


app.register_blueprint(messages_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

# tutorial code:
# def home():
#     msg = Message(subject='Hello from the other side!', sender='peter@mailtrap.io', recipients=['paul@mailtrap.io'])
#     msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
#     mail.send(msg)
#     return "Message sent!"

if __name__ == '__main__':
    app.run(debug=True)