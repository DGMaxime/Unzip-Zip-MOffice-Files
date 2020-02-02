import argparse
import os
import zipfile
import shutil

parser_args = argparse.ArgumentParser()
parser_args.add_argument("-i", "--file", required=True, help="Path to file", type=str)
args = vars(parser_args.parse_args()) # Namespace

# Open archive file
foldername, ext = os.path.splitext(args['file'])
archive = zipfile.ZipFile(args['file'], 'r')
archive.extractall(foldername)

##
# Do what you want...
##

zipf = zipfile.ZipFile(foldername+'_new'+ext, 'w', zipfile.ZIP_DEFLATED, compresslevel=1)
length = len(foldername)
for root, dirs, files in os.walk(foldername):
    folder = root[length:]  # path without the "parent"
    for file in files:
        zipf.write(os.path.join(root, file), os.path.join(folder, file))

zipf.close()
shutil.rmtree(foldername)