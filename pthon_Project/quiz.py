r=0
y= { 1:" 1.Mumbai"" 2.Channai"" 3.Kolkata"" 4.New Delhi", 2:"1. 1947 2.1936 3.1974 4.1911", 3:"1.programming language 2.language 3.Machime language", 4:"1.Variable 2.datatype 3. function 4.structure", 5:"Type of data 2.function"}
q={1:"1.What is  the  capital citu of India?", 2:"2.When did India get independent", 3:"3.What  is python?", 4:"4.What is bool?", 5:"5.What is the datatype?"}
ans={1:"New Delhi", 2:"1947", 3:"programming language", 4:"datatype", 5:"Type of data"}
for i in y:
    print(q[i])
    print(y[i])
    answer= ans[i]
    # print(answer)
    while True:
     value= input("Enter  the value in string (not in number)").strip()
     if not value:
       print("Your input value is not fill, Fill the answer")
       print("Your answer :",value)
     elif value!=answer:
       print("->You have  entered the wrong answer.Enter  the right answer")
       r=r-1
     else:
       print("->You have enter right answer!!!!!!!")
       r=r+1
       break
     
print("score: ", r)
