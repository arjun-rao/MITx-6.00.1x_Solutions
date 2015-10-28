### PROBLEM 5 ####

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self,name)
        validStatus = ["citizen","legal_resident","illegal_resident"]
        if(status in validStatus):
            self.status = status
        else:
            raise ValueError
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status












#### PROBLEM 4 ######
#def getSublists(L,n):
#     """
#      Returns a list of all possible sublists of L of length nm without skipping elements in L
#     """
#     assert(len(L) != 0), "List is empty"
#     assert(0<n<=len(L)), "n is not between 0 and Len(L))"
#     result = []
#     i = 0
#     j = n
#     while(j<=len(L)):
#        result.append(L[i:j])
#        j+=1
#        i+=1
#     return result
#     
#def longestRun(L):
#    """ 
#    Returns length of longest running monotonically increasing numbers occuring in L
#    """
#    def isSorted(L1):
#        for e in range(len(L1)-1):
#            if(L1[e]>L1[e+1]):
#                return False
#        return True
#        
#    Llength = len(L)
#    i = Llength
#    maxlength = 1
#    while(i>1):
#        sublists = getSublists(L,i)
#        for sublist in sublists:
#            if(isSorted(sublist) and maxlength<len(sublist)):
#                maxlength = len(sublist)
#        i-=1
#    return maxlength
#         
#         
#print 'answer:', longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])
