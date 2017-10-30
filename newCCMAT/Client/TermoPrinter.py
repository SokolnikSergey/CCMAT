from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from win32print import GetDefaultPrinter

import cgi
import tempfile
import win32api
from datetime import datetime

class TermoPrinter:
    def __init__(self):
        self.__path_to_logo = "cclogo.jpg"

    def print_on_paper(self,data):

        currency = data["currency"]
        amount = data["amount"]
        reciever_address = data["reciever"]
        date_time = data["date_time"]
        date,time = str(date_time.date()),str(date_time.time())
        cryptomat_location = data['cryptomat_location']
        support = data["support"]

        try:
            currentprinter = GetDefaultPrinter()
            pdf_file_name = tempfile.mktemp(".pdf")
            styles = getSampleStyleSheet()
            h1 = styles["h1"]
            normal = styles["Normal"]

            doc = SimpleDocTemplate(pdf_file_name)

            image = Image(self.__path_to_logo,300,60)
            story = [Spacer(0.5, 0.5 * inch)]
            story.append(image)
            story.append(Spacer(0.5, 2 * inch))
            story.append(Paragraph("<para fontSize=25 fontName='Helvetica-Bold'  alignment = center >Amount of Crypto: {} {}</para>".format(currency,amount), normal))
            story.append(Spacer(0.5, 0.5 * inch))
            story.append(Paragraph("<para fontSize=20 alignment=center>Reciever Address: {}</para>".format(reciever_address), normal))
            story.append(Spacer(0.5, 0.5 * inch))
            story.append(
                Paragraph("<para fontSize=20 alignment=center>Date: {}</para>".format(date),
                          normal))
            story.append(Spacer(0.5, 0.5 * inch))
            story.append(
                Paragraph("<para fontSize=20 alignment=center>Time: {}</para>".format(time),
                          normal))
            story.append(Spacer(0.5, 0.5 * inch))
            story.append(
                Paragraph("<para fontSize=20 alignment=center>Location: {}</para>".format(cryptomat_location),
                          normal))
            story.append(Spacer(0.5, 0.5 * inch))
            story.append(Paragraph("<para fontSize=25 alignment=center>Support: {}</para>".format(support),normal))

            doc.multiBuild(story)
            win32api.ShellExecute(0, "open", pdf_file_name, None, ".", 0)

        except Exception as ex:
            print(ex)



t = TermoPrinter()
t.print_on_paper({"currency": "BTC","amount":0.25,"reciever":1233123123123123,"date_time":datetime.now(),
                'cryptomat_location':"Pushkina Kolontushkina","support":"8-800-555-35-35"})