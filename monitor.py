import pyglet
pyglet.font.add_file('fonts/THSarabunIT9.ttf')
pyglet.font.add_file('fonts/THSarabunIT9 Bold.ttf')
pyglet.font.add_file('fonts/THSarabunIT9 Italic.ttf')
pyglet.font.add_file('fonts/THSarabunIT9 BoldItalic.ttf')

from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk, Image

from time import strftime
from datetime import datetime, timedelta

import sqlite3

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()
  
root = Tk()
root.state('zoomed')
root.resizable(0, 0)
root.title('หน้าจอแสดงคาบเรียน ณ ปัจจุบัน')

def date_config(now):
    if now.strftime('%a') == 'Mon': date = 'วันจันทร์ที่ '
    elif now.strftime('%a') == 'Tue': date = 'วันอังคารที่ '
    elif now.strftime('%a') == 'Wed': date = 'วันพุธที่ '
    elif now.strftime('%a') == 'Thu': date = 'วันพฤหัสบดีที่ '
    elif now.strftime('%a') == 'Fri': date = 'วันศุกร์ที่ '
    elif now.strftime('%a') == 'Sat': date = 'วันเสาร์ที่ '
    elif now.strftime('%a') == 'Sun': date = 'วันอาทิตย์ที่ '

    if now.strftime('%m') == '01': month = ' มกราคม'
    elif now.strftime('%m') == '02': month = ' กุมภาพันธ์'
    elif now.strftime('%m') == '03': month  = ' มีนาคม'
    elif now.strftime('%m') == '04': month = ' เมษายน'
    elif now.strftime('%m') == '05': month = ' พฤษภาคม'
    elif now.strftime('%m') == '06': month = ' มิถุนายน'
    elif now.strftime('%m') == '07': month = ' กรกฎาคม'
    elif now.strftime('%m') == '08': month = ' สิงหาคม'
    elif now.strftime('%m') == '09': month = ' กันยายน'
    elif now.strftime('%m') == '10': month = ' ตุลาคม'
    elif now.strftime('%m') == '11': month = ' พฤศจิกายน'
    elif now.strftime('%m') == '12': month = ' ธันวาคม'

    return date + now.strftime("%#d") + month + " พ.ศ. " + str(int(now.strftime('%Y')) + 543)
  
def local_config():
    now = datetime.now()
    timeout_check(now)
    date_text.config(text = date_config(now))
    time_text.config(text = 'เวลา ' + now.strftime('%H:%M:%S') + ' น.')
    desc_update(now)
    time_text.after(1000, local_config)

def desc_config(inst, subj):
    instructor.config(text = inst)
    subject.config(text = subj)

def period(now, bgn, end):
    if datetime.strptime(bgn, '%H:%M').time() <= now.time() <= datetime.strptime(end, '%H:%M').time(): return True
    else : return False

