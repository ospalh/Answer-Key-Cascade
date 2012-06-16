﻿"""
Name: Answer Key Cascade
Filename: Answer_Key_Cascade.py
Version: 0.2
Author: Kenishi
Desc:	By defualt Anki 2 now reduces the button count depending on card age.
		Cards can now have anywhere from 2 to 4 buttons max depending on age.
		Answering a card with 2 buttons requires you to press 1 or 2 if you are using hotkeys.
		This can interfere with review speed if you don't realize its 2 buttons and answer 3/4.
		This addon makes it so answering with a higher ease than possible will answer with the actual highest.
		
		*Example* 3 Button card: You press "4", the addon answers with "3".
		
		Support at http://forum.koohii.com/viewtopic.php?pid=178705#p178705
"""


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from aqt import mw

### Key Dictionary for new answer ###
KEYS = {2:(Qt.Key_2,u'2'),
		3:(Qt.Key_3,u'3')}

def KeyRemap_keyPressEvent(evt):
	if mw.reviewer.state == "answer": # Check if we're in answer
		cnt = mw.col.sched.answerButtons(mw.reviewer.card) # Get button count
		if evt.text() > str(cnt): # Was our answer larger than the max button count?
			key, text = KEYS.get(cnt,(evt.key(),evt.text()))
			evt = QKeyEvent(QEvent.KeyRelease, key, evt.modifiers(), text, evt.isAutoRepeat(), evt.count()) # Modify answer to reflect that we wanted the max answer
	return oldPressevent(evt)	

### Wrap old keyPressEvent with our new one
oldPressevent = mw.keyPressEvent
mw.keyPressEvent = KeyRemap_keyPressEvent