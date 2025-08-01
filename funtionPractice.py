def check_for_word():
    word="learning"

    with open ("practice.txt", "r") as f:
        data=f.read()

   

        if(data.find(word)!=-1):
         print("found")
        else:
         print("not found")



check_for_word()



def check_for_line_word():
   word="learning"
   data=True
   line_no=1
   with open("practice.txt","r") as f:
      while data:
         data=f.readline()
         if(word in data):
            print(line_no)
            return 
         line_no +=1
      return -1    
   
print(check_for_line_word())



with open("number.txt","r")as f:
   data=f.read()
   print(data)
   num=""
   for i in range(len(data)):
      if(data[i]==","):
         print(int(num))
         num=""
      else:
         num +=data[i]   

