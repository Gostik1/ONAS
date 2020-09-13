#!/usr/bin/env python
# coding: utf-8

# In[1]:


message = "Hello Python world!"
print(message)


# In[2]:


message = "Hello Python world!"
print(message)
message = "Python is my favorite language!"
print(message)


# In[3]:


message = "Здравствуйте преподователь!"
print(message)


# In[6]:


my_string = "This is a double-quoted string."
my_string = 'This is a single-quoted string.'
print(my_string)


# In[7]:


quote = "Linus Torvalds once said, 'Any program is only as good as it is useful.'"
print(quote)


# In[8]:


first_name = 'Alexsandr'
print(first_name)
print(first_name.title())


# In[9]:


first_name = 'Alex'
print(first_name)
print(first_name.title())
print(first_name.upper())
first_name = 'Alex'
print(first_name.lower())


# In[10]:


first_name = 'Alexsandr'
last_name = 'Poplavskiy'
full_name = first_name + ' ' + last_name

print(full_name.title())


# In[11]:


first_name = 'Alexsandr'
last_name = 'Poplavskiy'
full_name = first_name + ' ' + last_name
message = full_name.title() + ' ' + "Студенты группы Кн 3.1.03"
print(message)


# In[24]:


print("Alexsandr")
print("\nAlexsandr!")
print("Alexs\nandr!")
print("\n\nAlexsandr")


# In[13]:


name = ' Alex '
print(name.lstrip())
print(name.rstrip())
print(name.strip())


# In[14]:


quote = "Жизнь — это чудесное приключение, достойное того, чтобы ради удач терпеть и неудачи."   
print(quote)


# In[15]:


first ="Steve" 
last ="Jobs"
message ="Стив Джобс мой кумир" + ' ' +"Подари мне айфон"
print(message)


# In[19]:


print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2)


# In[20]:


standard_order = 2+3*4
print(standard_order)
my_order = (2+3)*4
print(my_order)


# In[21]:


print(0.1+0.1)


# In[22]:


# This line is a comment.
print("This line is not a comment, it is code.")


# In[29]:


def thank_you(name):
# This function prints a two-line personalized thank you message.
    print("\nYou are doing good work, %s!" % name)
    print("Thank you very much for your efforts on this project.")
thank_you('Adriana')
thank_you('Billy')
thank_you('Caroline')


# In[35]:


def get_number_word(number):
# Takes in a numerical value, and returns
# the word corresponding to that number.
    if number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
# ...
# Let's try out our function.
for current_number in range(0,4):
    number_word = get_number_word(current_number)
    print(current_number, number_word)


# In[36]:


students = ['bernice', 'aaron', 'cody']
for student in students:
    print("Hello, " + student.title() + "!")


# In[38]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dog = dogs[0]
print(dog.title())


# In[39]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dog = dogs[-1]
print(dog.title())


# In[40]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
for dog in dogs:
    print(dog)


# In[41]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
print("Results for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index)
    print("Place: " + place + " Dog: " + dog.title())


# In[ ]:




