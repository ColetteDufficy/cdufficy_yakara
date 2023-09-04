from db.run_sql import run_sql
from models.msg_template import Msg_template


# select_all() method to access ALL templated messages in the db, so that they can be accessed in the drop down menu
# select_all()
def select_all():
    msg_templates = []

    sql = "SELECT * FROM msg_templates"
    results = run_sql(sql)

    for row in results:
        msg_template = Msg_template(row['msg_title'], row['msg_content'], row['id'])
        msg_templates.append(msg_template)
    return msg_templates



# selct(id) method so that once useer has chosen a msg_title, the corresponding msg_content will appear in preview window
# select by specific id
def select(id):
    msg_template = None
    
    sql = "SELECT * FROM msg_templates WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        row = result[0]  
        msg_template = Msg_template(row['msg_title'], row['msg_content'], row['id'])
    return msg_template