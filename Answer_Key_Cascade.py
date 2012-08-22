# -*- mode: python ; coding: utf-8 -*-
#
# © 2012 Roland Sieker (ospalh@gmail.com), 2012-04-13
#
# License: GNU AGPL, version 3 or later; http://www.gnu.org/copyleft/agpl.html


"""
Add-on for Anki 2 to always accept answer keys up to 4.
"""

from aqt.reviewer import Reviewer

def four_answer_card(self, ease):
    """
    Wrapper for the old Reviewer._answerCard

    Only call the old _answerCard function when we have an ease up to
    four. There are at most four buttons, but there may be fewer. When
    we have fewer than four and we try to answer with an non-existant
    ease, pretend we pressed the highest ease button.
    When the eease is > 4, we don't call the _answerCard. That is
    OK. The old behaviour was to do nothing inside that function in
    that case.
    """
    if (ease <= 4):
        old__answerCard(self,
                        min(ease, self.mw.col.sched.answerButtons(self.card)))


old__answerCard = Reviewer._answerCard
Reviewer._answerCard = four_answer_card
