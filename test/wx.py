from wxauto import *

wx = WeChat()

wx.GetSessionList()
'''
wx.LoadMoreMessage()
msgs = wx.GetAllMessage
'''
msg = '[炸弹]'
who = '小小小厚桑'
wx.ChatWith(who)
for i in range(10):
    wx.SendMsg(msg)
    print(i)