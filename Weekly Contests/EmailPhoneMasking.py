import sys
# taking input from the console
#lines = sys.stdin.readlines()

#function to mask the phone number
def maskPhone(phone) :
    if not phone :
        return

    # the output result i.e the masked string
    outRes = ""
    appendDash = False
    hashNum = "0123456789"
    hashDash = "()- "
    #add the first 2 characters to the outRes for P:
    outRes = phone[0:2]
    for i in range(2,len(phone)-4) :
        if phone[i] == "+" :
            outRes += "+"
            appendDash = False
        elif (phone[i] in hashDash) and (appendDash) :
            outRes += "-"
            appendDash = False
        elif phone[i] in hashNum :
            outRes += "*"
            appendDash = True

    #appending the last 4 characters
    outRes += phone[len(phone)-4:]
    print(outRes)

def maskEmail(email):
    if not email :
        return
    # the output result i.e the masked string
    outRes = ""

