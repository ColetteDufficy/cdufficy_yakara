DROP TABLE IF EXISTS msg_sents;
DROP TABLE IF EXISTS msg_templates;


CREATE TABLE msg_templates (
    id SERIAL PRIMARY KEY,
    msg_title VARCHAR(255) NOT NULL,
    msg_content VARCHAR(255) NOT NULL
);

CREATE TABLE msg_sents (
    id SERIAL PRIMARY KEY,
    recipient_name VARCHAR(255) NOT NULL,
    recipient_email VARCHAR(255) NOT NULL,
    msg_template_id INT REFERENCES msg_templates(id) ON DELETE CASCADE
);

INSERT INTO msg_templates (msg_title, msg_content) VALUES ('Hello Message', E'Hello, \n\nThank you for your call today. \nPlease contact us if you have any further questions. \n\nYakara' );
INSERT INTO msg_templates (msg_title, msg_content) VALUES ('Hello Message', E'Hello, \n\nThank you for your call today. \nPlease contact us if you have any further questions. \n\nYakara' );
INSERT INTO msg_templates (msg_title, msg_content) VALUES ('Thank You Message', E'Thank you. \nYakara' );

INSERT INTO msg_sents (recipient_name, recipient_email, msg_template_id) VALUES ('Ruby', 'Ruby@gmail.com', 1);

