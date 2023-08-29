from db.run_sql import run_sql

from models.msg_sent import Msg_sent #importing the class of Msg_sent to be used in CRUD



#SAVE
def save(msg_sent):
    sql = """
        INSERT INTO msg_sent (recipient_name, recipient_email, msg_template_id) 
        VALUES (%s, %s, %s) 
        RETURNING *
    """
    #i dont insert a value ie '%s' for the id value here, because it hasnt been generated yet - because its a new item, and thereore doesnt have an id yet. Thats why its listed as None in the def init on msg_sent.py file
    
    values = [
        msg_sent.recipient_name, 
        msg_sent.recipient_email, 
        msg_sent.msg_template.id
        ]
    
    results = run_sql(sql, values)
    id = results[0]['id'] #this is telling it where to find the 'id' number once its been generated in the 'dictionary'  - see run_sql file for defintion of the the dctionary
    msg_sent.id = id
    return msg_sent