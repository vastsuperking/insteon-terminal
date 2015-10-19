#-------------------------------------------------------------------------------
#
# Insteon switch 2477S
#
import iofun
import message

from querier import Querier
from querier import MsgHandler
from switch import Switch
from linkdb import *

from us.pfrommer.insteon.cmd.msg import Msg
from us.pfrommer.insteon.cmd.msg import MsgListener
from us.pfrommer.insteon.cmd.msg import InsteonAddress

def out(msg = ""):
	iofun.out(msg)

class DefaultMsgHandler(MsgHandler):
	label = None
	def __init__(self, l):
		self.label = l
	def processMsg(self, msg):
		out(self.label + " got msg: " + msg.toString())
		return 1

class Switch2477S(Switch):
	"""==============  Insteon SwitchLinc 2477S ==============="""
	def __init__(self, name, addr):
		Switch.__init__(self, name, addr)

	def readOpFlags(self):
		"""readOpFlags()
		read operational flags"""
		self.querier.setMsgHandler(DefaultMsgHandler("read op flags"))
		self.querier.querysd(0x1f, 0x00);
