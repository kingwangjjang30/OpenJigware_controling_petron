import clr
import time
clr.AddReference("OpenJigWare")
from OpenJigWare import Ojw


COjw = Ojw()
m_CMot = Ojw.CProtocol2()
m_CMot.Open(34, 1000000)


m_CMot.SetTorq(True)
m_CMot.SyncRead(1,2,3,4,5,6,7,8)
m_CMot.Wait(10000)

def init():
    m_CMot.PlayFrameString("S2,500,0,1:0,2:0,3:90,4:0,5:0,6:-90,7:-80,8:-80")

def updawnshaking():
    
    for i in range(50):
        m_CMot.PlayFrameString("S2,2000,0,1:0,2:0,3:70,4:0,5:0,6:-70,7:-80,8:-80")
        m_CMot.PlayFrameString("S2,2000,0,1:0,2:0,3:130,4:0,5:0,6:-130,7:-110,8:-110")

def RLshaking():
    
    for i in range(5):
        m_CMot.PlayFrameString("S2,100,0,1:60,2:60,3:90,4:0,5:0,6:-90,7:-80,8:-80")
        m_CMot.PlayFrameString("S2,100,0,1:-60,2:-60,3:90,4:0,5:0,6:-90,7:-80,8:-80")

def hello():
    m_CMot.PlayFrameString("S2,100,0,1:0,2:0,3:70,4:0,5:0,6:-120,7:-80,8:-70")
    time.sleep(1)
    init()

def loop_motion():
    while(True):
        m_CMot.PlayFrameString("S2,1000,0,1:0,2:0,3:90,4:0,5:0,6:-90,7:-80,8:-80")
        m_CMot.PlayFrameString("S2,2000,0,1:0,2:0,3:90,4:0,5:0,6:-90,7:-80,8:-80")
        m_CMot.PlayFrameString("S2,2000,0,1:0,2:0,3:150,4:0,5:0,6:-150,7:-110,8:-110")
        m_CMot.PlayFrameString("S2,2000,0,1:60,2:60,3:90,4:0,5:0,6:-90,7:-80,8:-80")
        m_CMot.PlayFrameString("S2,2000,0,1:-60,2:-60,3:90,4:0,5:0,6:-90,7:-80,8:-80")


def loop_motion_updawn():
    while(True):
        for i in range(100):
            m_CMot.PlayFrameString("S2,500,0,1:0,2:0,3:90,4:0,5:0,6:-90,7:-80,8:-80")
            m_CMot.PlayFrameString("S2,500,0,1:0,2:0,3:150,4:0,5:0,6:-150,7:-110,8:-110")
        m_CMot.Wait(5000)
        m_CMot.SetTorq(False)
        m_CMot.Wait(300000)
        m_CMot.SetTorq(True)

def shi():
    while(True):
        m_CMot.PlayFrameString("S2,1000,0,1:0,2:0,3:0,4:0,5:0,6:0,7:-80,8:-80")
        m_CMot.PlayFrameString("S2,1000,0,1:30,2:30,3:90,4:0,5:0,6:-90,7:-80,8:-80")
        m_CMot.PlayFrameString("S2,1000,0,1:30,2:30,3:30,4:0,5:0,6:-30,7:-80,8:-80")
        m_CMot.PlayFrameString("S2,1000,0,1:0,2:0,3:40,4:0,5:0,6:-40,7:-80,8:-80")
        m_CMot.PlayFrameString("S2,1000,0,1:-20,2:-20,3:50,4:0,5:0,6:-50,7:-80,8:-80")

def gang():
    while(True):
        m_CMot.PlayFrameString("S2,1000,0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0")

init()
m_CMot.Wait(1000)
updawnshaking()
init()

#m_CMot.Wait(3000)
# 위치를 0으로 변경
# m_CMot.PlayFrameString("S2,1000,0,2:0,1:0,3:30")
#m_CMot.Wait(3000)
# 1, 2번 다이나믹셀을 둘다 90도 위치로 변경
#m_CMot.PlayFrameString("S2,1000,0,1:90,2:90,3:90")

# 위치를 0으로 변경
#m_CMot.PlayFrameString("S2,1000,0,2:0,1:-30,3:30")

# PC의 Comport를 체크한다.
#strPorts = Ojw.CSerial.GetPortNames()
#for strPort in strPorts:
#print(strPort)

anPorts = Ojw.CSerial.GetPorts()
for nPort in anPorts:
    print(nPort)

#m_CMot.SetTorq(False)
# 통신을 닫는다.
m_CMot.Close()

#you need a OpenJigware dll