def desc_update(now):
    if now.strftime('%a') == 'Mon':
        mon_desc = cursor.execute('SELECT * FROM mon').fetchall()
        if period(now, '08:10', '09:00'): desc_config(mon_desc[0][0], mon_desc[0][1])
        elif period(now, '09:10', '10:00'): desc_config(mon_desc[1][0], mon_desc[1][1])
        elif period(now, '10:20', '11:10'): desc_config(mon_desc[2][0], mon_desc[2][1])
        elif period(now, '11:20', '12:10'): desc_config(mon_desc[3][0], mon_desc[3][1])
        elif period(now, '12:20', '13:00'): desc_config(mon_desc[4][0], mon_desc[4][1])
        elif period(now, '13:10', '14:00'): desc_config(mon_desc[5][0], mon_desc[5][1])
        elif period(now, '14:10', '15:00'): desc_config(mon_desc[6][0], mon_desc[6][1])
        elif period(now, '15:10', '17:30'): desc_config(mon_desc[7][0], mon_desc[7][1])
        elif period(now, '17:30', '18:00'): desc_config(mon_desc[8][0], mon_desc[8][1])
        else : desc_idle()
    elif now.strftime('%a') == 'Tue':
        tue_desc = cursor.execute('SELECT * FROM tue').fetchall()
        if period(now, '08:10', '09:00'): desc_config(tue_desc[0][0], tue_desc[0][1])
        elif period(now, '09:10', '10:00'): desc_config(tue_desc[1][0], tue_desc[1][1])
        elif period(now, '10:20', '12:10'): desc_config(tue_desc[2][0], tue_desc[2][1])
        elif period(now, '12:20', '13:00'): desc_config(tue_desc[3][0], tue_desc[3][1])
        elif period(now, '13:10', '14:00'): desc_config(tue_desc[4][0], tue_desc[4][1])
        elif period(now, '14:10', '15:00'): desc_config(tue_desc[5][0], tue_desc[5][1])
        elif period(now, '15:10', '16:00'): desc_config(tue_desc[6][0], tue_desc[6][1])
        elif period(now, '16:10', '18:00'): desc_config(tue_desc[7][0], tue_desc[7][1])
        else : desc_idle()
    elif now.strftime('%a') == 'Wed':
        wed_desc = cursor.execute('SELECT * FROM wed').fetchall()
        if period(now, '08:10', '09:00'): desc_config(wed_desc[0][0], wed_desc[0][1])
        elif period(now, '09:10', '10:00'): desc_config(wed_desc[1][0], wed_desc[1][1])
        elif period(now, '10:20', '11:10'): desc_config(wed_desc[2][0], wed_desc[2][1])
        elif period(now, '11:20', '12:10'): desc_config(wed_desc[3][0], wed_desc[3][1])
        elif period(now, '12:20', '13:00'): desc_config(wed_desc[4][0], wed_desc[4][1])
        elif period(now, '13:10', '16:00'): desc_config(wed_desc[5][0], wed_desc[5][1])
        elif period(now, '16:10', '18:00'): desc_config(wed_desc[6][0], wed_desc[6][1])
        else : desc_idle()
    elif now.strftime('%a') == 'Thu':
        thu_desc = cursor.execute('SELECT * FROM thu').fetchall()
        if period(now, '08:10', '10:00'): desc_config(thu_desc[0][0], thu_desc[0][1])
        elif period(now, '10:20', '11:10'): desc_config(thu_desc[1][0], thu_desc[1][1])
        elif period(now, '11:20', '12:10'): desc_config(thu_desc[2][0], thu_desc[2][1])
        elif period(now, '12:20', '13:00'): desc_config(thu_desc[3][0], thu_desc[3][1])
        elif period(now, '13:10', '14:00'): desc_config(thu_desc[4][0], thu_desc[4][1])
        elif period(now, '14:10', '15:00'): desc_config(thu_desc[5][0], thu_desc[5][1])
        elif period(now, '15:10', '16:00'): desc_config(thu_desc[6][0], thu_desc[6][1])
        elif period(now, '16:10', '18:00'): desc_config(thu_desc[7][0], thu_desc[7][1])
        else : desc_idle()
    elif now.strftime('%a') == 'Fri':
        fri_desc = cursor.execute('SELECT * FROM fri').fetchall()
        if period(now, '08:10', '09:00'): desc_config(fri_desc[0][0], fri_desc[0][1])
        elif period(now, '09:10', '10:00'): desc_config(fri_desc[1][0], fri_desc[1][1])
        elif period(now, '10:20', '12:10'): desc_config(fri_desc[2][0], fri_desc[2][1])
        elif period(now, '12:20', '13:00'): desc_config(fri_desc[3][0], fri_desc[3][1])
        elif period(now, '13:10', '14:00'): desc_config(fri_desc[4][0], fri_desc[4][1])
        elif period(now, '14:10', '15:00'): desc_config(fri_desc[5][0], fri_desc[5][1])
        elif period(now, '15:10', '16:00'): desc_config(fri_desc[6][0], fri_desc[6][1])
        else : desc_idle()
    else : desc_config('ไม่มีผู้สอน', 'วันหยุด เสาร์ - อาทิตย์')

def desc_idle():
    desc_config('ไม่มีผู้สอน', 'ช่วงพัก');

def reset_table(date):
        cursor.execute('DELETE FROM ' + date + ';')
        cursor.execute('INSERT INTO ' + date + ' SELECT * FROM ' + date + '_def;')

        conn.commit()

def timeout_check(now):
    timeout_date = cursor.execute('SELECT * FROM timeout').fetchall()

    for i in range(len(timeout_date)):
        if now.strftime('%#d/%#m/%Y') == timeout_date[i][0]:
            reset_table('mon')
            reset_table('tue')
            reset_table('wed')
            reset_table('thu')
            reset_table('fri')

            cursor.execute('DELETE FROM timeout WHERE date = \'' + timeout_date[i][0] + '\';')
            conn.commit()

logo_img = ImageTk.PhotoImage(Image.open("img/logo.png").resize((83, 83)))
logo = Label(image = logo_img)
logo.image = logo_img

#วัน font = (ฟอนต์, ขนาดตัวอักษร), foreground = สี *สามารถใช้ hex code แทนชื่อสีได้
date_text = Label(root, font = ('THSarabunIT๙-Bold', 24))
#เวลา font = (ฟอนต์, ขนาดตัวอักษร), foreground = สี *สามารถใช้ hex code แทนชื่อสีได้
time_text = Label(root, font = ('THSarabunIT๙-Bold', 36))
#ชื่อผู้ฝึกสอน font = (ฟอนต์, ขนาดตัวอักษร), foreground = สี *สามารถใช้ hex code แทนชื่อสีได้
instructor = Label(root, font = ('THSarabunIT๙-Bold', 40), foreground = 'blue')
#ชื่อวิชา font = (ฟอนต์, ขนาดตัวอักษร), foreground = สี *สามารถใช้ hex code แทนชื่อสีได้
subject = Label(root, font = ('THSarabunIT๙-Bold', 36), foreground = 'red')

