
# import requests
# import json
# headers = {
#     'host': 'app.xiaoyuan.ccb.com',
#     'content-length': '144',
#     'accept': 'application/json, text/plain, */*',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 12; PEGM10 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36jianronghuixue/1.2.7',
#     'content-type': 'application/json;charset=UTF-8',
#     'origin': 'https://app.xiaoyuan.ccb.com',
#     'x-requested-with': 'com.ccb.xiangdaxiaoyuan',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://app.xiaoyuan.ccb.com/LHECRESM/DZK/index2022012101.html',
#     'accept-encoding': 'gzip, deflate',
#     'accept-language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cookie': 'IN031=31002|YWO2l; sid=845401db-9038-4890-a691-9cc10485d7fb; tgw_l7_route=608417dba25267713d0f2b720788c555; IN008=8002|Yg+8c; IN001=1002|Yg+8g; IN010=10003|Yg+8h',
# }

# body = {
#   "stuClass": "9999",
#   "schoolId": "10530",
#   "schoolName": "湘潭大学",
#   "stId": "201705800130",
#   "userId": "A3231003158107633243904008",
#   # "stName": "王天睿",
#   # "locationAddr": "北京市朝阳区黄木厂路",
#   # "id": "D839DCC92AAF53D1E0539349FD0A51BF",
#   "departments": "50eeac63789e4c78810a0d6571a77652",
#   "isContact": "N",
#   "isFever": "0",
#   "isWuhan": "N",
#   "nowArea": "a",
#   # "nowArea": "北京市海淀区",
#   "familyaddress": "b",
#   # "familyaddress": "中关村制造大街",
#   # "familyStatus": "0",
#   # "diagnosisTreatment": "",
#   # "nowStatus": "0",
#   "healthStatus": "3",
#   # "isLevel": "N",
#   # "isbackLive": "N",
#   # "trafficTool": "",
#   # "backTrafficTool": "",
#   # "levelDate": "",
#   # "backtime": "",
#   # "arriveAddr": "",
#   # "trafficNo": "",
#   # "backTrafficNo": "",
#   # "professional": "9D7B8587B3C74DA8E0539349FD0A7824",
#   # "personType": "",
#   # "temperature": "36",
#   # "remarks": "每周一次核酸检测 2月13日阴性",
#   "isAppearDiagnosis": "N",
#   "isVaccinate": "0",
#   "otherDesc": "1",
#   "isContactWithDiagnosis": "N",
#   # "isInSchool": "",
#   "stMobile": "15773211225"
# }
# response = requests.post('https://app.xiaoyuan.ccb.com/channelManage/outbreak/addOutbreak', headers=headers, data = json.dumps(body))
# print(response.text)



import requests
import json
headers = {
    'host': 'app.xiaoyuan.ccb.com',
    'content-length': '144',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; PEGM10 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36jianronghuixue/1.2.7',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.xiaoyuan.ccb.com',
    'x-requested-with': 'com.ccb.xiangdaxiaoyuan',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://app.xiaoyuan.ccb.com/LHECRESM/DZK/index2022012101.html',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'IN031=31002|YWO2l; sid=845401db-9038-4890-a691-9cc10485d7fb; tgw_l7_route=608417dba25267713d0f2b720788c555; IN008=8002|Yg+8c; IN001=1002|Yg+8g; IN010=10003|Yg+8h',
}

body = {
  "stuClass": "9999",
  "schoolId": "10530",
  "schoolName": "湘潭大学",
  # "stId": "201705800131",
  "stId": "201705800130",
  "userId": "A3231003158107633243904008",
  # "stName": "王天睿",
  # "locationAddr": "北京市朝阳区黄木厂路",
  # "id": "D839DCC92AAF53D1E0539349FD0A51BF",
  "departments": "50eeac63789e4c78810a0d6571a77652",
  "isContact": "N",
  "isFever": "0",
  "isWuhan": "N",
  "nowArea": "a",
  # "nowArea": "北京市海淀区",
  "familyaddress": "b",
  # "familyaddress": "中关村制造大街",
  "healthStatus": "3",
  "isAppearDiagnosis": "N",
  "isVaccinate": "0",
  "otherDesc": "1",
  "isContactWithDiagnosis": "N",
  "stMobile": "15773211225"
}
response = requests.post('https://app.xiaoyuan.ccb.com/channelManage/outbreak/addOutbreak', headers=headers, data = json.dumps(body))
print(response.text)