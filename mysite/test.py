import requests
headers={
    'X-AUTH-TOKEN':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxODI0MjA5MSIsImlhdCI6MTU3NDIzNjU4NywiZXhwIjoxNjA1NzcyNTg3fQ.mnwJT2V_3zQg3wVcF2ZjHdF4wXg4kQZkBFAChK8Tljj6xCzvoOj3P7TPk2BFM1jT6mXcLIPKSt7RuVSo6kfCDw',
    'version':'TYC-Web',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Host':'www.tianyancha.com',
    'Origin':'https://www.tianyancha.com',
    'Referer':'https://www.tianyancha.com/vipintro/?jsid=SEM-BAIDU-PZ1907-SY-000100',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'ssuid=9139757216; aliyungf_tc=AQAAAKSP6ihQ0AcA2B3Gb3Aoc0I4WEcB; csrfToken=CGaq9ckyzAvq1nrs7YeXeTbd; TYCID=357f8fe00b6b11ea9ca85f3f9b6fc438; undefined=357f8fe00b6b11ea9ca85f3f9b6fc438; jsid=SEM-BAIDU-PZ1907-SY-000100; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1574236588; _ga=GA1.2.1264184258.1574236588; _gid=GA1.2.542264972.1574236588; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252243%2525%2522%252C%2522state%2522%253A5%252C%2522surday%2522%253A%2522928%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522145%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522onum%2522%253A%2522107%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxODI0MjA5MSIsImlhdCI6MTU3NDIzNjU4NywiZXhwIjoxNjA1NzcyNTg3fQ.mnwJT2V_3zQg3wVcF2ZjHdF4wXg4kQZkBFAChK8Tljj6xCzvoOj3P7TPk2BFM1jT6mXcLIPKSt7RuVSo6kfCDw%2522%252C%2522vipToTime%2522%253A%25221654333916137%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522post%2522%253A%2522%25E8%25B4%25A2%25E5%258A%25A1%257C%25E4%25BA%25BA%25E5%258A%259B%25E8%25B5%2584%25E6%25BA%2590%257C%25E8%25A1%258C%25E6%2594%25BF%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E4%25B9%259D%25E6%2598%259F%25E6%2583%259F%25E8%25AF%259A%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522companyName%2522%253A%2522%25E5%258C%2597%25E4%25BA%25AC%25E4%25B9%259D%25E6%2598%259F%25E6%2583%259F%25E8%25AF%259A%25E4%25BE%259B%25E5%25BA%2594%25E9%2593%25BE%25E4%25BF%25A1%25E6%2581%25AF%25E6%258A%2580%25E6%259C%25AF%25E6%259C%2589%25E9%2599%2590%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522isExpired%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%252250%2522%252C%2522mobile%2522%253A%252218618242091%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxODI0MjA5MSIsImlhdCI6MTU3NDIzNjU4NywiZXhwIjoxNjA1NzcyNTg3fQ.mnwJT2V_3zQg3wVcF2ZjHdF4wXg4kQZkBFAChK8Tljj6xCzvoOj3P7TPk2BFM1jT6mXcLIPKSt7RuVSo6kfCDw; RTYCID=687f3da060bb47658d02ffebf600b4bf; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1574241914; CT_TYCID=7e72d2dd047840b9a7db82633f0e38d9; cloud_token=f2a4ed18f6b94a80a755a56b76a3acbc; cloud_utm=490c5e3b1bb845f7ac7a19cfdf57895e; _gat_gtag_UA_123487620_1=1'
    }

cookies={
        'HMACCOUNT':'3D726065B88963BB',
        'HMVT':'e92c8d65d92d534b0fc290df538b4758|1574236588|',
        'Hm_ck_1574236588135':'',
        'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758':'1574236588',
        'Hm_lvt_e92c8d65d92d534b0fc290df538b4758':'1574236588',
        'TYCID':'357f8fe00b6b11ea9ca85f3f9b6fc438',
        '_ga':'GA1.2.1264184258.1574236588',
        '_gat_gtag_UA_123487620_1':'1',
        '_gid':'GA1.2.542264972.1574236588',


        'auth_token':'jj6xCzvoOj3P7TPk2BFM1jT6mXcLIPKSt7RuVSo6kfCDw',
         # 'bannerFlag':'undefined',
         'jsid':'SEM-BAIDU-PZ1907-SY-000100',
         'ssuid':'9139757216',
         'tyc-user-info':'522mobile%2522%253A%252218618242091%2522%257D',
         'undefined':'357f8fe00b6b11ea9ca85f3f9b6fc438',


         # 'aliyungf_tc':'AQAAAEu5/FNPgAoA2B3Gb4fluZa21miu',
         # 'aliyungf_tc':'AQAAAEz6pEAoAg4A2B3Gb9Q3cfsSLAFc',
         'aliyungf_tc':'AQAAAKSP6ihQ0AcA2B3Gb3Aoc0I4WEcB',
         'bannerFlag':'',
         'csrfToken':'CGaq9ckyzAvq1nrs7YeXeTbd'


         }


# test = requests.get(url='https://www.tianyancha.com/company/2352677480', headers=headers)
#
# print(test)



#
# class Person:
#     def sayHello(self,name):
#         print("hello,"+name)
#         p = Person()
#         p.sayHello("andy")


def sayHello(self,name):
    print("hello,"+name)

#通过type来创建一个类对象，名称为Person，这个类对象有一个方法sayHello
Person = type("Person",(),{"sayHello":sayHello})

#通过类对象来创建实例
p = Person()

p.sayHello("andy")  # hello andy



from django.db import models
class Employee(models.Model):
    name = models.CharField(maxlength = 50)
    age  = models.IntegerField()