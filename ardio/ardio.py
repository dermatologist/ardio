import sys
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

def process_args(inputfile: str, outputfile: str):
    print('{0} is the input and {1} is output'.format(inputfile, outputfile))

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Usage: ardio inputfile outputfile")
        process_args("/home/beapen/scratch/ardio/pdf/article1.pdf",
                     "/home/beapen/scratch/ardio/pdf/article1.mp3")
    else:
        process_args(sys.argv[1], sys.argv[2])

