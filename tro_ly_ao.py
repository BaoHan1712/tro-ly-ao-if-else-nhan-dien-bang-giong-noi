import speech_recognition as sr
from datetime import datetime,date
import pyttsx3
import wikipedia

now = datetime.now()


# Chuyển đổi thành giong nói tiếng việt
robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty("voices")
robot_mouth.setProperty("voice", voices[1].id)
# nghe ne
robot_ear = sr.Recognizer()
while True:
    with sr.Microphone() as mic:
        print("Robot: Tôi đang nghe nè")
        audio = robot_ear.record(mic,duration= 5)
    print("......") 

    try:
        you = robot_ear.recognize_google(audio,language = "vi")
    except:
        you = ""
    print("you:" + you)

    if you == "":
        robot_brain ="Tôi chưa nghe bạn nói gì, bạn nói đi"
    elif "Hôm nay" in you:
        robot_brain = now.strftime("Hôm nay là ngày %d %m %Y ")
    elif "giờ" in you:
        robot_brain = now.strftime("%H:%M:%S")   
    elif "chào" in you:
        robot_brain = "Xin chào bạn, tôi có thể giúp gì cho bạn"
    elif "thả thính thứ nhất" in you:
        robot_brain = "OK tôi sẽ làm 1 câu thả thính, Nếu em là bịch thuốc phiện thì anh sẽ là thằng nghiện đầu tiên. Nếu em là trại thương điên thì anh là thằng điên mãi mãi. "
    elif "thả thính thứ hai" in you:
        robot_brain = "OK tôi sẽ làm 1 câu ,  Nhân chi sơ tính bản thiện. Thích em đến nghiện thì phải làm sao? "
    elif "thả thính thứ ba" in you:
        robot_brain = "OK tôi sẽ làm 1 câu thả thính, Ai dám nói nơi hạnh phúc nhất là thiên đường. Người đó chắc hẳn không biết đến khoảnh khắc mỗi khi em cười rồi! "
    elif "thả thính" in you:
        robot_brain = "OK tôi sẽ làm 1 câu thả thính, em ăn cơm chưa "
    elif "tên" in you:
        robot_brain = "Tôi là trợ lý ảo được tạo ra bởi 1 người tên là Hàn Quốc Bảo với mục đích là phục vụ và trả lời các câu hỏi mà bạn đưa ra "
    elif "Tên" in you:
        robot_brain = "Tôi là trợ lý ảo được tạo ra bởi 1 người tên là Hàn Quốc Bảo với mục đích là phục vụ và trả lời các câu hỏi mà bạn đưa ra"
        robot_mouth.say(robot_brain)
    elif "tạm biệt" in you:
        robot_brain = "tạm biệt bạn, chúc bạn một ngày tốt lành"
        print("Robot:" + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "Tạm biệt" in you:
        robot_brain = "tạm biệt bạn, chúc bạn một ngày tốt lành"
        print("Robot:" + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif you:
        wikipedia.set_lang("vi")
        robot_brain= wikipedia.summary(you,sentences = 1)
        
    else :
        robot_brain = "Tôi không biết"
        print(robot_brain)
    

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    
    


    

# engine.say("xin chào bạn, tôi là trợ lý ảo")

# engine.runAndWait()