import tempfile

from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO


def pdf_miner_extract(pdf_file, password='', pages=0):
    """
    Convert pdf to text arrays
    :param pdf_file:
    :param password:
    :param pages:
    """
    pdf_resource_manager = PDFResourceManager()
    output_stream = StringIO()
    device = TextConverter(pdf_resource_manager, output_stream,
                           laparams=LAParams(char_margin=0.8, detect_vertical=False))
    file_stream = open(pdf_file, 'rb')
    interpreter = PDFPageInterpreter(pdf_resource_manager, device)
    pages_set = []
    for page in PDFPage.get_pages(file_stream, set(), pages, password):
        interpreter.process_page(page)
        pages_set.append(output_stream.getvalue())
        output_stream.truncate(0)
    file_stream.close()
    device.close()
    output_stream.close()
    return pages_set


def pdf_to_text(file_object):
    """
    Converts PDF to giant String using command line tool pdftotext
    :param file_object:
    :return: list fo str
    """
    pdfData = file_object.read()
    tf = tempfile.NamedTemporaryFile()
    tf.write(pdfData)
    tf.seek(0)
    outputTf = tempfile.NamedTemporaryFile()

    if len(pdfData) > 0:
        out, err = subprocess.Popen(["pdftotext", "-layout", tf.name, outputTf.name ]).communicate()
        return outputTf.read()
    else:
        return None