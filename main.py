from tkinter import Tk, Canvas, Frame, Scrollbar, Text, font
from menu_bar import create_menu_bar
from settings_bar import create_settings_bar
from pdf_handler import open_pdf, show_pdf

def adjust_font(option, value=None):
    global text_area
    if option == "size":
        try:
            size = int(value) if value else content_font_actual.cget("size") + 2
            content_font_actual.configure(size=max(8, size))
            font_size_var.set(str(content_font_actual.cget("size")))
            text_area.configure(font=content_font_actual)
        except ValueError:
            pass
    elif option == "bold":
        weight = "bold" if content_font_actual.cget("weight") == "normal" else "normal"
        content_font_actual.configure(weight=weight)
        text_area.configure(font=content_font_actual)
    elif option == "font_family":
        content_font_actual.configure(family=value)
        text_area.configure(font=content_font_actual)


def new_document():
    global text_area
    canvas.delete("all")
    shadow_offset = 10
    canvas.create_rectangle(248 + shadow_offset, 10 + shadow_offset, 843 + shadow_offset, 852 + shadow_offset, fill="black", outline="")
    text_area = Text(canvas, width=70, height=40, wrap="word", font=content_font_actual, bg="white")
    canvas.create_window(248, 10, anchor="nw", window=text_area, width=595, height=842)

# Main Tkinter setup
root = Tk()
root.title("PDF Okuyucu")
root.state("zoomed")
root.configure(bg="white")

global content_font_actual
content_font_actual = font.Font(family="Helvetica", size=14, weight="normal")

settings_bar = create_settings_bar(root, content_font_actual, adjust_font)

frame = Frame(root, bg="white")
frame.pack(fill="both", expand=True)
scroll = Scrollbar(frame, orient="vertical")
scroll.pack(side="right", fill="y")
canvas = Canvas(frame, yscrollcommand=scroll.set, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)
scroll.config(command=canvas.yview)

create_menu_bar(root, new_document, lambda: open_pdf(canvas, show_pdf))

new_document()
root.mainloop()