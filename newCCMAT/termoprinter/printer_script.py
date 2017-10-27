from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer , Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from win32print import GetDefaultPrinter

import cgi
import tempfile
import win32api
try:
  currentprinter = GetDefaultPrinter()
  print(currentprinter)
  
  source_file_name = "README.md"
  pdf_file_name = tempfile.mktemp (".pdf")
  
  styles = getSampleStyleSheet()
  h1 = styles["h1"]
  normal = styles["Normal"]
  
  doc = SimpleDocTemplate(pdf_file_name)
 
  text = cgi.escape (open (source_file_name).read ()).splitlines ()
  
  image = Image("312.png")
  
  story = [Paragraph (text[0], h1)]
  for line in text[1:]:
    story.append (Paragraph (line, normal))
    story.append (Spacer (0.5, 0.1 * inch))
  
  story.append(image)
  doc.multiBuild(story)
  
  win32api.ShellExecute(0, "print", pdf_file_name , None, ".", 0)
  input()
except Exception as ex:
  print(ex)
  input()
  
