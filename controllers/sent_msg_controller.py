from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.msg_template import Msg_template

import repositories.sent_msg_repository as sent_msg_repository
import repositories.msg_template_repository as msg_template_repository


messages_blueprint = Blueprint("messages", __name__)
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
# POST '/' -onchnage event prompts post response to fill preview screen with user-choosen msg_content
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


# # CREATE
# # POST '/message'
# # 'post' the data from the form back to the db so it will persist
# @messages_blueprint.route("/",  methods=['POST'])
# def create_message():

#     user_id = request.form['user_id']
#     location_id = request.form['location_id']
#     review = request.form['review']
#     user = user_repository.select(user_id)
#     location = location_repository.select(location_id)
#     visit = Visit(user, location, review)
#     visit_repository.save(visit)

#     return redirect('/')


