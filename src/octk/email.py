from email.message import EmailMessage
from pathlib import Path
from typing import Optional, Union
import octk

def create_email_file(
        recipients:list[str],
        subject_text:str="",
        out_path:Optional[Union[str,Path]]=None,
        attachments:Optional[list[Union[str,Path]]]=None,
        # is_draft=True,
):
    if attachments is None:
        attachments=[]
    if out_path is None:
        if not subject_text:
            out_path=octk.uniquify("email.eml")
        else:
            out_path=subject_text 
    msg = EmailMessage()
    msg['Subject'] = subject_text
    msg['To'] = ', '.join(recipients)
    msg.preamble = 'This is a multi-part message in MIME format. You will not see this in a MIME-aware mail reader\n.'

    for attachment in attachments:
        with open(attachment, 'rb') as fp:
            attachment_bytes =  fp.read()
            
        msg.add_attachment(
            attachment_bytes,
            maintype='application', 
            subtype='xlsx', 
            filename=Path(attachment).name
            )

    msg.add_header('X-Unsent', '1')

    with open(out_path, 'wb') as outfile:
        outfile.write(bytes(msg))