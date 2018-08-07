import logging
import os
import sys
import threading
import time
import tkinter
from multiprocessing.pool import ThreadPool
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import ttk

from chardet.universaldetector import UniversalDetector

logging.basicConfig(filename='Log.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='[%d/%m/%Y %H:%M:%S] - ', filemode='a')

class Gui():
    def insert_text(self):
        global current_directory
        current_directory = fd.askdirectory()

    def exit_program(self):
        sys.exit()

    def open_instructions(self):
        os.startfile('ReadMe.txt')

    def get_about(self):
        messagebox.showinfo("About", "ReplaceFile © 2018. Author: VFeschenko@lotus.asb.by (Telegram: @windx13)")

    def press_start(self):
        self.task_thread = threading.Thread(target=self.start_thread)
        self.task_thread.start()

    def start_thread(self):
        self.is_started = True

        self.one_label = False
        self.two_label = False
        self.tree_label = False
        self.four_label = False

        if self.is_started is not True:
            return

        try:
            if current_directory == '':
                pass
        except NameError:
            messagebox.showerror("Ошибка!", "Укажите папку, в которой нужно производить поиск файлов!")
            logging.error("Укажите папку, в которой нужно производить поиск файлов!")
        else:
            self.one_label = True

        mask_text = self.text_mask.get("1.0", 'end-1c')
        mask_text = str(mask_text)

        u_mask_text = mask_text.upper()
        l_mask_text = mask_text.lower()

        if self.is_started is not True:
            return

        if mask_text == '':
            messagebox.showerror("Ошибка!", "Введите маску файла для поиска!")
            logging.error("Введите маску файла для поиска!")
        else:
            self.two_label = True

        if self.is_started is not True:
            return

        search_text = self.text_search.get("1.0", 'end-1c')
        search_text = str(search_text)
        if search_text == '':
            messagebox.showerror("Ошибка!", "Введите текст, который нужно искать в файлах!")
            logging.error("Введите текст, который нужно искать в файлах!")
        else:
            self.tree_label = True

        if self.is_started is not True:
            return

        replace_text = self.text_replace.get("1.0", 'end-1c')
        replace_text = str(replace_text)
        if replace_text == '':
            messagebox.showerror("Ошибка!", "Введите текст, на который производится замена в файлах!")
            logging.error("Введите текст, на который производится замена в файлах!")
        else:
            self.four_label = True

        if self.is_started is not True:
            return

        if self.one_label and self.two_label and self.tree_label and self.four_label:

            if self.is_started is not True:
                return

            self.start_stop_btn = ttk.Button(text='Стоп', command=self.press_stop)
            self.start_stop_btn.place(x=100, y=350, width=200, height=40)

            if self.is_started is not True:
                return

            self.text_p.insert(tkinter.END, '[Начинаем поиск указанных файлов в заданной папке..]\n')
            logging.info('[Начинаем поиск указанных файлов в заданной папке..]')
            self.text_p.yview(tkinter.END)
            tree = os.walk(current_directory)
            self.path_f = []
            for d, dirs, files in tree:
                if self.is_started is not True:
                    return
                for f in files:
                    path = os.path.join(d, f)
                    self.path_f.append(path)

            if self.is_started is not True:
                return

            for n, i in enumerate(self.path_f):
                if self.is_started is not True:
                    return
                item = str(i).replace('\\', r'/')
                item = item.replace(r'/', '\\')
                self.path_f[n] = item

            self.text_p.insert(tkinter.END, '[Начинаем замену..]\n')
            logging.info('[Начинаем замену..]')
            self.text_p.yview(tkinter.END)

            self.pb['maximum'] = len(self.path_f)

            for i in self.path_f:
                if self.is_started is not True:
                    return
                if mask_text in i:
                    if self.is_started is not True:
                        return
                    # Определяем кодировку
                    detector = UniversalDetector()
                    with open(i, 'rb') as fh:
                        for line in fh:
                            detector.feed(line)
                            if detector.done:
                                break
                        detector.close()

                    with open(i, 'r', encoding=detector.result.get('encoding')) as file_in:
                        self.text = file_in.read()
                    self.text = self.text.replace(search_text, replace_text)
                    with open(i, 'w', encoding=detector.result.get('encoding')) as file_out:
                        file_out.write(self.text)
                    self.text_p.insert(tkinter.END, '[Файл %s обработан успешно!]\n' % i)
                    logging.info('[Файл %s обработан успешно!]' % i)
                    self.text_p.yview(tkinter.END)
                    if self.is_started is not True:
                        return
                elif u_mask_text in i:
                    if self.is_started is not True:
                        return
                    # Определяем кодировку
                    detector = UniversalDetector()
                    with open(i, 'rb') as fh:
                        for line in fh:
                            detector.feed(line)
                            if detector.done:
                                break
                        detector.close()

                    with open(i, 'r', encoding=detector.result.get('encoding')) as file_in:
                        self.text = file_in.read()
                    self.text = self.text.replace(search_text, replace_text)
                    with open(i, 'w', encoding=detector.result.get('encoding')) as file_out:
                        file_out.write(self.text)
                    self.text_p.insert(tkinter.END, '[Файл %s обработан успешно!]\n' % i)
                    logging.info('[Файл %s обработан успешно!]' % i)
                    self.text_p.yview(tkinter.END)
                    if self.is_started is not True:
                        return
                elif l_mask_text in i:
                    if self.is_started is not True:
                        return
                    # Определяем кодировку
                    detector = UniversalDetector()
                    with open(i, 'rb') as fh:
                        for line in fh:
                            detector.feed(line)
                            if detector.done:
                                break
                        detector.close()

                    with open(i, 'r', encoding=detector.result.get('encoding')) as file_in:
                        self.text = file_in.read()
                    self.text = self.text.replace(search_text, replace_text)
                    with open(i, 'w', encoding=detector.result.get('encoding')) as file_out:
                        file_out.write(self.text)
                    self.text_p.insert(tkinter.END, '[Файл %s обработан успешно!]\n' % i)
                    logging.info('[Файл %s обработан успешно!]' % i)
                    self.text_p.yview(tkinter.END)
                    if self.is_started is not True:
                        return
                self.pb.step(1)

        self.text_p.insert(tkinter.END, '\n[Завершено]\n')
        logging.info('[Завершено]')
        logging.info('-----------')
        self.text_p.yview(tkinter.END)
        self.start_stop_btn = ttk.Button(text='Старт', command=self.press_start)
        self.start_stop_btn.place(x=100, y=350, width=200, height=40)

    def press_stop(self):
        self.is_started = False
        self.stop_thread_init = threading.Thread(target=self.stop_thread)
        self.stop_thread_init.start()

    def stop_thread(self):
        time.sleep(1)
        self.pb.stop()
        self.text_p.insert(tkinter.END, '\n[Остановлено]\n')
        logging.info('[Остановлено]')
        logging.info('-------------')
        self.text_p.yview(tkinter.END)
        self.start_stop_btn = ttk.Button(text='Старт', command=self.press_start)
        self.start_stop_btn.place(x=100, y=350, width=200, height=40)

    def init(self):
        self.is_started = False
        self.pool = ThreadPool(8)
        self.root = tkinter.Tk()
        self.w = self.root.winfo_screenwidth()  # Ширина
        self.h = self.root.winfo_screenheight()  # Высота
        self.w = self.w // 2  # Середина экрана
        self.h = self.h // 2
        self.w = self.w - 200
        self.h = self.h - 200
        self.root.geometry("400x450+{}+{}".format(self.w, self.h))
        self.root.resizable(False, False)
        self.root.title('ReplaceFile')
        self.root.iconbitmap('icon.ico')

        self.mainmenu = tkinter.Menu(self.root)
        self.root.config(menu=self.mainmenu)

        self.filemenu = tkinter.Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Выход", command=self.exit_program)

        self.helpmenu = tkinter.Menu(self.mainmenu, tearoff=0)
        self.helpmenu.add_command(label="Инструкция", command=self.open_instructions)
        self.helpmenu.add_command(label="О программе", command=self.get_about)

        self.mainmenu.add_cascade(label="Файл", menu=self.filemenu)
        self.mainmenu.add_cascade(label="О программе", menu=self.helpmenu)

        self.text_p = tkinter.Text(self.root, autoseparators=True, wrap=tkinter.WORD, font='Courier 8')
        self.text_p.place(x=5, y=190, width=390, height=150)

        ttk.Style().configure("TButton", padding=6, relief="flat",
                              background="#ccc")

        self.btn1 = ttk.Button(text='Каталог с файлами', command=self.insert_text)
        self.btn1.place(x=100, y=5, width=200, height=40)

        self.start_stop_btn = ttk.Button(text='Старт', command=self.press_start)
        self.start_stop_btn.place(x=100, y=350, width=200, height=40)

        self.pb = ttk.Progressbar(self.root, orient="horizontal")
        self.pb.place(x=5, y=400, width=390, height=25)

        self.label_mask = ttk.Label(self.root, text='Маска')
        self.label_mask.place(x=330, y=60, width=200, height=35)
        self.text_mask = tkinter.Text(self.root)
        self.text_mask.place(x=5, y=60, width=320, height=35)

        self.label_search = ttk.Label(self.root, text='Искать')
        self.label_search.place(x=330, y=100, width=200, height=35)
        self.text_search = tkinter.Text(self.root)
        self.text_search.place(x=5, y=100, width=320, height=35)

        self.label_replace = ttk.Label(self.root, text='Заменить')
        self.label_replace.place(x=330, y=140, width=200, height=35)
        self.text_replace = tkinter.Text(self.root)
        self.text_replace.place(x=5, y=140, width=320, height=35)

        self.root.mainloop()

try:
    gui = Gui()
    gui.init()
except Exception as e:
    logging.error(e)
    sys.exit()
