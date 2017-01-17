#Uznavaka (c) 2017, 5n6r. Under MIT License
#!/usr/bin/env python3
import requests,urllib.request,sys,time, json
#urllib.request.urlretrieve(ulng,str(nog)+".jpg")
print("Узнавака версия 0.1 "+chr(169)+" 2017, 5n6r")
f = open("vkgbd.txt","a")
for i in range(0,99999999):
 nmgr=str(i)
 url2="https://api.vk.com/method/groups.getById?group_ids="+nmgr
 r2 = requests.get(url2)
 s2=r2.json()
 try:
  nmg=s2["response"][0]["name"]
  idg=s2["response"][0]["gid"]
  print("Группа с gid: "+str(idg)+" называется: "+nmg)
  f.write("Группа с gid: "+str(idg)+" называется: "+nmg+"\n")
 except KeyError:
  err=s2["error"]["error_msg"]
  print("Sorry, but... "+err)
 time.sleep(0.25)
f.close()
print("Готово!")
