from pathlib import Path
from typing import Union, Optional
from . import email

def uniquify(path:Union[str,Path], counter:int=0):
    if isinstance(path, str):
        path = Path(path)
    path = path.resolve()
    if counter != 0:
        candidate_path = path.parent / f"{path.stem}({counter}){path.suffix}"
    else:
        candidate_path = path
    if not candidate_path.exists():
        return candidate_path
    counter += 1
    return uniquify(path, counter)

def make_draft_email(
    path:Union[str,Path],
    subject:str="",
    body:str="",
    attachments:Optional[list]=None,
    recipients:Optional[list]=None
):
    if attachments is None:
        attachments = []
    if recipients is None:
        recipients = []
    email.create_email_file(
        recipients=recipients,
        subject_text=subject,
        out_path=path,
        attachments=attachments,
        )
    # if isinstance(path, str):
    #     path = Path(path)
    # path = uniquify(path)
    # with path.open("w") as f:
    #     f.write(f"Subject: {subject}\n")
    #     f.write(f"\n")
    #     f.write(f"{body}\n")
    # if attachments is not None:
    #     for attachment in attachments:
    #         if isinstance(attachment, str):
    #             attachment = Path(attachment)
    #         attachment = attachment.resolve()
    #         attachment_link = uniquify(path.parent / attachment.name)
    #         attachment_link.symlink_to(attachment)
    #         with path.open("a") as f:
    #             f.write(f"\n")
    #             f.write(f"{attachment_link}\n")
    # return path
