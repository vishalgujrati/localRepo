amount = int(input("enter your amount: "))
#including gst
gst = (amount * 18)/100 + amount
cgst = (amount*9)/100  + amount
sgst = (amount*9)/100 + amount
#excluding gst
egst = gst - amount
ecgst =  cgst - amount
esgst = sgst - amount 

print("the total gst with amount",gst)
print("the total cgst with amount",cgst)
print("the total sgst with amount",sgst)
print("paid gst is",egst)
print("paid sgst is",ecgst)
print("paid cgst is",esgst)

input("Press Enter to exit...")