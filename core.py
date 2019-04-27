def gbk2utf8(inputFileLoc, outputFileLoc):
    with open(inputFileLoc, 'rb') as inputFile:
        raws = inputFile.readlines()
    with open(outputFileLoc, 'w', encoding = 'UTF-8') as outputFile:
        for raw in raws:
            outputFile.write(raw.decode('gbk'))