from db.run_sql import run_sql

from models.msg_template import Msg_template


# i need select_all() in order to access ALL of the templated messages that are in the db, so that they canm be accessed in the drop down menu

def select_all():
    msg_templates = []

    sql = "SELECT * FROM msg_templates"
    results = run_sql(sql)

    for row in results:
        msg_template = Msg_template(row['msg_title'], row['msg_content'], row['id'])
        msg_templates.append(msg_template)
    return msg_templates