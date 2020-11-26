"""
 Copyright (c) 2020 Bell Eapen

 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

import sys
import re
import operator
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
from gtts import gTTS

def main_routine():
    if(len(sys.argv) != 3):
        print("Usage: ardio inputfile outputfile")
    else:
        process_args(sys.argv[1], sys.argv[2])

def process_args(inputfile: str, outputfile: str):
    FINAL_OUTPUT = "Created with Ardio by Bell Eapen at nuchange.com. "
    print('{0} is the input and {1} is output'.format(inputfile, outputfile))
    common_font_size = get_common_font_size(inputfile)
    for page_layout in extract_pages(inputfile):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                if(get_common_font_size_of_element(element) == common_font_size):
                    FINAL_OUTPUT = FINAL_OUTPUT + \
                        remove_all_but_alpabets(element.get_text())
    print(FINAL_OUTPUT)
    write_audio_file(FINAL_OUTPUT, outputfile)

def write_audio_file(content: str, outputfile: str):
    tts = gTTS(content)
    tts.save(outputfile)

def get_common_font_size_of_element(element: LTTextContainer):
    SIZE_COUNT = {}
    for text_line in element:
        for character in text_line:
            if isinstance(character, LTChar):
                if character.size in SIZE_COUNT:
                    SIZE_COUNT[character.size] = SIZE_COUNT[character.size] + 1
                else:
                    SIZE_COUNT[character.size] = 1
    return max(SIZE_COUNT.items(), key=operator.itemgetter(1))[0]


def get_common_font_size(inputfile: str):
    SIZE_COUNT = {}
    for page_layout in extract_pages(inputfile):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    for character in text_line:
                        if isinstance(character, LTChar):
                            if character.size in SIZE_COUNT:
                                SIZE_COUNT[character.size] = SIZE_COUNT[character.size] + 1
                            else:
                                SIZE_COUNT[character.size] = 1
    return max(SIZE_COUNT.items(), key=operator.itemgetter(1))[0]

def remove_all_but_alpabets(input: str):
    regex = re.compile('[\(\)\[\]0-9]')
    return regex.sub('', input).replace("\n", " ").replace("- ", "")


if __name__ == "__main__":
    main_routine()

