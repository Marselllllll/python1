import tkinter as tk
kniga ={}
listfio = []
listnum =[]

def norm_number(number):
    number = number.replace(' ','').replace('-','')
    if number[:2] == '+7' and len(number) == 12:
        return number
    if number[0] == '8' and len(number) == 11:
        number = number.replace('8','+7',1)
        return number
    if number[0] == '9' and len(number) == 10:
        number = '+7' + number
        return number
    else:
        return 'Неправильно набран номер'

def norm_fio(fio):
    fio = fio.title()
    return fio+" "

def f_create():
    def f_create_number():
        fio = enteryfio.get()
        number = enterynum.get()
        corr_number = norm_number(number)
        corr_fio = norm_fio(fio)
        kniga[corr_fio] = corr_number
        c_window.destroy()
    c_window = tk.Tk()
    c_window.title("СОЗДАТЬ КОНТАКТ")
    c_window.resizable(
        width=False,
        height=False
    )
    c_window.geometry("350x170")
    lbl_bg1 = tk.Label(
        master=c_window,
        background="LightSalmon2"
    )
    lbl_bg1.place(
        height=170,
        width=350,
        x=0,
        y=0
    )
    frame_fio_c = tk.Frame(
        master=c_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )
    frame_number_c = tk.Frame(
        master=c_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )
    frame_fio_c1 = tk.Frame(
        master=c_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )
    frame_number_c1 = tk.Frame(
        master=c_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )
    frame_fio_c.place(
        height=45,
        width=70,
        x=25,
        y=25
    )
    frame_number_c.place(
        height=45,
        width=70,
        x=25,
        y=80
    )
    frame_fio_c1.place(
        height=45,
        width=225,
        x=105,
        y=25
    )
    frame_number_c1.place(
        height=45,
        width=225,
        x=105,
        y=80
    )
    lbl_fio_c = tk.Label(
        master=frame_fio_c,
        text="ФИО:",
        bg="coral3"
    )
    lbl_fio_c.pack(
        expand=True,
        fill=tk.BOTH
    )
    lbl_number_c = tk.Label(
        master=frame_number_c,
        text="Номер:",
        bg="coral3"
    )
    lbl_number_c.pack(
        expand=True,
        fill=tk.BOTH
    )
    enteryfio = tk.Entry(
        master=frame_fio_c1,
        bg="coral3"
    )
    enteryfio.pack(
    expand=True,
    fill=tk.BOTH
    )
    enterynum = tk.Entry(
        master=frame_number_c1,
        bg="coral3"
    )
    enterynum.pack(
    expand=True,
    fill=tk.BOTH
    )

    frame_save_c = tk.Frame(
        master=c_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )
    frame_save_c.place(
        height=30,
        width=80,
        x=245,
        y=130
    )
    btn_save_number = tk.Button(
        master=frame_save_c,
        text="Сохранить",
        bg="coral1",
        command=f_create_number
    )
    btn_save_number.pack(
        expand=True,
        fill=tk.BOTH
    )

