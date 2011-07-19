import os

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, cm

here = os.path.dirname(__file__)

def create_document(name, offset = 1):
    c = canvas.Canvas(os.path.join(here, 'src_pdf', name))
    c.translate(0, 297 * mm)
    c.drawString(1 * cm, -(offset) * cm, name)
    c.showPage()
    c.save()

def main():
    create_document("document1.pdf", 1)
    create_document("document2.pdf", 3)
    create_document("document3.pdf", 5)
    create_document("document4.pdf", 7)
    create_document("document5.pdf", 9)

if __name__ == '__main__':
    main()
