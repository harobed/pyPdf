import os, filecmp

here = os.path.dirname(__file__)

from pyPdf import PdfFileWriter, PdfFileReader

def _src_file(name):
    return os.path.join(here, 'src_pdf', name)

def _out_file(name):
    return os.path.join(here, 'out_pdf', name)

def test_concat():
    output = PdfFileWriter()
    output.addPage(PdfFileReader(_src_file('document1.pdf')).getPage(0))
    output.addPage(PdfFileReader(_src_file('document2.pdf')).getPage(0))
    output.addPage(PdfFileReader(_src_file('document3.pdf')).getPage(0))
    output.write(_out_file('test_concat.pdf'))
    assert filecmp.cmp(
        _out_file('test_concat.pdf'),
        _out_file('test_concat.pdf_valid')
    )


def test_insert():
    output = PdfFileWriter()
    output.addPage(PdfFileReader(_src_file('document1.pdf')).getPage(0))
    output.addPage(PdfFileReader(_src_file('document2.pdf')).getPage(0))
    output.insertPage(
        PdfFileReader(_src_file('document3.pdf')).getPage(0),
        1
    )
    output.write(_out_file('test_insert.pdf'))
    assert filecmp.cmp(
        os.path.join(here, 'out_pdf', 'test_insert.pdf'),
        os.path.join(here, 'out_pdf', 'test_insert.pdf_valid')
    )

def test_merge():
    output = PdfFileWriter()

    page0 = PdfFileReader(_src_file('document1.pdf')).getPage(0)
    page0.mergePage(PdfFileReader(_src_file('document2.pdf')).getPage(0))
    page0.mergePage(PdfFileReader(_src_file('document3.pdf')).getPage(0))
    output.addPage(page0)

    output.write(_out_file('test_merge.pdf'))

def test_add_bookmark():
    output = PdfFileWriter()
    output.addPage(PdfFileReader(_src_file('document1.pdf')).getPage(0))
    output.addPage(PdfFileReader(_src_file('document2.pdf')).getPage(0))
    output.addPage(PdfFileReader(_src_file('document3.pdf')).getPage(0))

    output.addBookmark("Document 1", 0)
    output.addBookmark("Document 2", 1)
    output.addBookmark("Document 3", 2)

    output.write(_out_file('test_add_bookmark.pdf'))
