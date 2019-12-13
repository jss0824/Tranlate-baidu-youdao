# Tranlate-baidu-youdao
百度翻译和有道翻译的js逆向破解


百度
================
百度翻译接口有两个参数值需要破解，sign值和token值

全局搜索token后发现token的值是不变的，所以可以直接构造出token的值。

接下来全局搜索sign，跟踪到他的加密函数，扣下来js代码放到文件里面运行，缺啥补啥就可以了。


有道
=================
有道接口通过观察有四个参数是动态的，sign,ts,salt,bv

ts 参数是通过 r = “” + (new Date).getTime() 生成； 也就是获取了当前的时间戳

bv参数是通过 t = n.md5(navigator.appVersion) 生成； 也就是 navigator.appVersion 的 MD5 加密

salt参数是通过 i = r + parseInt(10 * Math.random(), 10) 生成 即在 r(就是ts)的基础上在最后一位随机加上一个整数

sign参数是通过 md5(“fanyideskweb” + e + i + “@6f#X3=cCuncYssPsuRUE”)生成

通过逆向js代码就可以破解。
