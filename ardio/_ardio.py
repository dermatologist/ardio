from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
# for page_layout in extract_pages("/home/beapen/scratch/ardio/ardio/qrmine.pdf"):
#     for element in page_layout:
#         if isinstance(element, LTTextContainer):
#             for text_line in element:
#                 for character in text_line:
#                     if isinstance(character, LTChar):
#                         print(character.fontname)
#                         print(character.size)

# for page_layout in extract_pages("/home/beapen/scratch/ardio/ardio/qrmine.pdf"):
#     for element in page_layout:
#         print(element)

for page_layout in extract_pages("/home/beapen/scratch/ardio/ardio/qrmine.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            # print(element)
            # print(" : ")
            print(element.get_text())
            print("-------------------------")
