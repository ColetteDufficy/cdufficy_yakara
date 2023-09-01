from flask import Flask, render_template

from controllers.msg_template_controller import messages_blueprint

app = Flask(__name__)


app.register_blueprint(messages_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)