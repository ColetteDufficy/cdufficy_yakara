DROP TABLE IF EXISTS msg_sent;
DROP TABLE IF EXISTS msg_templates;


CREATE TABLE msg_templates (
    id SERIAL PRIMARY KEY,
    msg_title VARCHAR(255) NOT NULL,
    msg_content VARCHAR(255) NOT NULL
);

CREATE TABLE msg_sent (
    id SERIAL PRIMARY KEY,
    recipient_name VARCHAR(255) NOT NULL,
    recipient_email VARCHAR(255) NOT NULL,
    msg_template_id INT REFERENCES msg_templates(id) ON DELETE CASCADE
);

INSERT INTO msg_templates (msg_title, msg_content) VALUES ('Hello Message', 'Hello, \nThank you for your call today. \nPlease contact us if you have any further questions. \Yakara' );

