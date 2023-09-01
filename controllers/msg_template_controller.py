from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.msg_template import Msg_template
from models.msg_sent import Msg_sent

import repositories.sent_msg_repository as sent_msg_repository
import repositories.msg_template_repository as msg_template_repository


messages_blueprint = Blueprint("index", __name__)
#blueprint is a place to store lots of routes. ie @app.routes


# RESTful CRUD Routes:
# 1. INDEX
# 2. NEW
# 3. CREATE
# 4. SHOW
# 5. EDIT
# 6. UPDATE
# 7. DELETE

# NEW
# GET '/' requesting all the msg_title so they appear in drop down as options
# POST '/' onchange event prompts POST response to fill preview screen with user-choosen msg_content
@messages_blueprint.route("/", methods=['GET', 'POST'])
def get_all_msg_templates():
    selected_template_msg_content = ""
    selected_template_id = None

    msg_templates = msg_template_repository.select_all()

    if request.method == 'POST':
        # print("Form Data:", request.form)
        selected_template_id = int(request.form['msg_template_id'])

        if selected_template_id:
            selected_template = msg_template_repository.select(int(selected_template_id))
            if selected_template:
                selected_template_msg_content = selected_template.msg_content

        # print("selected_template_id:", selected_template_id)
        # print("selected_template_msg_content:", selected_template_msg_content)

    return render_template("index.html", msg_templates=msg_templates, selected_template_msg_content=selected_template_msg_content, selected_template_id=selected_template_id)


# CREATE
# POST 'msg_sent' back to db as persistent data
@messages_blueprint.route("/sent", methods=['POST'])
def create_msg_sent_to_db():
    recipient_name = request.form['name']
    recipient_email = request.form['email']
    msg_template_id = request.form['msg_template_id']

    msg_template = msg_template_repository.select(msg_template_id)

    msg_sent = Msg_sent(recipient_name, recipient_email, msg_template)
    sent_msg_repository.save(msg_sent)

    # print("msg_sent submiussion:", msg_sent)


    return render_template('sent.html')





