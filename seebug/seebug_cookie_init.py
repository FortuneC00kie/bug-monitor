#coding:utf-8
import PyV8
import re
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')

headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}

result =''

def get_jsluid(req):
    post_cookie = {}
    rec_cookie = req.headers['Set-Cookie']
    r1 = re.compile(r'__jsluid.*?\;')
    jsluid = re.search(r1, rec_cookie).group(0)[:-1]
    name, value = jsluid.split('=')
    post_cookie[name] = value
    get_jsl_clearance(req, post_cookie)
    return post_cookie

def get_jsl_clearance(req, post_cookie):
    req.encoding = 'utf-8'
    script = req.text.strip().replace("<script>", "")
    script = script.replace("</script>","")
    script = script.replace(";eval", ";document.write")
    script = script.replace("\x00", "")

    class v8Doc(PyV8.JSClass):
        def write(self, s):
            global result
            result = s

    class Global(PyV8.JSClass):
        def __init__(self):
            self.document = v8Doc()
     
    glob = Global()
    ctxt = PyV8.JSContext(glob)
    ctxt.enter()
    ctxt.eval(script)

    script = result.replace("while(window._phantom||window.__phantomas){};","")
    script = script.replace("setTimeout('location.href=location.href.replace(/[\?|&]captcha-challenge/,\\\'\\\')',1500);", "")
    script = script.replace("if((function(){try{return !!window.addEventListener;}catch(e){return false;}})()){document.addEventListener('DOMContentLoaded',l,false);}else{document.attachEvent('onreadystatechange',l);}", "l();");
    script = script.replace("var h=document.createElement('div');h.innerHTML='<a href=\\\'/\\\'>x</a>';h=h.firstChild.href;var r=h.match(/https?:\\/\\//)[0];h=h.substr(r.length).toLowerCase();","var h =\"https://www.seebug.org\";")
    r = re.compile(r'document.cookie.*?\)\;')
    script = re.sub(r, 'document.write(dc)',script)
    try:
    	ctxt.eval(script)
    except:
    	print "seebug反爬虫策略可能已更新，请调整爬虫解析策略"
    	exit()
    name, value = result.split('=')
    post_cookie[name] = value
    return post_cookie

def cookie_init():
    req = requests.get("https://www.seebug.org/vuldb/vulnerabilities")
    return get_jsluid(req)


