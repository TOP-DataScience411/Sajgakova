source_text=input("Исходный текст: ")
corrected_text = ''
symbol='.,:;!?–—\'\"()*/'
for i in source_text:
    if i in symbol:
        corrected_text=source_text.replace(i," ")
print(f"\nИсправленный текст: {corrected_text}")

#Исходный текст:  Было темно в гостиной. Лаптев, не садясь и держа шляпу в руках, стал извиняться за беспокойство; он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, и его смущала мысль, что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита.
#
#Исправленный текст:  Было темно в гостиной  Лаптев, не садясь и держа шляпу в руках, стал извиняться за беспокойство; он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, и его смущала мысль, что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита

#Не могу понять почему код не убирает некоторые знаки