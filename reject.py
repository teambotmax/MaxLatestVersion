print (""" 
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ ✯͜͡❂➣ PC Windows + IOS IPAD + CHOME OS + WIN10
┃ ✯͜͡❂➣ เครดิตการแก้ ( ห้ามเปลี่ยนส่วนนี้ )
┃ ✯͜͡❂➣ ไลน์ไอดี :: http://line.me/ti/p/%40jnx0914l
┃ ✯͜͡❂➣ ลิขสิทธิ์ :: http://github.com/teambotmax
┃ ✯͜͡❂➣ ประเทศ :: ไทย ( Thailand )
┃ ✯͜͡❂➣ ผู้สร้าง :: แม็กซ์ บินแหลก ( TEAM BOT MAX )
┃ ✯͜͡❂➣ เวอร์ชั่น :: 10.0.0.0
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
from MaxLatestVersion import *
from time import sleep
try:
    with open('token.txt','r') as lg:
        MAXz = lg.read()
        maxbots = TEAMBOTMAXv2(MAXz)
except:
    maxbots = TEAMBOTMAXv2()
    with open('token.txt','w') as lg:
        lg.write(maxbots.authToken)
print ('++ Auth Token : %s' % maxbots.authToken)
int1 = len(maxbots.getGroupIdsInvited())
if int1 == 0:
    print("✯͜͡❂ ไม่มีกลุ่มที่ค้างเชิญ")
else:
    for groups in maxbots.getGroupIdsInvited():
        print("✯͜͡❂ กำลังปฏิเสธการเชิญกลุ่ม " + maxbots.getGroup(groups).name)
        sleep(2)
        maxbots.rejectGroupInvitation(groups)
    print("\n✯͜͡❂ คุณปฏิเสธ「 " + str(int1) + " 」คำเชิญกลุ่ม")