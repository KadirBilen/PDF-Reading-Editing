from tkinter import Menu

def create_menu_bar(root, new_document, open_pdf):
    menu_bar = Menu(root)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Yeni Dosya", command=new_document)
    file_menu.add_command(label="Dosya Aç", command=open_pdf)
    file_menu.add_separator()
    file_menu.add_command(label="Çıkış", command=root.quit)
    menu_bar.add_cascade(label="Dosya", menu=file_menu)

    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Düzenleme Seçenekleri")
    menu_bar.add_cascade(label="Düzenle", menu=edit_menu)

    settings_menu = Menu(menu_bar, tearoff=0)
    settings_menu.add_command(label="Tercihler")
    menu_bar.add_cascade(label="Ayarlar", menu=settings_menu)

    root.config(menu=menu_bar)