def f_search():
    def f_btn_search():
        s_name1 = enteryfio_s.get()
        s_name = norm_fio(s_name1)
        textnum1 = kniga.get(s_name)

        if textnum1!= None:

            def f_renew_number1():
                del kniga[s_name]
                a = f_create()



            war_window1 = tk.Tk()
            war_window1.title("КОНТАКТ")
            war_window1.resizable(
                width=False,
                height=False
            )
            war_window1.geometry("350x170")
            lbl_bg5 = tk.Label(
                master=war_window1,
                background="LightSalmon2"
            )
            lbl_bg5.place(
                height=170,
                width=350,
                x=0,
                y=0
            )
            frame_fio_war1 = tk.Frame(
                master=war_window1,
                relief=tk.GROOVE,
                bg="coral3",
                borderwidth=5
            )
            frame_number_war1 = tk.Frame(
                master=war_window1,
                relief=tk.GROOVE,
                bg="coral3",
                borderwidth=5
            )
            frame_fio_war11 = tk.Frame(
                master=war_window1,
                relief=tk.GROOVE,
                bg="coral3",
                borderwidth=5
            )
            frame_number_war11 = tk.Frame(
                master=war_window1,
                relief=tk.GROOVE,
                bg="coral3",
                borderwidth=5
            )
            frame_fio_war1.place(
                height=45,
                width=70,
                x=25,
                y=25
            )
            frame_number_war1.place(
                height=45,
                width=70,
                x=25,
                y=80
            )
            frame_fio_war11.place(
                height=45,
                width=225,
                x=105,
                y=25
            )
            frame_number_war11.place(
                height=45,
                width=225,
                x=105,
                y=80
            )
            lbl_fio_war1 = tk.Label(
                master=frame_fio_war1,
                text="ФИО:",
                bg="coral3"
            )
            lbl_fio_war1.pack(
                expand=True,
                fill=tk.BOTH
            )
            lbl_number_war1 = tk.Label(
                master=frame_number_war1,
                text="Номер:",
                bg="coral3"
            )
            lbl_number_war1.pack(
                expand=True,
                fill=tk.BOTH
            )
            labelfio1 = tk.Label(
                master=frame_fio_war11,
                bg="coral3",
                text=s_name
            )
            labelfio1.pack(
                expand=True,
                fill=tk.BOTH
            )
            labelnum1 = tk.Label(
                master=frame_number_war11,
                bg="coral3",
                text=textnum1
            )
            labelnum1.pack(
                expand=True,
                fill=tk.BOTH
            )

            frame_save_war1 = tk.Frame(
                master=war_window1,
                relief=tk.GROOVE,
                bg="coral3",
                borderwidth=5
            )
            frame_save_war1.place(
                height=30,
                width=80,
                x=245,
                y=130
            )
            btn_save_number1 = tk.Button(
                master=frame_save_war1,
                text="Изменить",
                bg="coral1",
                command=f_renew_number1
            )
            btn_save_number1.pack(
                expand=True,
                fill=tk.BOTH
            )

    s_window = tk.Tk()
    s_window.title("ПОИСК")
    s_window.resizable(
        width=False,
        height=False
    )
    s_window.geometry("350x170")
    lbl_bg4 = tk.Label(
        master=s_window,
        background="LightSalmon2"
    )
    lbl_bg4.place(
        height=170,
        width=350,
        x=0,
        y=0
    )
    frame_fio_s = tk.Frame(
        master=s_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )
    '''frame_number_s = tk.Frame(
        master=s_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )'''
    frame_fio_s1 = tk.Frame(
        master=s_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )
    '''frame_number_s1 = tk.Frame(
        master=s_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )'''
    frame_fio_s.place(
        height=45,
        width=70,
        x=25,
        y=25
    )
    '''frame_number_s.place(
        height=45,
        width=70,
        x=25,
        y=80
    )'''
    frame_fio_s1.place(
        height=45,
        width=225,
        x=105,
        y=25
    )
    '''frame_number_s1.place(
        height=45,
        width=225,
        x=105,
        y=80
    )'''
    lbl_fio_s = tk.Label(
        master=frame_fio_s,
        text="ФИО:",
        bg="coral3"
    )
    lbl_fio_s.pack(
        expand=True,
        fill=tk.BOTH
    )
    '''lbl_number_s = tk.Label(
        master=frame_number_s,
        text="Номер:",
        bg="coral3"
    )
    lbl_number_s.pack(
        expand=True,
        fill=tk.BOTH
    )'''
    enteryfio_s = tk.Entry(
        master=frame_fio_s1,
        bg="coral3"
    )
    enteryfio_s.pack(
        expand=True,
        fill=tk.BOTH
    )
    '''enterynum_s = tk.Entry(
        master=frame_number_s1,
        bg="coral3"
    )
    enterynum_s.pack(
        expand=True,
        fill=tk.BOTH
    )'''

    frame_search = tk.Frame(
        master=s_window,
        relief=tk.GROOVE,
        bg="coral3",
        borderwidth=5
    )
    frame_search.place(
        height=30,
        width=80,
        x=245,
        y=130
    )
    btn_search = tk.Button(
        master=frame_search,
        text="Найти",
        bg="coral1",
        command=f_btn_search
    )
    btn_search.pack(
        expand=True,
        fill=tk.BOTH
    )


