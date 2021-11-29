import mailbox
from email.header import decode_header
import re



msgs = mailbox.mbox('source/Novem Workouts.mbox')

for msg in msgs:

    # get email subject
    email_subject = decode_header(msg["Subject"])

    # multi-format body
    email_body = msg.get_payload()

    # find plain text format 
    for a in email_body:
        if "text/plain" == a.get_content_type():
            email_text = a.get_payload() 

    # clean off other text
    clean = re.split('\*\*\sWOD.*\\r\\n',email_text)
    
    # clean = re.split('(NovemFit \& Hybrid)', clean)
    if not len(clean) == 2:
        print(f"email did not parse. Subject: {email_subject}")
        continue
    
    clean = re.split('=3D=3D=3D=3D',clean[1])
    # print(clean[0])


