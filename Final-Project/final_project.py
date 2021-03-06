# #Mengimport Modul Package yang dibutuhkan (sumber : https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# #Mengimport Modul Input Password tidak kelihatan (sumber : https://ganishare.blogspot.com/2018/12/input-password-python-getpass.html)
import getpass
import stdiomask #mengimport package input password menjadi tanda bintang

#membuat variabel dari dan ke banyak penerima melalui file txt (sumber : https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib/51931160#51931160)
fromaddr = "belajarpython030201@gmail.com"

#membaca tujuan file.txt
ke = open('file.txt', 'r+')
toaddr1 = [i.strip() for i in ke.readlines()]
# membuat object from, to dan subject
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr1)
msg['Subject'] = "Pengiriman Pesan via Python"

#menambahkan isi pesan
body = "Ini adalah contoh pengiriman pesan melalui Python"
msg.attach(MIMEText(body, 'plain'))

#menambahkan lampiran
filename = "tes.docx"
attachment = open("D:\\tes.docx","rb")

part = MIMEBase("application", "octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header("content-Disposition", "attachement; filename= {}".format(filename))

msg.attach(part)

#menentukan server emailnya
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#memasukan password email
pwd = stdiomask.getpass('password = ')
server.login(fromaddr, pwd)

#mengirim pesan via server
text = msg.as_string()
server.sendmail(fromaddr, toaddr1, text)
print("Email Sent!")
server.quit()