def f_arhiv():
    def f_war_number():
        def f_renew_number():
            del kniga[textfio]
            a = f_create()

        war_window = tk.Tk()
        war_window.title("КОНТАКТ")
        war_window.resizable(
            width=False,
            height=False
        )
        war_window.geometry("350x170")
        lbl_bg2 = tk.Label(
            master=war_window,
            background="LightSalmon2"
        )
        lbl_bg2.place(
            height=170,
            width=350,
            x=0,
            y=0
        )
        frame_fio_war = tk.Frame(
            master=war_window,
            relief=tk.GROOVE,
            bg="coral3",
            borderwidth=5
        )
        frame_number_war = tk.Frame(
            master=war_window,
            relief=tk.GROOVE,
            bg="coral3",
            borderwidth=5
        )
        frame_fio_war1 = tk.Frame(
            master=war_window,
            relief=tk.GROOVE,
            bg="coral3",
            borderwidth=5
        )
        frame_number_war1 = tk.Frame(
            master=war_window,
            relief=tk.GROOVE,
            bg="coral3",
            borderwidth=5
        )
        frame_fio_war.place(
            height=45,
            width=70,
            x=25,
            y=25
        )
        frame_number_war.place(
            height=45,
            width=70,
            x=25,
            y=80
        )
        frame_fio_war1.place(
            height=45,
            width=225,
            x=105,
            y=25
        )
        frame_number_war1.place(
            height=45,
            width=225,
            x=105,
            y=80
        )
        lbl_fio_war = tk.Label(
            master=frame_fio_war,
            text="ФИО:",
            bg="coral3"
        )
        lbl_fio_war.pack(
            expand=True,
            fill=tk.BOTH
        )
        lbl_number_war = tk.Label(
            master=frame_number_war,
            text="Номер:",
            bg="coral3"
        )
        lbl_number_war.pack(
            expand=True,
            fill=tk.BOTH
        )
        labelfio = tk.Label(
            master=frame_fio_war1,
            bg="coral3",
            text=textfio
        )
        labelfio.pack(
            expand=True,
            fill=tk.BOTH
        )
        labelnum = tk.Label(
            master=frame_number_war1,
            bg="coral3",
            text=textnum
        )
        labelnum.pack(
            expand=True,
            fill=tk.BOTH
        )

        frame_save_war = tk.Frame(
            master=war_window,
            relief=tk.GROOVE,
            bg="coral3",
            borderwidth=5
        )
        frame_save_war.place(
            height=30,
            width=80,
            x=245,
            y=130
        )
        btn_save_number = tk.Button(
            master=frame_save_war,
            text="Изменить",
            bg="coral1",
            command=f_renew_number
        )
        btn_save_number.pack(
            expand=True,
            fill=tk.BOTH
        )
    a_window = tk.Tk()
    a_window.title("АРХИВ")
    lbl_bg3 = tk.Label(
        master=a_window,
        background="LightSalmon2"
    )
    lbl_bg3.pack(fill=tk.BOTH)
    listfio = list(kniga.keys())
    listnum = list(kniga.values())
    for i in range(0, len(kniga)):
        fr_contact = tk.Frame(
            master=lbl_bg3,
            relief=tk.GROOVE,
            bg="coral3",
            borderwidth=5
        )
        fr_contact.grid(
            row=i,
            column=0,
            padx=5,
            pady=5
        )
        textfio = listfio[i]
        textnum = listnum[i]

        btn_create = tk.Button(
            master=fr_contact,
            text=textfio+textnum,
            bg="coral1",
            command=f_war_number
        )
        btn_create.pack(
            expand=True,
            fill=tk.BOTH
        )
    a_window.resizable(
        width=False,
        height=False
    )





main_window = tk.Tk()
main_window.title("КОНТАКТЫ")
main_window.resizable(
    width=False,
    height=False
)
main_window.geometry("155x170")
lbl_bg = tk.Label(background="LightSalmon2")
lbl_bg.place(
    height=170,
    width=155,
    x=0,
    y=0
)

frame1 = tk.Frame(
    master=main_window,
    relief=tk.GROOVE,
    bg="coral3",
    borderwidth=5
)
frame2 = tk.Frame(
    master=main_window,
    relief=tk.GROOVE,
    bg="coral3",
    borderwidth=5
)
frame3 = tk.Frame(
    master=main_window,
    relief=tk.GROOVE,
    bg="coral3",
    borderwidth=5
)

frame1.place(
    height=40,
    width=110,
    x=25,
    y=25
)
frame2.place(
    height=40,
    width=110,
    x=25,
    y=65
)
frame3.place(
    height=40,
    width=110,
    x=25,
    y=105
)

btn_create = tk.Button(
    master=frame1,
    text="Создать контакт",
    bg="coral1",
    command=f_create
)

btn_search = tk.Button(
    master=frame2,
    text="Поиск",
    bg="coral1",
    command=f_search
)

btn_arhiv = tk.Button(
    master=frame3,
    text="Архив",
    bg="coral1",
    command=f_arhiv
)

btn_create.pack(fill=tk.BOTH)
btn_search.pack(fill=tk.BOTH)
btn_arhiv.pack(fill=tk.BOTH)



main_window.mainloop()

