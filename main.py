from tkinter import *
from PIL import ImageTk, Image
import requests


def number(age_box, gender_box, a):
    koniec = Toplevel()
    koniec.minsize(width=800, height=800)
    koniec.title("Image")

    canvas = Canvas(koniec, width=600, height=800)

    b = int(age_box)
    c = gender_box

    gender = ["Male", "Female"]
    age_cat = {
        'teen': list(range(0, 19)),
        'young': list(range(18, 41)),
        'mature': list(range(40, 99))
    }

    print('Age:', b)
    print('Gender:', c)
    print('Temperature:', a)
    info = f'Age: {b}, Gender: {c}, Temperature: {a}'
    info = Label(koniec, text=info, font=('Arial', 15))
    info.pack()

    if c == gender[1]:
        if b in age_cat['teen']:
            if a >= 30:
                label = Label(koniec, text="You are a young Girl. You can wear Tank Top",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                img = ImageTk.PhotoImage(Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\F_0 to 18_Sunny.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)

            elif 24 <= a <= 29:
                label = Label(koniec, text="You are a young Girl. You can wear T Shirt",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                label.pack()
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\F_0 to 18_Cloudy.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            else:
                img = ImageTk.PhotoImage(Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\F_0 to 18_Raining.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)

        elif 18 <= b <= 40:
            if a >= 30:
                label = Label(koniec, text="You are a young Women. You can wear Tank Top",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\F_18 to 40_Sunny.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            elif 24 <= a <= 29:
                label = Label(koniec, text="You are a young Women. You can wear T Shirt",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                label.pack()
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\F_18 to 40_Cloudy.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            else:
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\F_18 to 40_Raining.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)

        elif b > 40:
            if a >= 30:
                label = Label(koniec, text="You are a Mature Women. You can wear Tank Top",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\F_40 above_Sunny.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            elif 24 <= a <= 29:
                label = Label(koniec, text="You are a Mature Women. You can wear T Shirt",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                label.pack()
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\F_40 above_Cloudy.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            else:
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\F_40 above_Raining.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)

    elif c == "Male":
        if 0 <= b <= 18:
            if a >= 30:
                label = Label(koniec, text="You are a young Boy. You can wear Tank Top",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                img = ImageTk.PhotoImage(Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\M_0 to 18_Sunny.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)

            elif 24 <= a <= 29:
                label = Label(koniec, text="You are a young Boy. You can wear T Shirt",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                label.pack()
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\M_0 to 18_Cloudy.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            else:
                img = ImageTk.PhotoImage(Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\M_0 to 18_Raining.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)

        elif 18 <= b <= 40:
            if a >= 30:
                label = Label(koniec, text="You are a young Man. You can wear Tank Top",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\M_18 to 40_Sunny.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            elif 24 <= a <= 29:
                label = Label(koniec, text="You are a young Men. You can wear T Shirt",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                label.pack()
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\M_18 to 40_Cloudy.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            else:
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\M_18 to 40_Raining.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)

        elif b > 40:
            if a >= 30:
                label = Label(koniec, text="You are a Mature Men. You can wear Tank Top",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\M_40 and above_Sunny.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            elif 24 <= a <= 29:
                label = Label(koniec, text="You are a Mature Men. You can wear T Shirt",
                              font=('Arial', 22),
                              width=80,
                              height=3,
                              foreground="white",
                              background="black")
                label.pack()
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\M_40 and above_Cloudy.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)
            else:
                img = ImageTk.PhotoImage(
                    Image.open(r'C:\Users\HOVT\PycharmProjects\ImageAPI\files\M_40 and above_Raining.jpg'))
                canvas.create_image(0, 0, anchor=NW, image=img)

    canvas.pack()
    canvas.mainloop()


if __name__ == '__main__':
    window = Tk()
    window.title("Welcome")
    window.geometry("500x500")

    heading = Label(text="""Welcome to Pixel Empire, 
    we will suggest what kind of clothes you can wear 
    based on the current temperature in Singapore""",
                    width=80,
                    height=3,
                    foreground="white",
                    background="black")
    heading.pack()

    intro = Label(window, text="Please enter your name")
    entry = Entry(window)  # this entry is the text box where we enter our name
    intro.pack(pady=7)
    entry.pack(pady=7)

    age_label = Label(window, text="What is your age")
    age_label.pack(pady=7)

    age_box = Entry(window)
    age_box.pack(pady=7)

    gender_label = Label(window, text="What is your gender")
    gender_label.pack(pady=7)

    gender_box = Entry(window)
    gender_box.pack(pady=7)

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": "Singapore"}

    headers = {
        
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    dict = response.json()

    a = (dict['current']['temp_c'])

    print(f' Singapore current weather is {a} degree celcius')

    button = Button(window,
                    text='Click me',
                    width=15,
                    height=1,
                    command=lambda: number(str(age_box.get()), str(gender_box.get()), a)
                    )
    button.pack(pady=5)

    answer = Label(window, text='')
    answer.pack(pady=20)

    window.mainloop()
