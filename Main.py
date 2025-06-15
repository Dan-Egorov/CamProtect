import cv2
import face_recognition
from tkinter import *
from tkinter import filedialog
import time
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak
file = []
text = ""

def click_button1():
    global file
    file = filedialog.askopenfilenames()
    print(file)
    return file


def click_button2():
    global text
    text = user_text.get("0.1", "end")
    print(text)
    return text


def click_button3():
    desk.destroy()


desk = Tk()
desk.geometry("400x400")
desk.title("MegaBull")

but = Button(text="Выбрать фото")
but.config(command=click_button1)
but.pack()

user_text = Text(width=30, height=8)
user_text.pack()

but2 = Button(text="Подтверждение текста")
but2.config(command=click_button2)
but2.pack()

but3 = Button(text="Начать программу!!!!")
but3.config(command=click_button3)
but3.pack()

desk.mainloop()

file = list(file)
know_img = []
known_face_encoding = []
for i in file:
    know_img.append(face_recognition.load_image_file(i))

for i in know_img:
    known_face_encoding.append(face_recognition.face_encodings(i)[0])
#print(known_face_encoding, know_img)
#image = face_recognition.load_image_file(file)

flag = True
video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()

    rgb_small_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    #print(face_locations)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
        #print(matches)
        face_distances = face_recognition.face_distance(known_face_encoding, face_encoding)
        #best_match_index = np.argmin(face_distances)
        if matches[0]:
            speak(text)
            #os.system("start C:\\Users\\User\\PycharmProjects\\pythonProject13\\Recording(4) (online-video-cutter.com).mp4")
    cv2.imshow("To end the program, press \"escape\"", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    time.sleep(0.6)
