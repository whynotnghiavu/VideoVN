import tkinter as tk


from view.UseCase import UseCase
from view.Button import Button
from view.ButtonClick import ButtonClick


def app():
    gui = tk.Tk()
    # Đặt vị trí ở bên phải màn hình
    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()
    # NOTE: Kích thước cửa sổ (400)
    x_pos = screen_width - 400
    y_pos = 0
    gui.geometry(f"{400}x{screen_height}+{x_pos}+{y_pos}")

    gui.configure(background="#282a36")

    # Tạo checkbox
    var_shutdown = tk.IntVar()
    checkbox = tk.Checkbutton(
        text="Tự động tắt máy",
        variable=var_shutdown,
        background="#abd200",
        foreground="#000000",
        # NOTE: Kích thước nút bấm (40)
        width=40,
    )
    checkbox.pack()

    # Thêm các nút chức năng
    for chuc_nang, theme in Button.button_themes.items():
        button = tk.Button(
            text=chuc_nang,
            background=theme[0],
            foreground=theme[1],
            # NOTE: Kích thước nút bấm (40)
            width=40,
            command=lambda i=chuc_nang: ButtonClick(i, var_shutdown)
        )
        button.pack()

    # Tự động hỏi thư mục
    gui.bind('<Return>', ButtonClick(UseCase.ChonThuMuc, var_shutdown))
    gui.mainloop()
