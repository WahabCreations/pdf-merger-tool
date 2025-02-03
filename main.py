
import PyPDF2
pdffiles = ['Lecture05_GameObjects (1).pdf','Lecture06_Sprites (1).pdf','Lecture08_Sprite Animations.pdf']
merger = PyPDF2.PdfMerger()
for filename in pdffiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')

