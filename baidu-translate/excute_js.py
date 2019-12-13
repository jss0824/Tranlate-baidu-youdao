import execjs
import os


query = 'Hello spider'
with open('baidu_translate_js.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())

sign = ctx.call('e',query)
print(sign)






