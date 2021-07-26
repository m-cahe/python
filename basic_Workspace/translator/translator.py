from googletrans import Translator

translator = Translator()
sentence="안녕"
print(translator.detect(text='안녕', desc='en',src='ko'))
