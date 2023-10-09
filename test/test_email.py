import octk

attachment=r"E:\alexa\OneDrive\Projects\Code\Proj\octk\test\data\inputs\test_attachment.txt"
outpath = r"E:\alexa\OneDrive\Projects\Code\Proj\octk\test\data\output\test_email.eml"

octk.make_draft_email(
    path=outpath,
    subject="Test Subject",
    body="Test Body",
    attachments=[attachment]
)