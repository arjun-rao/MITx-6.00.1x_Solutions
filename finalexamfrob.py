# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def display(start):
    cur = start
    print cur.myName()
    while(cur.getAfter()!= None):
        cur = cur.getAfter()
        print cur.myName(),
    
    

                
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if(atMe.myName() < newFrob.myName()):#newFrob comes after atme
        nxt = atMe.getAfter()
        if(nxt == None):# insert at last node
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            return;
        elif(nxt.myName() >= newFrob.myName()):#insert immediately after atME
            newFrob.setAfter(nxt)
            newFrob.setBefore(atMe)
            atMe.setAfter(newFrob)
            nxt.setBefore(newFrob)
            return;
        else:
            insert(atMe.getAfter(),newFrob)
            return;
    else: #newFrob comes before at me
        bfr= atMe.getBefore()
        if(bfr == None): #insert before first node
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            return;
        elif(bfr.myName() <= newFrob.myName()): #insert Immediatly before atMe
            newFrob.setAfter(atMe)
            newFrob.setBefore(bfr)
            atMe.setBefore(newFrob)
            bfr.setAfter(newFrob)
            return;
        else:
            insert(atMe.getBefore(),newFrob)
            return;
            
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if(start.getBefore() == None):
        return start
    return findFront(start.getBefore())            
        