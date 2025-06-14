import fitz
from PIL import Image, ImageTk

def open_pdf(canvas, show_pdf):
    from tkinter import filedialog
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return

    pdf_document = fitz.open(file_path)
    page = pdf_document[0]
    pix = page.get_pixmap()
    pix.save("temp_page.png")
    show_pdf(canvas, "temp_page.png")
    pdf_document.close()

def show_pdf(canvas, image_path):
    image = Image.open(image_path)
    img = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=img)
    canvas.image = img