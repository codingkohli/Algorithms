# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
# taking input from the console
lines = sys.stdin.readlines()

#function to mask the phone number
def maskPhone(phone) :
    if not phone :
        return
    #cleansing the string for '\n'
    phone = phone.rstrip()
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
    return outRes

def maskEmail(email):
    if not email :
        return
    #cleansing the string for '\n'
    email = email.rstrip()
    # the output result i.e the masked string
    outRes = ""
    #splitting the values into 2 parts and treating seperately
    val = email.split("@")
    # getting the first part of the email
    # add the first 2 characters to the outRes for P:
    outRes = email[0:2]
    #picking the first and last element of the email
    outRes += email[2]
    outRes += "*****"
    outRes += val[0][-1]
    outRes += "@"
    outRes += val[1]
    return outRes

# printing the lines to the STDOUT
printRes = []
for inp in lines :
    if inp[0] == "E" :
        printRes.append(maskEmail(inp))
    elif inp[0] == "P" :
        printRes.append(maskPhone(inp))

# printing the result
for res in printRes :
    print(res)