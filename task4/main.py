import re

def replace_fio_with_n(text):
    re_str = r'[А-Я][а-я]*(-[А-Я][а-я]*)\s[А-Я][а-я]*\s[А-Я][а-я]*'
    new_text = re.sub(re_str, 'N', text)
    return new_text


text = "Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании вину инкриминируемого правонарушения признала в полном объёме и суду показала, что 14 сентября 1876 года, будучи в состоянии алкогольного опьянения от безысходности, в связи с состоянием здоровья позвонила со своего стационарного телефона в полицию, сообщив о том, что у неё в квартире якобы заложена бомба."


res_text = replace_fio_with_n(text)
print(res_text)
