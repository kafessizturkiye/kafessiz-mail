import random
import webbrowser
adresler = ["ozgeilkim@gmail.com", "ilkim.ozbek@kafessizturkiye.org"]
adres= random.choice(adresler)
adres2=random.choice(adresler)
adres3=random.choice(adresler)
başlıklar = ['beni bırak','kafese hayır']
başlık=random.choice(başlıklar)
metinler = ['kafeslere hayır deyin', 'bu eziyet kabul edilemez', 'şikayetçiyim']
metin=random.choice(metinler)
mail='mailto:'+adres+'?cc='+adres2+'&bcc='+adres3+'&subject='+başlık+'&body='+metin
mail=mail.replace('ı','%C4%B1')
mail=mail.replace('ö','%C3%B6')
mail=mail.replace('ü','%C3%BC')
mail=mail.replace('ş','%C5%9F')
mail=mail.replace('ç','%C3%A7')
mail=mail.replace('ğ','%C4%9F')
mail=mail.replace(' ','%20')

import webbrowser
webbrowser.open(mail)

print(mail)


#mailto:ilkim?body=m%C4%B1km%C3%B6km%C3%BCk%C5%9Fak%C3%A7ak%C4%9Fak%20
#mailto:ilkim?body=m%C4%B1km%C3%B6km%C3%BCk%C5%9Fak%C3%A7ak%C4%9Fak
#mailto:ilkim?body=m%C4%B1k%20m%C3%B6k%20m%C3%BCk%20%C5%9Fak%20%C3%A7ak%20%C4%9Fak
#mailto:ilkim.ozbek@kafessizturkiye.com?body=m%C4%B1k%20m%C3%B6k%20m%C3%BCk%20%C5%9Fak%20%C3%A7ak%20%C4%9Fak

#mailto:ilkim.ozbek@kafessizturkiye.com?cc=ozgeilkim@gmail.com&bcc=ozgeilkim@gmail.com&subject=hek&body=m%C4%B1k%20m%C3%B6k%20m%C3%BCk%20%C5%9Fak%20%C3%A7ak%20%C4%9Fak