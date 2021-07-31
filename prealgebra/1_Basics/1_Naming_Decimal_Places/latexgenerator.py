from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Command
from pylatex.utils import italic, NoEscape, verbatim
from pylatex.base_classes import Environment
from pylatex.package import Package

from  section_1 import Decimal_Places
class AllTT(Environment):
    """A class to wrap LaTeX's alltt environment."""
    packages = [Package('alltt')]
    escape = False
    content_separator = "\n"


def fill_document(doc):
    """Add a section, a subsection and some text to the document.
    
    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section('Instruction:')):
        doc.append('Write down the correct decimals place for where the under bar is \n')
        #doc.append(italic('ita'))

        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')
    
    with doc.create(Section('Wrapping Latex Environments')):
        doc.append(NoEscape(
        r"""
        The following is a demonstration of a custom \LaTeX{}
        command with a couple of parameters.
        """))

    # Put some data inside the AllTT environment

    with doc.create(Section('Problems:')):
        with doc.create(Tabular('cccccc')) as table:
            for i in range(30):
                a,b = Decimal_Places("medium", False)    
            print(a)
            table.add_row((verbatim(verbatim(a)), 2, 3, 4, 5, 6))
            table.add_empty_row()
            table.add_empty_row()
            table.add_empty_row()
            table.add_row((7, 8, 9, 10, 11, 12))
            table.add_empty_row()
            table.add_empty_row()
            table.add_empty_row()
            table.add_row((13, 14, 15, 16, 17, 18))
            table.add_empty_row()
            table.add_empty_row()
            table.add_empty_row()
            table.add_row((19, 20, 21, 22, 23, 24))
            table.add_empty_row()
            table.add_empty_row()
            table.add_empty_row()
            table.add_row((25, 26, 27, 28, 29, 30))


if __name__ == '__main__':
    # Basic document
    geometry_options = {"tmargin": "2cm", "bmargin": "2cm"}
    doc = Document('basic', geometry_options=geometry_options)
    
    fill_document(doc)

    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()

    # Document with `\maketitle` command activated
    doc = Document()

    doc.preamble.append(Command('title', 'Naming Decimal Places Worksheet'))
    doc.preamble.append(Command('author', ''))
    doc.preamble.append(Command('date', ''))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    doc.generate_pdf('basic_maketitle', clean_tex=False)

    # Add stuff to the document
    with doc.create(Section('A second section')):
        doc.append('Some text.')

    doc.generate_pdf('basic_maketitle2', clean_tex=False)
    tex = doc.dumps()  # The document as string in LaTeX syntax