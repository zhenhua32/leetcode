from imapclient import IMAPClient
import email
from email import policy
import mimetypes
import os

server = IMAPClient("imap.qq.com", ssl=True)
# TODO: replace with your credentials
server.login("your_email@qq.com", "your_code")
select_info = server.select_folder("INBOX", readonly=True)
messages = server.search(["SINCE 05-Jul-2021"])


# parse email
for uid, message_data in server.fetch(messages[:1], "RFC822").items():
    email_message = email.message_from_bytes(message_data[b"RFC822"], policy=policy.default)

    # print headers
    for key, val in email_message.items():
        print(key, val)

    print()
    print(email_message.is_multipart())
    print(email_message.get_content_type())
    print()

    # save content
    counter = 1
    for part in email_message.walk():
        # multipart/* are just containers
        if part.get_content_maintype() == "multipart":
            continue
        # Applications should really sanitize the given filename so that an
        # email message can't be used to overwrite important files
        filename = part.get_filename()
        if not filename:
            ext = mimetypes.guess_extension(part.get_content_type())
            if not ext:
                # Use a generic bag-of-bits extension
                ext = ".bin"
            filename = f"part-{counter:03d}{ext}"
        counter += 1
        with open(os.path.join("./email", filename), "wb") as fp:
            fp.write(part.get_payload(decode=True))
