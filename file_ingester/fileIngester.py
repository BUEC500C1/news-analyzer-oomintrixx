import os
import textract
from shutil import copyfile

def fileIngest(file_path):
    copyfile(file_path, original_files)
    text = textract.process(file_path)
    
