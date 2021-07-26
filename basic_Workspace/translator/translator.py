from json import detect_encoding
from googletrans import Translator                      #googletrans -> translator -> detect/translate
                                                        #4.0.0 이상
translator = Translator()

sentence=input("무슨 말을 번역할래? ")
print(translator.detect(sentence).lang, ' : ' , sentence)   #detect:감지하다v

result_ko = translator.translate(sentence, dest="ko")
result_en = translator.translate(sentence, dest='en')       #translate(${sentence}, dest='${language}) / dest(=destination)
result_ja = translator.translate(sentence, dest='ja')
result_vi = translator.translate(sentence, dest='vi')

print(result_ko.dest," : ",result_ko.text)
print(result_en.dest,' : ',result_en.text)
print(result_ja.dest,' : ',result_ja.text)
print(result_vi.dest,' : ',result_vi.text)