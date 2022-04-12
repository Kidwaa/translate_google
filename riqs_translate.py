import os
from google.cloud import translate
from google.cloud import translate_v2 as translate
import csv


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"E:\Selise\RiQS\Translation\TranslationAPI\Google_Cloud_Key.json"
translate_client=translate.Client()


#text = "Kategorie hinzufÃ¼gen"
#target= 'en'

#output=translate_client.translate(text,target)

#print(output)
#def translate_riqs()


German_List = []
with open('German.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        German_List.append(row[0])

def translate_list(lang_list, lang):
    target=lang
    translated_lang=[]
    for text in lang_list:
        output=translate_client.translate(text,lang)
        translated_lang.append(output)


    return translated_lang

Italian=translate_list(German_List, 'it')
French=translate_list(German_List, 'fr')

print(French)
print(Italian)
