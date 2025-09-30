import pyttsx3

text = """
My name is Govind Singh Solanki, and I belong to Bhopal, Madhya Pradesh. Currently, I am pursuing my 
Master of Computer Applications (MCA) from Shri Vaishnav Institute of Management & Science, Indore, 
with a CGPA of 7.0. Prior to this, I completed my Bachelor of Computer Applications (BCA) from 
SIRT, Bhopal, securing a CGPA of 8.0. I did my schooling from St. Xavier’s School, Bhopal, 
which laid a strong foundation for my academic journey.
...
"""

engine = pyttsx3.init()
engine.save_to_file(text, "govind_singh_solanki_intro.mp3")
engine.runAndWait()
