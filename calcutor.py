firstnumber = int(input ("Enter the first number:"))                  
secondnumber = int(input ("Enter the second number:"))
process = input("""Enter the transaction
("addition: +, subtraction: -, multiplication: x, division: /")
""")
if process == ("+"):
    print (firstnumber+secondnumber)

elif process == ("-"):
    print (firstnumber-secondnumber)

elif process == ("x"):
     print (firstnumber*secondnumber)

elif process == ("/"):
    print (firstnumber/secondnumber)
