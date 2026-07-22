from gtts import gTTS #Importing Google Text to Speech library

import pypdf
pdf_File = open('kinderkonten.pdf','rb')

pdf_Reader = pypdf.PdfReader(pdf_File)
count = pdf_Reader.get_num_pages()
textList = []


for i in range (count):
    try:
        page = pdf_Reader.get_page(i)
        textList.append(page.extract_text())
    except:
        pass


textString = "".join(textList)

print(textString)

language = "de"
myAudio = gTTS(text=textString, lang = language, slow=False)
myAudio.save("Audio.mp3")

