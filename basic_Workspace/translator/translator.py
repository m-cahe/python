from json import detect_encoding
from googletrans import Translator                      #googletrans -> translator -> detect/translate
                                                        #4.0.0 이상
translator = Translator()

sentence=input("무슨 말을 번역할래? ")
print(translator.detect(sentence).lang, ' : ' , sentence)   #detect:감지하다v

lan=["ko","en","ja","vi"]
result_ko = translator.translate(sentence, dest=lan[0])
result_en = translator.translate(sentence, dest=lan[1])       #translate(${sentence}, dest='${language}) / dest(=destination)
result_ja = translator.translate(sentence, dest=lan[2])
result_vi = translator.translate(sentence, dest=lan[3])

result_lan = [result_ko, result_en, result_ja, result_vi]
for a in result_lan:
    if(translator.detect(sentence).lang == a.dest):            #중복언어 제외
        continue
    print(a.dest," : ",a.text)
