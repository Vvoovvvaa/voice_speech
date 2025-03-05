import speech_recognition as sr
import os
import webbrowser

mic = sr.Microphone(device_index=2)
r = sr.Recognizer()
# list_mic = sr.Microphone.list_microphone_names()
# for i, mic_name in enumerate(list_mic):
#     print(f"Index {i}: {mic_name}")

def open_chrome():
    webbrowser.open("https://www.google.com")
    print("Ok")


def open_youtube():
    webbrowser.open("https://www.youtube.ru")
    print("OK")


def open_instagram():
    webbrowser.open("https://www.instagram.com")
    print("ok")


def open_files():
    os.system("explorer C://")
    print("OK")


def open_dow():
    path = os.path.expandvars(r"%USERPROFILE%\Downloads")
    os.system(f"explorer {path}")
    print("OK")


def create_file(file_name):
    folder = os.path.expandvars(r"%USERPROFILE%\Downloads")  
    filepath = os.path.join(folder, file_name)

    with open(filepath, "w") as file:
        file.write("")

    print(f"File {file_name} created in {folder}")


def open_file(file_name, folder):
    folder = os.path.expandvars(r"%USERPROFILE%\Downloads")  
    filepath = os.path.join(folder, file_name)

    if os.path.exists(filepath):
        os.startfile(filepath)
        print(f"Opening: {file_name}")
    else:
        print(f"File {file_name} not found in {folder}")


def delete_file(file_name, folder):
    filepath = os.path.join(folder, file_name)
    if not os.path.exists(filepath):
        print(f"File {file_name} not found")
        return
    os.remove(filepath)
    print(f"File {file_name} deleted")


def recognize_command():
    with mic as source:
        print("Say something...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Couldn't understand the speech.")
    except sr.RequestError as e:
        print(f"Speech recognition service error: {e}")
    return input("Enter comand: ").strip().lower()


def main():
    command = recognize_command()

    if "open chrome" in command :
        open_chrome()
    elif "open youtube" in command:
        open_youtube()                                                  
    elif "open instagram" in command:
        open_instagram()
    elif "open files" in command:
        open_files()
    elif "open download" in command:
        open_dow()
    elif "create file" in command:
        file_name = command.replace("create file ", "")
        create_file(file_name)
    elif "open file" in command:
        file_name = command.replace("open file ", "")
        open_file(file_name, os.path.expandvars(r"%USERPROFILE%\Downloads"))

    elif "delete file" in command:
        file_name = command.replace("delete file ", "")
        delete_file(file_name, os.path.expandvars(r"%USERPROFILE%\Downloads"))


if __name__ == "__main__":
    main()