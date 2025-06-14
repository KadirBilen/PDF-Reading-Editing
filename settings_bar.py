from tkinter import Frame, Button, Entry, StringVar, OptionMenu
from tkinter.ttk import Style

def create_settings_bar(root, content_font_actual, adjust_font):
    # Ayarlar çubuğu
    settings_bar = Frame(root, bg="#f0f0f0", height=60, bd=2, relief="flat")
    settings_bar.pack(fill="x")

    # Buton stili
    style = Style()
    style.configure(
        "TButton",
        padding=6,
        relief="flat",
        background="#ffffff",
        font=("Helvetica", 10),
    )
    style.map(
        "TButton",
        background=[("active", "#e0e0e0")],
        relief=[("pressed", "sunken"), ("!pressed", "flat")],
    )

    # Yazı boyutu ayarı
    font_size_var = StringVar()
    font_size_var.set(str(content_font_actual.cget("size")))

    def on_size_change(*args):
        adjust_font("size", font_size_var.get())

    font_size_var.trace("w", on_size_change)

    # Büyüt butonu
    Button(
        settings_bar,
        text="➕",
        command=lambda: adjust_font("size", content_font_actual.cget("size") + 2),
        bg="#ffffff",
        relief="flat",
        font=("Helvetica", 11),
    ).pack(side="left", padx=5)

    # Küçült butonu
    Button(
        settings_bar,
        text="➖",
        command=lambda: adjust_font("size", content_font_actual.cget("size") - 2),
        bg="#ffffff",
        relief="flat",
        font=("Helvetica", 11),
    ).pack(side="left", padx=5)

    # Yazı tipi
    Entry(
        settings_bar,
        textvariable=font_size_var,
        width=5,
        font=("Helvetica", 12),
        justify="center",
        relief="groove",
    ).pack(side="left", padx=10)

    font_family_var = StringVar()
    font_family_var.set(content_font_actual.cget("family"))
    font_options = ["Helvetica", "Times", "Courier", "Arial"]

    OptionMenu(
        settings_bar,
        font_family_var,
        *font_options,
        command=lambda value: adjust_font("font_family", value),
    ).pack(side="left", padx=10)

    # Kalınlık ayarı
    Button(
        settings_bar,
        text="B",
        command=lambda: adjust_font("bold"),
        font=("Helvetica", 11),
        bg="#ffffff",
        relief="flat",
    ).pack(side="left", padx=10)

    return settings_bar
