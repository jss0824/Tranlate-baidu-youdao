import requests
import json
import jsonpath
import execjs

class BaiduTranslateJS(object):
    def __init__(self, query):
        """
        :param query: 待翻译内容

        """
        self.query = query
        self.url = "https://fanyi.baidu.com/v2transapi"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Cookie": "BIDUPSID=C0AB51C407693D9BC714F9DE26F40330; PSTM=1537981507; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __cfduid=d748c0a1ee0c7675032bbf90c1b56b0fb1564369498; H_WISE_SIDS=130610_137150_137734_132923_138359_137485_134726_138436_106370_135846_137971_120222_138490_137717_137979_132911_137690_131246_132551_137749_136680_118878_118872_118841_118827_118791_107319_137176_136431_133352_137901_136863_138147_137088_136194_124632_137104_133847_138479_138343_137468_134046_131423_137703_138177_110085_137866_127969_137912_138152_127416_136636_137208_138250_138303_137619_137450; BAIDUID=443E21AADAE30A617427A231019DCCA2:SL=0:NR=50:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDUSS=NCTGo3UVpBTnkyU3h0R3RPcmpSeHZ2UDJsY2JKOGFHak55TDZEZHBaamVveFZlRVFBQUFBJCQAAAAAAAAAAAEAAABDzU5LbHVjaWVuMDgyNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN4W7l3eFu5dLU; H_PS_PSSID=; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; APPGUIDE_8_2_2=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; delPer=0; PSINO=2; yjs_js_security_passport=3a9d2cd9af8a3e18b0ab32cb39f7b1f0effc226b_1575961537_js; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1575945814,1575945911,1575961536,1575961545; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1575961545; __yjsv5_shitong=1.0_7_a97a6a643e2c1d4730f64162bb8f8333f440_300_1575961546180_60.209.189.124_45af69e7"
        }
        self.data = {
            "from": "en",
            "to": "zh",
            "query": self.query,  # query 即我们要翻译的的内容
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": "",  # sign 是变化的需要我们执行js代码得到
            "token": "10c151d1ebc28b753bebaafe15a19384"  # token没有变化
        }

    def structure_form(self):
        """
        读取js文件，得到sign值
        :return:
        """
        with open('baidu_translate_js.js', 'r', encoding='utf-8') as f:
            ctx = execjs.compile(f.read())

        sign = ctx.call('e', self.query)
        # print(sign)
        self.data['sign'] = sign

    def get_response(self):
        """
        通过构造的新的表单数据，访问api，获取翻译内容
        :return: 翻译结果
        """
        self.structure_form()
        # print(self.data)
        response = requests.post(self.url, headers=self.headers, data=self.data).json()
        # print(response)
        r = response['trans_result']['data'][0]['dst']
        return r

if __name__ == '__main__':
    baidu_translate_spider = BaiduTranslateJS('my world')     #英译汉  如果需要汉译英需要在data参数中改"from": "en","to": "zh",
    result = baidu_translate_spider.get_response()
    print(result)


