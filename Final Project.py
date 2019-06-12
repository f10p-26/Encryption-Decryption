#!/usr/bin/env python
# coding: utf-8

# # Encrypted Email
# ## For this project I explored the process of encryption and decryption and sending emails using python. For this project I used the method of Caesar Cipher and shifted the character by number 11. 

# In[38]:


final = ""
option = input("\nEnter 1 to Encrypt or 2 to Decrypt:\n>>") #For Custom Encoding
if option == "1":
    msg = input("\nEnter the message to encrypt:\n>>") #encoding
    for i in range(0, len(msg)):
        final = final + chr(ord(msg[i]) - 11)
    print(final)
elif option == "2": #decoding
    msg = input("\nEnter the message to decrypt:\n>>")
    for i in range(0, len(msg)):
        final = final + chr(ord(msg[i]) + 11)    
    print(final)
else:
    print("Please use number 1 or 2 only")


# ### For the purpose of this course I made a mock email to use it to email individuals. For user friendly reason, I added the feature where it would ask the user to specify the email. 
# ### The email is: f343p12@gmail.com
# ### password: Cogs18isAwes0me

# In[ ]:


import smtplib #Sending the encoded message
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("f343p12@gmail.com", "Cogs18isAwes0me")
receiver = input("/nEnter receiver's email address:\n>>")
s.sendmail("f343p12@gmail.com", receiver, final)
s.quit

print("Email sent")


# ### For the receiver to decode the message, they have to use the following function. This is just for the receiver in order to decode the message

# In[39]:


message = input("\nEnter your Encrypted Message here: \n>>") # dedocding the message
msg = ' '

for ord_1 in message:
    ind = ord(ord_1) + 11
    ord_2 = chr(ind)
    msg = msg + ord_2


print(msg)


# ### While I explored the probability of reading emails using a code, I saw related projects online and they appeared to be sophisticated and beyond the scope of the lessons of this course. To compensate for the email aspect, I created a separate code where the receiver can decode the encoded message