main_btn_style = Style()
main_btn_style.configure('W.TButton',
    width = 10,
    height = 50,
    font = ('THSarabunIT๙-Bold', 20))

sub_btn_style = Style()
sub_btn_style.configure('X.TButton',
    width = 15,
    height = 50,
    font = ('THSarabunIT๙-Bold', 16))

def setting_menu():
    top = Toplevel(root)
    top.geometry("250x150")
    top.resizable(0, 0)
    top.title("การตั้งค่า")

    def reset_alltable():
        reset_table('mon')
        reset_table('tue')
        reset_table('wed')
        reset_table('thu')
        reset_table('fri')

        cursor.execute('DELETE FROM timeout;')
        conn.commit()

        top.destroy()
        top.update()
    
    def edit_menu():
        top.destroy()
        top.update()

        edit_menu = Toplevel(root)
        edit_menu.geometry("250x650")
        edit_menu.resizable(0, 0)
        edit_menu.title("แลกคาบ")

        def sec1_date_changed(event):
            if sec1_date.get() == 'วันจันทร์': date1 = 'mon'
            elif sec1_date.get() == 'วันอังคาร': date1 = 'tue'
            elif sec1_date.get() == 'วันพุธ': date1 = 'wed'
            elif sec1_date.get() == 'วันพฤหัสบดี': date1 = 'thu'
            elif sec1_date.get() == 'วันศุกร์': date1 = 'fri'

            sub1s = list()
            for i in range(len(cursor.execute('SELECT subject FROM ' + date1).fetchall())):
                sub1s.append(cursor.execute('SELECT subject FROM ' + date1).fetchall()[i][0])
            
            sub1.set(sub1s[0])
            sec1_box['values'] = tuple(sub1s)
        
        def sec2_date_changed(event):
            if sec2_date.get() == 'วันจันทร์': date2 = 'mon'
            elif sec2_date.get() == 'วันอังคาร': date2 = 'tue'
            elif sec2_date.get() == 'วันพุธ': date2 = 'wed'
            elif sec2_date.get() == 'วันพฤหัสบดี': date2 = 'thu'
            elif sec2_date.get() == 'วันศุกร์': date2 = 'fri'

            sub2s = list()
            for i in range(len(cursor.execute('SELECT subject FROM ' + date2).fetchall())):
                sub2s.append(cursor.execute('SELECT subject FROM ' + date2).fetchall()[i][0])
            
            sub2.set(sub2s[0])
            sec2_box['values'] = tuple(sub2s)
        
        def edit_apply():
            inst1 = cursor.execute('SELECT instructor FROM ' + date1 + ' WHERE subject = \'' + sub1.get() + '\';').fetchall()[0][0]
            inst2 = cursor.execute('SELECT instructor FROM ' + date2 + ' WHERE subject = \'' + sub2.get() + '\';').fetchall()[0][0]

            cursor.execute('UPDATE ' + date2 + ' SET instructor = \'รอเปลี่ยน\', subject = \'รอเปลี่ยน\' WHERE instructor = \'' + inst2 + '\' AND subject = \'' + sub2.get() + '\';')
            cursor.execute('UPDATE ' + date1 + ' SET instructor = \'' + inst2 + '\', subject = \'' + sub2.get() + '\' WHERE instructor = \'' + inst1 + '\' AND subject = \'' + sub1.get() + '\';')
            cursor.execute('UPDATE ' + date2 + ' SET instructor = \'' + inst1 + '\', subject = \'' + sub1.get() + '\' WHERE instructor = \'รอเปลี่ยน\' AND subject = \'รอเปลี่ยน\';')

            now = datetime.now()
            timeout_date = now + timedelta(days = timeout.get())

            if cursor.execute('SELECT count(date) FROM timeout WHERE date = \'' + timeout_date.strftime('%#d/%#m/%Y') + '\'').fetchone()[0] < 1:
                cursor.execute('INSERT INTO timeout VALUES(\'' + timeout_date.strftime('%#d/%#m/%Y') + '\')')

            conn.commit()

            edit_menu.destroy()
            edit_menu.update()

        Label(edit_menu, text='ตั้งเวลาคืนค่าตารางเรียนอัตโนมัติ', font = ('THSarabunIT๙-Bold', 14)).pack(pady = (30, 5))

        timeout = IntVar(edit_menu, 1)
        timeout_values = {
            "๑ วัน" : 1,
            "๒ วัน" : 2,
            "๓ วัน" : 3,
            "๔ วัน" : 4,
            "๕ วัน" : 5,
            "๖ วัน" : 6,
            "๗ วัน" : 7
        }

        for (text, value) in timeout_values.items():
            Radiobutton(edit_menu, text = text, variable = timeout, value = value).pack(pady = (5, 0))

        sec1_date_label = Label(edit_menu, text='วันที่เรียนคาบที่ 1', font = ('THSarabunIT๙-Bold', 14))
        sec1_date_label.pack(pady = (20, 0))

        sec1_date = StringVar(edit_menu, 'วันจันทร์')
        sec1_date_box = Combobox(edit_menu, textvariable=sec1_date)
        sec1_date_box['values'] = ['วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์']
        sec1_date_box['state'] = 'readonly'
        sec1_date_box.bind('<<ComboboxSelected>>', sec1_date_changed)
        sec1_date_box.pack(pady = (10, 0))

        date1 = str()
        if sec1_date.get() == 'วันจันทร์': date1 = 'mon'
        elif sec1_date.get() == 'วันอังคาร': date1 = 'tue'
        elif sec1_date.get() == 'วันพุธ': date1 = 'wed'
        elif sec1_date.get() == 'วันพฤหัสบดี': date1 = 'thu'
        elif sec1_date.get() == 'วันศุกร์': date1 = 'fri'

        sec1_label = Label(edit_menu, text='คาบที่ 1', font = ('THSarabunIT๙-Bold', 14))
        sec1_label.pack(pady = (10, 0))

        sub1s = list()
        for i in range(len(cursor.execute('SELECT subject FROM ' + date1).fetchall())):
            sub1s.append(cursor.execute('SELECT subject FROM ' + date1).fetchall()[i][0])

        sub1 = StringVar(edit_menu, sub1s[0])
        sec1_box = Combobox(edit_menu, textvariable=sub1)
        sec1_box['values'] = tuple(sub1s)
        sec1_box['state'] = 'readonly'
        sec1_box.pack(pady = (10, 30))

        sec2_label = Label(edit_menu, text='วันที่เรียนคาบที่ 2', font = ('THSarabunIT๙-Bold', 14))
        sec2_label.pack()

        sec2_date = StringVar(edit_menu, 'วันจันทร์')
        sec2_date_box = Combobox(edit_menu, textvariable=sec2_date)
        sec2_date_box['values'] = ['วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์']
        sec2_date_box['state'] = 'readonly'
        sec2_date_box.bind('<<ComboboxSelected>>', sec2_date_changed)
        sec2_date_box.pack(pady = (10, 0))

        date2 = str()
        if sec2_date.get() == 'วันจันทร์': date2 = 'mon'
        elif sec2_date.get() == 'วันอังคาร': date2 = 'tue'
        elif sec2_date.get() == 'วันพุธ': date2 = 'wed'
        elif sec2_date.get() == 'วันพฤหัสบดี': date2 = 'thu'
        elif sec2_date.get() == 'วันศุกร์': date2 = 'fri'

        sec2_label = Label(edit_menu, text='คาบที่ 2', font = ('THSarabunIT๙-Bold', 14))
        sec2_label.pack(pady = (10, 0))

        sub2s = list()
        for i in range(len(cursor.execute('SELECT subject FROM ' + date2).fetchall())):
            sub2s.append(cursor.execute('SELECT subject FROM ' + date2).fetchall()[i][0])

        sub2 = StringVar(edit_menu, sub2s[0])
        sec2_box = Combobox(edit_menu, textvariable=sub2)
        sec2_box['values'] = tuple(sub2s)
        sec2_box['state'] = 'readonly'
        sec2_box.pack(pady = (10, 20))

        apply_btn = Button(edit_menu, text = "ตกลง", style = 'X.TButton', command = edit_apply)
        apply_btn.pack(anchor = 'center', pady=(15, 0))

    btn = Button(top, text ="แลกคาบ", style = 'X.TButton', command = edit_menu)
    btn.pack(pady = (30, 0))

    reset_btn = Button(top, text = "คืนค่าตารางเรียนทันที", style = 'X.TButton', command = reset_alltable)
    reset_btn.pack(anchor = 'center', pady = (20, 0))

setting_btn = Button(root, text ="การตั้งค่า", style = 'W.TButton', command = setting_menu)

logo.pack(anchor = 'center', pady = (80, 0))
date_text.pack(anchor = 'center', pady = (50, 0))
time_text.pack(anchor = 'center', pady = (0, 50))
instructor.pack(anchor = 'center')
subject.pack(anchor = 'center')

setting_btn.pack(pady = (50, 0))

local_config() 
mainloop()

conn.close()