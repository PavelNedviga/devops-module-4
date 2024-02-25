import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk
import requests
from io import BytesIO

class CatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cat Image Viewer")
        self.geometry("600x400")

        self.cat_image_label = Label(self)
        self.cat_image_label.pack(pady=20)

        self.get_cat_button = Button(self, text="Get Cat Image", command=self.get_cat_image)
        self.get_cat_button.pack(pady=10)

        self.save_cat_button = Button(self, text="Save Cat Image", command=self.save_cat_image)
        self.save_cat_button.pack(pady=10)

        self.current_cat_url = ""

    def get_cat_image(self):
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        if response.ok:
            data = response.json()
            cat_url = data[0]['url']
            self.current_cat_url = "L6_task/" + cat_url.split('/')[-1]  # Extract filename for saving
            image_response = requests.get(cat_url)
            if image_response.ok:
                image_data = Image.open(BytesIO(image_response.content))
                image_data = image_data.resize((400, 300), Image.BICUBIC)
                self.cat_photo = ImageTk.PhotoImage(image_data)
                self.cat_image_label.config(image=self.cat_photo)

    def save_cat_image(self):
        if self.current_cat_url:
            response = requests.get(f"https://api.thecatapi.com/v1/images/search?filename={self.current_cat_url}")
            if response.ok:
                with open(self.current_cat_url, 'wb') as f:
                    f.write(response.content)
                print(f"Image saved as {self.current_cat_url}")

if __name__ == '__main__':
    app = CatApp()
    app.mainloop()
