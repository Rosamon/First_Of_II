import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#keras? tenser////


from tkinter import *
import tkinter as tk
#import win32gui # на линуксе не знаю чем заменить, так что без понятия работает ли оно
from PIL import ImageGrab, Image
import numpy as np



'''def predict_digit(img):
    # Рабочая часть, возврат цифры
    # изменение рзмера изобржений на 28x28
    img = img.resize((28,28))
    # конвертируем rgb в grayscale
    img = img.convert('L')
    img = np.array(img)
    # изменение размерности для поддержки модели ввода и нормализации
    img = img.reshape(1,28,28,1)
    img = img/255.0
    # предстказание цифры
    #тута img -> куда-то v II
    # return x # где х - цифра'''
    
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.x = self.y = 0
        self.title(" ИИ ") # Заголовок
        # Создание элементов
        self.canvas = tk.Canvas(self, width=280, height=280, bg = "white", cursor="cross")
        self.label = tk.Label(self, width=10, text="...", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text = "Распознать", command = self.classify_handwriting) 
        self.button_clear = tk.Button(self, text = "Очистить", command = self.clear_all)
        
        # Сетка окна
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=0, column=1,pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)
        
        # нажатие на холст + движение, включает процедуру рисовки
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        
    def clear_all(self):
        '''Кнопка отчистить "холст" '''
        self.canvas.delete("all")
        
    def classify_handwriting(self):
        '''Кнопка запуска распознавания через скрина изображения -> в функцию 
        возврата значения через ИИ
        '''
        self.label.configure(text = "5") # запись в лэйбл
    # что дальше твориться я не знаб, но скорее всего оно должно скринить холст canvas
    ''' HWND = self.canvas.winfo_id() 
        rect = win32gui.GetWindowRect(HWND) # получаем координату холста
        im = ImageGrab.grab(rect)
        
        digit = predict_digit(im) # Вот эта функция возвращает число и далее выводим
        self.label.configure(text= str(digit)) 
    '''
        
    def draw_lines(self, event):
        '''Рисовка на холсте квадратиками '''
        self.x = event.x
        self.y = event.y
        r=8
        self.canvas.create_rectangle(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')
        # Ну или create_oval()


app = App()
mainloop()
