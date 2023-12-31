import pypinyin
import pykakasi

def cn_output(text):
    pinyin = " ".join(pypinyin.lazy_pinyin(text, errors='ignore'))
    return pinyin

def en_output(text):
    pinyin = " ".join(pypinyin.lazy_pinyin(text, errors='ignore'))
    return pinyin

def jp_output(text):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("s", True)
    kakasi.setMode("E", "a")
    converter = kakasi.getConverter()
    jp_output = converter.do(text)
    return jp_output