import json
import os
import sys
from win32api import GetModuleHandle, PostQuitMessage
import win32con
from win32gui import NIF_ICON, NIF_INFO, NIF_MESSAGE, NIF_TIP, NIM_ADD, NIM_DELETE, NIM_MODIFY, WNDCLASS, CreateWindow, DestroyWindow, LoadIcon, LoadImage, RegisterClass, Shell_NotifyIcon, UpdateWindow
import psutil
import ssl
import smtplib
import urllib
from PIL import Image
from PIL import ImageColor
import subprocess
import requests
from io import BytesIO
from urllib.request import urlopen
from datetime import datetime
import ctypes
from bs4 import BeautifulSoup
import math as mather
import threading
from suntime import Sun
import datetime as dater
from ctypes import *
import zipfile
import shutil
import pickle

class globals:
    class sound:
        soundArray = [[], 0]
        def initializeSoundArray(n):
            i = 0
            while i < n:
                globals.sound.soundArray[0].append('print("system fucky!")')
                i = i + 1
            return 0
    class color:
        ticn = -3
        jsonData = {}

class system:
    def getCPU(wait):
        error = 0
        try:
            temp = 50
            temp = psutil.cpu_percent(float(wait))
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            temp = error
        return temp

class IO:
    def getJson(path):
        error = 0
        try:
            file = open(path, "r")
            jsonData = json.loads(file.read())
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            jsonData = error
        return jsonData

    def saveJson(path, jsonData):
        error = 0
        try:
            file = open(path, "w")
            file.write(json.dumps(jsonData))
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        return error

    def getFile(path):
        error = 0
        try:
            file = open(path, "r")
            jsonData = file.read()
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            jsonData = error
        return jsonData
    
    class console:
        STD_OUTPUT_HANDLE = -11
 
        class COORD(Structure):
            pass
 
        COORD._fields_ = [("X", c_short), ("Y", c_short)]

        def printAt(r, c, s):
            h = windll.kernel32.GetStdHandle(IO.console.STD_OUTPUT_HANDLE)
            windll.kernel32.SetConsoleCursorPosition(h, IO.console.COORD(c, r))
        
            c = s.encode("windows-1252")
            windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)

    def saveFile(path, jsonData):
        error = 0
        try:
            file = open(path, "w")
            file.write(jsonData)
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        return error

    def saveList(path, list: Array):
        error = 0
        try:
            file = open(path, "wb")
            pickle.dump(list, file)
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        return error

    def getList(path):
        list = []
        error = 0
        try:
            file = open(path, "rb")
            jsonData = pickle.load(file)
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            jsonData = error
        return [list, jsonData]

    def appendFile(path, jsonData):
        error = 0
        try:
            file = open(path, "a")
            file.write(jsonData)
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        return error
    
    def unpack(path, outDir):
        try:
            with zipfile.ZipFile(path, 'r') as zip_ref:
                print(zip_ref.printdir())
                print('Extracting zip resources...')
                zip_ref.extractall(outDir)
                print("Done.")
        except Exception as erro:
                print("Could not unpack zip file.")
                print(erro)

    def pack(path, dir):
        shutil.make_archive(path, 'zip', dir)

class ambience:
    def getOutStatus():
        out = 0
        if os.path.isfile('nomufflewn.derp') == True:
            out = 1
        return out

class sound:
    class globals:
        bypass = 0

    class handler:
        def handle(argsArray):
            try:
                if globals.sound.soundArray[0] == []:
                    globals.sound.initializeSoundArray(200)
                n = 'sound.player.playSound("' + str(argsArray[0]) + '", ' + str(argsArray[1]) + ', ' + str(argsArray[2]) + ', ' + str(argsArray[3]) + ', ' + str(argsArray[4]) + ', ' + str(argsArray[5]) + ')'
                globals.sound.soundArray[0][globals.sound.soundArray[1]] = threading.Thread(target=sound.handler.sn, args=n)
                globals.sound.soundArray[0][globals.sound.soundArray[1]].start()
                globals.sound.soundArray[0][globals.sound.soundArray[1]].join()
                globals.sound.soundArray[1] = globals.sound.soundArray[1] + 1
                if globals.sound.soundArray[1] > len(globals.sound.soundArray[0]):
                    globals.sound.soundArray[1] = 0
            except:
                globals.sound.soundArray[1] = 0

        def sn(*args):
            string = ""
            for x in args:
                string += x
            print(str(string))
            exec(str(string))
            exit()

    class main:
        def playSound(path, speaker, volume, speed, balence, waitBool):
            sound.handler.handle([path, speaker, volume, speed, balence, waitBool])

        def playSoundWindow(path, volume, speed, balence, waitBool):
            if str(volume)[0] == "[":
                volumeI = volume[0]
                volumeO = volume[1]
            else:
                volumeI = volume
                volumeO = volume
            if ambience.getOutStatus() == 1:
                sound.main.playSound(path.split(";")[1], 4,  volumeO, speed, balence, waitBool)
            else:
                sound.main.playSound(path.split(";")[0], 2,  volumeI, speed, balence, 0)
                sound.main.playSound(path.split(";")[1], 3,  volumeO, speed, balence, waitBool)

        def playSoundAll(path, volume, speed, balence, waitBool):
            sound.main.playSound(path, 0, volume, speed, balence, 0)
            sound.main.playSound(path, 1, volume, speed, balence, 0)
            sound.main.playSound(path, 4, volume, speed, balence, waitBool)

    class player:
        def playSound(path, speaker, volume, speed, balence, waitBool):
            if speaker == 0:
                speakern = "clock.exe"
            elif speaker == 1:
                speakern = "fireplace.exe"
            elif speaker == 2:
                speakern = "window.exe"
            elif speaker == 3:
                speakern = "outside.exe"
            elif speaker == 5:
                speakern = "light.exe"
            else:
                speakern = "windown.exe"
            if sound.globals.bypass != 1:
                execPath = 'runaudio.vbs'
            else:
                execPath = 'bypassRunAudio.vbs'
            if waitBool == 0:
                os.system('cmd.exe /c start /b "" ' + speakern + ' ' + execPath + ' ' + path + ' ' + str(volume) + ' ' + str(balence) + ' ' + str(speed) + ' ' + path.split(".")[0])
                if sound.globals.bypass == 1:
                    print("WARNING: Audio State Bypass Enabled.")
                print("Playing sound " + path + " on speaker " + speakern + " with volume " + str(volume) + " with speed of " + str(speed) + " with balence of " + str(balence) + "...")
            else:
                if sound.globals.bypass == 1:
                    print("WARNING: Audio State Bypass Enabled.")
                print("Playing sound " + path + " on speaker " + speakern + " with volume " + str(volume) + " with speed of " + str(speed) + " with balence of " + str(balence) + ". Waiting...")
                os.system('cmd.exe /c start /b /wait "" ' + speakern + ' ' + execPath + ' ' + path + ' ' + str(volume) + ' ' + str(balence) + ' ' + str(speed) + ' ' + path.split(".")[0])

class winAPI:
    def getWallpaper():
        sbuf = ctypes.create_string_buffer(512) # ctypes.c_buffer(512)
        ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_GETDESKWALLPAPER,len(sbuf),sbuf,0)
        return sbuf.value

    def setWallpaper(path):
        changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
        ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER,0,path.encode(),changed) # "".encode() = b""

    class WindowsBalloonTip:
        def __init__(self, title, msg):
            message_map = {
                    win32con.WM_DESTROY: self.OnDestroy,
            }
            # Register the Window class.
            wc = WNDCLASS()
            hinst = wc.hInstance = GetModuleHandle(None)
            wc.lpszClassName = "PythonTaskbar"
            wc.lpfnWndProc = message_map # could also specify a wndproc.
            classAtom = RegisterClass(wc)
            # Create the Window.
            style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
            self.hwnd = CreateWindow( classAtom, "Taskbar", style, \
                    0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                    0, 0, hinst, None)
            UpdateWindow(self.hwnd)
            iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            try:
                hicon = LoadImage(hinst, iconPathName, \
                        win32con.IMAGE_ICON, 0, 0, icon_flags)
            except:
                hicon = LoadIcon(0, win32con.IDI_APPLICATION)
                flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
                nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
                Shell_NotifyIcon(NIM_ADD, nid)
                Shell_NotifyIcon(NIM_MODIFY, \
                            (self.hwnd, 0, NIF_INFO, win32con.WM_USER+20,\
                            hicon, "Balloon  tooltip",msg,200,title))
                # self.show_balloon(title, msg)
                os.times.sleep(10)
                DestroyWindow(self.hwnd)
        def OnDestroy(self, hwnd, msg, wparam, lparam):
            nid = (self.hwnd, 0)
            Shell_NotifyIcon(NIM_DELETE, nid)
            PostQuitMessage(0) # Terminate the app.

    def balloon_tip(title, msg):
        w=winAPI.WindowsBalloonTip(title, msg)

class color:
    def tempCalc(temp):
        if temp > 298:
            temptype = "hot"
        elif temp > 285:
            temptype = "warm"
        elif temp > 273:
            temptype = "cool"
        elif temp > 263:
            temptype = "cold"
        elif temp <= 263:
            temptype = "freeze"
        else:
            temptype = "warm"
        return temptype

    def saturateRGB(rgb):
        rgbn = [0, 0, 0]
        if rgb[0] > rgb[1]:
            maxRGB = rgb[0]
        else:
            maxRGB = rgb[1]
        if rgb[2] > maxRGB:
            maxRGB = rgb[2]
        if rgb[0] < rgb[1]:
            minRGB = rgb[0]
        else:
            minRGB = rgb[1]
        if rgb[2] < maxRGB:
            minRGB = rgb[2]
        satMult = 255 / maxRGB
        if minRGB == rgb[0]:
            rgbn[0] = int(rgb[0] / satMult)
        elif maxRGB == rgb[0]:
            rgbn[0] = int(rgb[0] * satMult)
        else:
            rgbn[0] = rgb[0]
        if minRGB == rgb[1]:
            rgbn[1] = int(rgb[1] / satMult)
        elif maxRGB == rgb[1]:
            rgbn[1] = int(rgb[1] * satMult)
        else:
            rgbn[1] = rgb[1]
        if minRGB == rgb[2]:
            rgbn[2] = int(rgb[2] / satMult)
        elif maxRGB == rgb[2]:
            rgbn[2] = int(rgb[2] * satMult)
        else:
            rgbn[2] = rgb[2]
        return rgbn

    def getWeatherb(weather):
        weatherb = 0
        if weather == "clear":
            weatherb = 0
        if weather == "fewcloud":
            weatherb = 1000
        if weather == "somecloud":
            weatherb = 2000
        if weather == "cloud":
            weatherb = 3000
        if weather == "rain":
            weatherb = 4000
        if weather == "snow":
            weatherb = 5000
        if weather == "thunder":
            weatherb = 6000
        return weatherb

    def returnSunInfo(clouds):
        jsonData = {
            "x": "-1",
            "y": "-1",
            "z": "-1",
        }
        current = 0
        weatherb = int(clouds) * 77.5
        sunrise = (int(str(Sun(44.766, -63.686).get_local_sunrise_time(dater.date.today())).split(" ")[1].split(":")[0].split("-")[0]) * 60 * 60) + (int(str(Sun(44.766, -63.686).get_local_sunrise_time(dater.date.today())).split(" ")[1].split(":")[1].split("-")[0]) * 60) + (int(str(Sun(44.766, -63.686).get_local_sunrise_time(dater.date.today())).split(" ")[1].split(":")[2].split("-")[0]))
        sunset = (int(str(Sun(44.766, -63.686).get_local_sunset_time(dater.date.today())).split(" ")[1].split(":")[0].split("-")[0]) * 60 * 60) + (int(str(Sun(44.766, -63.686).get_local_sunset_time(dater.date.today())).split(" ")[1].split(":")[1].split("-")[0]) * 60) + (int(str(Sun(44.766, -63.686).get_local_sunset_time(dater.date.today())).split(" ")[1].split(":")[2].split("-")[0]))
        current = (int((str(dater.datetime.now().strftime("%H:%M:%S")).split(":")[0])) * 60 * 60) + (int((str(dater.datetime.now().strftime("%H:%M:%S")).split(":")[1])) * 60) + (int((str(dater.datetime.now().strftime("%H:%M:%S")).split(":")[2])))
        weatherr = (9000 * ((3) ** (-0.0000001 * ((current - sunrise) ** 2)))) + (-1.0002 ** ((-2 * current) + 45000 + (2 * sunrise))) + (9000 * ((3) ** (-0.0000001 * ((current - sunset) ** 2)))) + (-1.0002 ** ((2 * current) + 45000 - (2 * sunset))) + (2300 * ((3) ** (-0.00000005 * ((current - sunset + 3700) ** 2)))) + (2300 * ((3) ** (-0.00000005 * ((current - sunrise - 3700) ** 2))))
        nf = 6000 - weatherr + weatherb
        rgb = color.tempToRGB(nf)
        limit = 1
        limit = (1.0013 ** (current - sunset - (sunset / 80))) + (1.0013 ** -(current - sunrise - (sunrise / 80)))
        if limit < 1:
            limit = 1
        rgb[0] = int(rgb[0] / limit)
        rgb[1] = int(rgb[1] / limit)
        rgb[2] = int(rgb[2] / limit)
        if rgb[0] < 0:
            rgb[0] = 0
        if rgb[0] > 255:
            rgb[0] = 255
        if rgb[1] < 0:
            rgb[1] = 0
        if rgb[1] > 255:
            rgb[1] = 255
        if rgb[2] < 0:
            rgb[2] = 0
        if rgb[2] > 255:
            rgb[2] = 255
        if (jsonData['x'] != str(rgb[0])) or (jsonData['y'] != str(rgb[1])) or (jsonData['z'] != str(rgb[2])):
            jsonData['x'] = str(int(rgb[0]))
            jsonData['y'] = str(int(rgb[1]))
            jsonData['z'] = str(int(rgb[2]))
            print(str(current) + " ::: " + str(jsonData) + ", colorTemp: " + str(nf) + "K" + ", weatherr: " + str(weatherr) + "K" + ", weatherb: " + str(weatherb) + "K")
        return [current, jsonData, nf, weatherr, weatherb]

    def tempToRGB(nf):
        red = 0
        green = 0
        blue = 0
        try:
            if nf < 4483:
                red = int((-1.002 ** -(nf - 2990)) + 309)
            elif nf < 18823:
                red = int((((-4 * (10 ** -11)) * (nf ** 3) + 806) / (0.001 * nf)) + 130)
            else:
                red = int((-1.0004 ** (nf - 14200)) + 165)
        except:
            pass
        try:
            if nf < 6600:
                green = int((-1.0004 ** -(nf - 14200)) + 269)
            elif nf < 17900:
                green = int((((-4 * (10 ** -11)) * (nf ** 3) + 527) / (0.001 * nf)) + 170)
            else:
                green = int((-1.0004 ** (nf - 14200)) + 191)
        except:
            pass
        try:
            if nf < 6424:
                blue = int((-1.0004 ** -(nf - 16400)) + 309)
            else:
                blue = int((-1.0004 ** (nf - 16400)) + 255)
        except:
            pass
        if red < 0:
            red = 0
        if red > 255:
            red = 255
        if green < 0:
            green = 0
        if green > 255:
            green = 255
        if blue < 0:
            blue = 0
        if blue > 255:
            blue = 255
        return [red, green, blue]
    
class calc:
    def subtractLarge(numbera, numberb):
            i = 0
            out = ""
            next = numbera[-(i + 1)]
            while i < len(numbera):
                if numbera[-(i + 1)] != next:
                    math = next - int(numberb[-(i + 1)])
                else:
                    math = int(numbera[-(i + 1)]) - int(numberb[-(i + 1)])
                if math < 0:
                    try:
                        next = int(numbera[-(i + 2)]) - 1
                    except:
                        next = 0 - 1
                    math = math + 10
                else:
                    try:
                        next = int(numbera[-(i + 2)])
                    except:
                        next = 0
                if math < 0:
                    math = 0
                out = str(out) + str(math)
                i = i + 1

    def findLargestPrime(x):
        print("The factors of",x,"are:")
        nonprime = [0]
        i = 1
        exit = 0
        while exit == 0:
            if x % i == 0:
                x = x / i
                n = x
            if i > (n / 2):
                exit = 1
            i = i + 1
        return n

    def addLarge(numbera: str, numberb: str):
        if numbera.find('-') != -1:
            nega = '-'
        else:
            nega = ''
        if numberb.find('-') != -1:
            negb = '-'
        else:
            negb = ''
        numbera = numbera.replace('-', '')
        numberb = numberb.replace('-', '')
        if numbera.find(".") == -1:
            numbera = numbera + ".0"
        if numberb.find(".") == -1:
            numberb = numberb + ".0"
        print(numbera + ";" + numberb)
        decimalloc = calc.findLargestDecimal(numbera, numberb)
        numbera = numbera.replace('.', '')
        numberb = numberb.replace('.', '')
        i = 0
        out = ""
        carry = 0
        while i < len(numbera):
            print(numbera + ";" + numberb)
            math = int(nega + numbera[-(i + 1)]) + int(negb + numberb[-(i + 1)]) + int(carry)
            print(math)
            if math > 9:
                carry = str(math)[0]
                math = str(math)[1]
            else:
                carry = 0
            out = str(out) + str(math)
            i = i + 1
        if int(carry) > 0:
            out = out + str(carry)
        i = 0
        outn = ""
        while i < len(out):
            outn = outn + out[-(i + 1)]
            i = i + 1
        print(decimalloc)
        if outn[1] == '-':
            neg = -1
        else:
            neg = 1
        if neg < 0:
            outf = "-" + (outn[0:mather.floor(decimalloc / 2)] + '.' + outn[mather.floor(decimalloc / 2):len(outn)]).replace('-', '')
            locf = calc.findLargestDecimal(outf, outf)
            if locf != decimalloc:
                print('fuck')
                i = 0
                outl = outf
                while (locf != decimalloc) and (i < len(outl)):
                    try:
                        outf = "-" + (outn[-len(outn):-mather.floor(i / 2)] + '.' + outn[-mather.floor(i / 2):-1] + outn[-1]).replace('-', '')
                        locf = calc.findLargestDecimal(outf, outf)
                    except:
                        pass
                    i = i + 1
                i = 0
                while (locf != decimalloc) and (i < len(outl)):
                    try:
                        outf = "-" + (outn[0:mather.floor(i / 2)] + '.' + outn[mather.floor(i / 2):len(outn)]).replace('-', '')
                        locf = calc.findLargestDecimal(outf, outf)
                    except:
                        pass
                    i = i + 1
        else:
            outf = (outn[-len(outn):-mather.floor(decimalloc / 2)] + '.' + outn[-mather.floor(decimalloc / 2):-1] + outn[-1]).replace('-', '')
            locf = calc.findLargestDecimal(outf, outf)
            if locf != decimalloc:
                print('fuck')
                i = 0
                outl = outf
                while (locf != decimalloc) and (i < len(outl)):
                    try:
                        outf = (outn[0:mather.floor(i / 2)] + '.' + outn[mather.floor(i / 2):len(outn)]).replace('-', '')
                        locf = calc.findLargestDecimal(outf, outf)
                    except:
                        pass
                    i = i + 1
                i = 0
                while (locf != decimalloc) and (i < len(outl)):
                    try:
                        outf = (outn[-len(outn):-mather.floor(i / 2)] + '.' + outn[-mather.floor(i / 2):-1] + outn[-1]).replace('-', '')
                        locf = calc.findLargestDecimal(outf, outf)
                    except:
                        pass
                    i = i + 1
        return outf

    def addLargeInt(numbera: str, numberb: str):
        i = 0
        out = ""
        carry = 0
        while i < len(numbera):
            print(numbera + ";" + numberb)
            math = int(numbera[-(i + 1)]) + int(numberb[-(i + 1)]) + int(carry)
            print(math)
            if math > 9:
                carry = str(math)[0]
                math = str(math)[1]
            else:
                carry = 0
            out = str(out) + str(math)
            i = i + 1
        if int(carry) > 0:
            out = out + str(carry)
        i = 0
        outn = ""
        while i < len(out):
            outn = outn + out[-(i + 1)]
            i = i + 1
        return outn

    def findLargestDecimal(numbera, numberb):
        i = 0
        a = 0
        while i < len(numbera):
            if numbera[-(i + 1)] == '.':
                a = i
            i = i + 1
        i = 0
        b = 0
        while i < len(numberb):
            if numberb[-(i + 1)] == '.':
                b = i
            i = i + 1
        out = a + b
        print(';' + str(out))
        return out

    def multiplyLarge(numbera, numberb):
        i = 0
        outls = []
        if numbera.find(".") == -1:
            numbera = numbera + ".0"
        if numberb.find(".") == -1:
            numberb = numberb + ".0"
        decimalloc = calc.findLargestDecimal(numbera, numberb)
        numbera = numbera.replace('.', '')
        numberb = numberb.replace('.', '')
        while i < len(numberb):
            n = 0
            carry = 0
            outa = ""
            while n < len(numbera):
                math = (int(numbera[-(n + 1)]) * int(numberb[-(i + 1)])) + carry
                if 9 < math:
                    print(math)
                    carry = int(str(math)[0])
                    math = int(str(math)[1])
                else:
                    carry = 0
                outa = outa + str(math)
                n = n + 1
            outa = outa + str(carry)
            f = 0
            outb = ""
            while f < len(outa):
                outb = outb + outa[-(f + 1)]
                f = f + 1
            outls.append(outb)
            i = i + 1
        i = 0
        outn = "0"
        print(outls)
        zero = ""
        while i < len(outls):
            values = calc.equalizeDigits(outn, outls[i] + str(zero))
            outn = calc.addLargeInt(values[0], values[1]).split(".")[0]
            zero = zero + "0"
            print(values)
            i = i + 1
        exit = 0
        i = 0
        while exit == 0:
            if outn[i] != "0":
                sub = i
                exit = 1
            i = i + 1
        return outn[-len(outn):-(decimalloc)] + "." + outn[-(decimalloc):-1] + outn[-1] + "0"

    def equalizeDigits(numbera, numberb):
        if numbera.find('-') != -1:
            nega = '-'
        else:
            nega = ''
        if numberb.find('-') != -1:
            negb = '-'
        else:
            negb = ''
        numbera = numbera.replace('-', '')
        numberb = numberb.replace('-', '')
        if len(numbera.split(".")[0]) < len(numberb.split(".")[0]):
            i = len(numbera.split(".")[0])
            while i < len(numberb.split(".")[0]):
                numbera = "0" + numbera
                i = i + 1
        elif len(numberb.split(".")[0]) < len(numbera.split(".")[0]):
            i = len(numberb.split(".")[0])
            while i < len(numbera.split(".")[0]):
                numberb = "0" + numberb
                i = i + 1
        try:
            if len(numbera.split(".")[1]) < len(numberb.split(".")[1]):
                i = len(numbera.split(".")[1])
                while i < len(numberb.split(".")[1]):
                    numbera = numbera + "0"
                    i = i + 1
            elif len(numberb.split(".")[1]) < len(numbera.split(".")[1]):
                i = len(numberb.split(".")[1])
                while i < len(numbera.split(".")[1]):
                    numberb = numberb + "0"
                    i = i + 1
        except:
            pass
        return [nega + numbera, negb + numberb]
    
    def cleanNumber(number: str):
        i = 0
        while i < len(number):
            if number[i] != "0":
                start = i
                if number[i] == '.':
                    start = i - 1
                i = len(number)
            i = i + 1
        i = 0
        while i < len(number):
            if number[-(i + 1)] != "0":
                end = -(i)
                if number[i] == '.':
                    end = -i + 1
                i = len(number)
            i = i + 1
        print(str(start) + ";" + str(end))
        out = number[start:end]
        if start == 0:
            if end == 0:
                out = number
        return out + "0"

    def mathLargeFloat(numbera: str, arth: str, numberb: str):
        if arth == "+":
            if numbera.find('.') == -1:
                numbera = numbera + ".0"
            if numberb.find('.') == -1:
                numberb = numberb + ".0"
        values = calc.equalizeDigits(numbera, numberb)
        numberan = values[0]
        numberbn = values[1]
        if arth == "+":
            print(numberan + '#' + numberbn)
            outn = calc.addLarge(numberan, numberbn)
        if arth == "-":
            i = 0
            out = ""
            next = numbera[-(i + 1)]
            while i < len(numbera):
                if numbera[-(i + 1)] != next:
                    math = next - int(numberb[-(i + 1)])
                else:
                    math = int(numbera[-(i + 1)]) - int(numberb[-(i + 1)])
                if math < 0:
                    try:
                        next = int(numbera[-(i + 2)]) - 1
                    except:
                        next = 0 - 1
                    math = math + 10
                else:
                    try:
                        next = int(numbera[-(i + 2)])
                    except:
                        next = 0
                if math < 0:
                    math = 0
                out = str(out) + str(math)
                i = i + 1
        if arth == "*":
            outn = calc.multiplyLarge(numbera, numberb)
            # outn = ""
            # while i < len(out):
            #     outn = outn + out[-(i + 1)]
            #     i = i + 1
        print(outn)
        return calc.cleanNumber(outn)

    def abs(num):
        out = num
        if str(num)[0] == '-':
            out = str(num)[1:]
        return out

class net:
    def sendEmail(userEmail, password, toEmail, inputType, messageData, server, port):
        try:
            error = 0
            smtp_server = server
            sender_email = userEmail
            receiver_email = toEmail
            if inputType == 0:
                message = messageData
            elif inputType == 1:
                message = str(IO.getFile(messageData)).encode('ascii', 'ignore')
            else:
                error = 1
                print("Please enter a valid message format, formats are < -text | -file>")
            try:
                if error != 1:
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()  # Can be omitted
                        server.starttls(context=context)
                        server.ehlo()  # Can be omitted
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                    print("email sent")
                    error = 0
                else:
                    print("email failed to send.")
                    error = 1
            except Exception as err:
                print("email failed to send.")
                print("Email messaging error:", sys.exc_info())
                error = err
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            error = err
        return error

    def getJsonAPI(url):
        ssl._create_default_https_context = ssl._create_unverified_context
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        response = urlopen(req)
        data_json = json.loads(response.read())
        return data_json
    
    def getRawAPI(url, myobj):
        ssl._create_default_https_context = ssl._create_unverified_context
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        response = urlopen(req)
        data_json = response.read()
        return data_json

    def makePostRequest(url, myobj):
        myobj['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        ssl._create_default_https_context = ssl._create_unverified_context
        response = requests.post(url, data = myobj)
        # req = urllib.request.Request(
        #     url, 
        #     data=None, 
        #     headers={
        #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        #     }
        # )
        # response = urlopen(req)
        # data_json = response.read()
        data_json = response.text
        return data_json

    def getTextAPI(url):
        ssl._create_default_https_context = ssl._create_unverified_context
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        response = urlopen(req)
        data_json = BeautifulSoup(response.read(), 'html.parser')
        text = data_json.find_all(text=True)
        data_out = cipher.listToString(text)
        return data_out

    def postAPI(url, node, data, encodeBool):
        ssl._create_default_https_context = ssl._create_unverified_context
        if int(encodeBool) != 0:
            encodedData = cipher.base64_encode(data)
        else:
            encodedData = data
        url = url + "?" + node + "=" + encodedData
        print(url)
        response = urlopen(url)
        data_json = response.read()
        return data_json
    
    def download(urlf, path, maxB):
        i = 0
        n = 0
        local_filename = path
        # NOTE the stream=True parameter below
        with requests.get(urlf, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    i = i + 1
                    f.write(chunk)
                    percent = (n / maxB) * 100
                    print("Download Progress: " + str(int(percent)) + "% ::: iter_bytepos: " + str(n) + " ::: writing file chunk " + str(i) + "...")
                    n = n + 8192
        return local_filename

class cipher:  
    def base64_encode(s):
        error = 0
        try:
            temp = str(os.environ['temp'])
            file = open(temp + "\\out_ser.cxl", "w")
            file.write(s)
            file.close()
            try:
                subprocess.check_output("certutil -f -encode \"" + temp + "\\out_ser.cxl\" \"" + temp + "\\dump_ser.base64\"", shell=True)
                file = open(temp + "\\dump_ser.base64", "r")
                encode = str(file.read())
                file.close()
                encode = encode.replace("=", "$")
                encode = encode.replace("+", "?")
                encode = encode.replace("/", "!")
                encode = (encode.split("-----BEGIN CERTIFICATE-----")[1]).split("-----END CERTIFICATE-----")[0].replace("\n", "")
            except:
                encode = "ZWNobyBmdWNrIA0K"
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            encode = error
        return encode
        
    def base64_decode(s):
        error = 0
        try:
            temp = str(os.environ['temp'])
            encode = s.replace("$", "=")
            encode = encode.replace("?", "+")
            encode = encode.replace("!", "/")
            encode = encode.replace("\n", "")
            encode = encode.replace(" ", "")
            encode = encode.replace("\"", "")
            file = open(temp + "\\out_ser.cxl", "w")
            file.write(encode)
            file.close()
            try:
                subprocess.check_output("certutil -f -decode \"" + temp + "\\out_ser.cxl\" \"" + temp + "\\dump_ser.base64\"", shell=True)
                file = open(temp + "\\dump_ser.base64", "r")
                decode = str(file.read())
                file.close()
            except:
                decode = "Operation was sucsessful."
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            decode = error
        return decode

    def listToString(s):
        str1 = " "
        return (str1.join(s))

    class tools:
        def removeDuplicateChars(string: str):
            newString = ""
            i = 0
            while i < len(string):
                if newString.find(string[i]) == -1:
                    newString = newString + string[i]
                i = i + 1
            return newString

        def listToString(s):
            str1 = " "
            return (str1.join(s))
    
    class enigma:
        class globals:
            null = ""
            charToNum = {' ': '32', '!': '33', '"': '34', '#': '35', '$': '36', '%': '37', '&': '38', "'": '39', '(': '40', ')': '41', '*': '42', '+': '43', ',': '44', '-': '45', '.': '46', '/': '47', '0': '48', '1': '49', '2': '50', '3': '51', '4': '52', '5': '53', '6': '54', '7': '55', '8': '56', '9': '57', ':': '58', ';': '59', '<': '60', '=': '61', '>': '62', '?': '63', '@': '64', 'A': '65', 'B': '66', 'C': '67', 'D': '68', 'E': '69', 'F': '70', 'G': '71', 'H': '72', 'I': '73', 'J': '74', 'K': '75', 'L': '76', 'M': '77', 'N': '78', 'O': '79', 'P': '80', 'Q': '81', 'R': '82', 'S': '83', 'T': '84', 'U': '85', 'V': '86', 'W': '87', 'X': '88', 'Y': '89', 'Z': '90', '[': '91', '\\': '92', ']': '93', '^': '94', '_': '95', '`': '96', 'a': '97', 'b': '98', 'c': '99', 'd': '100', 'e': '101', 'f': '102', 'g': '103', 'h': '104', 'i': '105', 'j': '106', 'k': '107', 'l': '108', 'm': '109', 'n': '110', 'o': '111', 'p': '112', 'q': '113', 'r': '114', 's': '115', 't': '116', 'u': '117', 'v': '118', 'w': '119', 'x': '120', 'y': '121', 'z': '122', '{': '123', '|': '124', '}': '125', '~': '126'}
            numToChar = {'32': ' ', '33': '!', '34': '"', '35': '#', '36': '$', '37': '%', '38': '&', '39': "'", '40': '(', '41': ')', '42': '*', '43': '+', '44': ',', '45': '-', '46': '.', '47': '/', '48': '0', '49': '1', '50': '2', '51': '3', '52': '4', '53': '5', '54': '6', '55': '7', '56': '8', '57': '9', '58': ':', '59': ';', '60': '<', '61': '=', '62': '>', '63': '?', '64': '@', '65': 'A', '66': 'B', '67': 'C', '68': 'D', '69': 'E', '70': 'F', '71': 'G', '72': 'H', '73': 'I', '74': 'J', '75': 'K', '76': 'L', '77': 'M', '78': 'N', '79': 'O', '80': 'P', '81': 'Q', '82': 'R', '83': 'S', '84': 'T', '85': 'U', '86': 'V', '87': 'W', '88': 'X', '89': 'Y', '90': 'Z', '91': '[', '92': '\\', '93': ']', '94': '^', '95': '_', '96': '`', '97': 'a', '98': 'b', '99': 'c', '100': 'd', '101': 'e', '102': 'f', '103': 'g', '104': 'h', '105': 'i', '106': 'j', '107': 'k', '108': 'l', '109': 'm', '110': 'n', '111': 'o', '112': 'p', '113': 'q', '114': 'r', '115': 's', '116': 't', '117': 'u', '118': 'v', '119': 'w', '120': 'x', '121': 'y', '122': 'z', '123': '{', '124': '|', '125': '}', '126': '~'}

        class enigma:
            salt = 0
            rotors = []
            plugboard = {}
            plugboardRev = {}
            plugboardKey = ""
            plugboardMax = 0
            rotorCount = 0
            class rotor:
                def count():
                    i = 0
                    cipher.enigma.enigma.rotors[0] = cipher.enigma.enigma.rotors[0] + 1
                    while i < 5:
                        if cipher.enigma.enigma.rotors[i] > 95:
                            cipher.enigma.enigma.rotors[i + 1] = cipher.enigma.enigma.rotors[i + 1] + 1
                            cipher.enigma.enigma.rotors[i] = 0
                        i = i + 1

            def init(salt, rotorCount: int, plugboardKey: str):
                cipher.enigma.enigma.plugboardKey = cipher.tools.removeDuplicateChars(plugboardKey)
                i = 0
                cipher.enigma.enigma.rotorCount = rotorCount
                while i < rotorCount:
                    cipher.enigma.enigma.rotors.append(0)
                    i = i + 1
                cipher.enigma.enigma.salt = (salt)
                i = 32
                plugboardMax = 0
                while i < 127:
                    if i < (len(cipher.enigma.enigma.plugboardKey) + 32):
                        cipher.enigma.enigma.plugboard[str(i)] = cipher.enigma.globals.charToNum[cipher.enigma.enigma.plugboardKey[int(i - 32)]]
                        if plugboardMax < int(cipher.enigma.globals.charToNum[str(cipher.enigma.enigma.plugboardKey[int(i - 32)])]):
                            plugboardMax = int(cipher.enigma.globals.charToNum[str(cipher.enigma.enigma.plugboardKey[int(i - 32)])])
                    else:
                        if str(cipher.enigma.enigma.plugboard).find(": \'" + str(i) + "\'") != -1:
                            n = 32
                            exitN = 0
                            while (n < 127) and (exitN != 1):
                                if str(cipher.enigma.enigma.plugboard).find(": \'" + str(n) + "\'") == -1:
                                    cipher.enigma.enigma.plugboard[str(i)] = str(n)
                                    exitN = 1
                                n = n + 1
                        else:
                            cipher.enigma.enigma.plugboard[str(i)] = str(i)

                    i = i + 1
                cipher.enigma.enigma.plugboardMax = plugboardMax
                i = 32
                while i < 127:
                    key = cipher.enigma.enigma.plugboard[str(i)]
                    cipher.enigma.enigma.plugboardRev[key] = str(i)
                    i = i + 1

        def dummy(dum):
            return dum

        class work:
            def encode(string):
                rotorCount = cipher.enigma.enigma.rotorCount
                cipher.enigma.enigma.rotors =  []
                i = 0
                cipher.enigma.enigma.rotorCount = rotorCount
                while i < rotorCount:
                    cipher.enigma.enigma.rotors.append(0)
                    i = i + 1
                i = 0
                new = ""
                newString = ""
                while i < len(string):
                    try:
                        dummy(cipher.enigma.globals.charToNum[string[i]])
                        new = int(cipher.enigma.enigma.plugboard[cipher.enigma.globals.charToNum[string[i]]])
                        n = 0
                        while n < len(cipher.enigma.enigma.rotors):
                            new = new + cipher.enigma.enigma.rotors[n]
                            if new > 126:
                                new = new - 95
                            cipher.enigma.enigma.rotor.count()
                            n = n + 1
                        n = 0
                        while n < len(cipher.enigma.enigma.rotors):
                            new = new + cipher.enigma.enigma.rotors[len(cipher.enigma.enigma.rotors) - (n + 1)]
                            if new > 126:
                                new = new - 95
                            cipher.enigma.enigma.rotor.count()
                            n = n + 1
                        if new > 126:
                            new = new - 95
                        new = cipher.enigma.enigma.plugboard[str(new)]
                        newString = newString + cipher.enigma.globals.numToChar[str(new)]
                    except:
                        newString = newString + string[i]
                    i = i + 1
                return newString
            
            def decode(string):
                rotorCount = cipher.enigma.enigma.rotorCount
                cipher.enigma.enigma.rotors =  []
                i = 0
                cipher.enigma.enigma.rotorCount = rotorCount
                while i < rotorCount:
                    cipher.enigma.enigma.rotors.append(0)
                    i = i + 1
                i = 0
                new = ""
                newString = ""
                while i < len(string):
                    try:
                        dummy(cipher.enigma.globals.charToNum[string[i]])
                        new = int(cipher.enigma.enigma.plugboardRev[cipher.enigma.globals.charToNum[string[i]]])
                        n = 0
                        while n < len(cipher.enigma.enigma.rotors):
                            new = new - cipher.enigma.enigma.rotors[n]
                            if new < 32:
                                new = new + 95
                            cipher.enigma.enigma.rotor.count()
                            n = n + 1
                        n = 0
                        while n < len(cipher.enigma.enigma.rotors):
                            new = new - cipher.enigma.enigma.rotors[len(cipher.enigma.enigma.rotors) - (n + 1)]
                            if new < 32:
                                new = new + 95
                            cipher.enigma.enigma.rotor.count()
                            n = n + 1
                        if new > 126:
                            new = new - 95
                        new = cipher.enigma.enigma.plugboardRev[str(new)]
                        newString = newString + cipher.enigma.globals.numToChar[str(new)]
                    except:
                        newString = newString + string[i]
                    i = i + 1
                return newString

class imageWorker:
    def getRGB(path):
        image_url = path
        resp = requests.get(image_url)
        assert resp.ok
        img = Image.open(BytesIO(resp.content)).convert('RGB')
        img2 = img.resize((1, 1))
        nf = img2.getpixel((0, 0))
        colorrgb = ImageColor.getcolor('#{:02x}{:02x}{:02x}'.format(*nf), "RGB")
        # print('#{:02x}{:02x}{:02x}'.format(*nf))
        return colorrgb

class clock:
    def getDateTime(utc = False):
        if utc:
            daten = datetime.utcnow()
        else:
            daten = datetime.now()
        dateArray = [1970, 1, 1, 0, 0, 0]
        dateArray[0] = int(str(daten).split(" ")[0].split("-")[0])
        dateArray[1] = int(str(daten).split(" ")[0].split("-")[1])
        dateArray[2] = int(str(daten).split(" ")[0].split("-")[2])
        dateArray[3] = int(str(daten).split(" ")[1].split(":")[0])
        dateArray[4] = int(str(daten).split(" ")[1].split(":")[1])
        dateArray[5] = int(str(daten).split(" ")[1].split(":")[2].split(".")[0])
        return dateArray

    def utcFormatToArray(string):
        year = int(string.split("-")[0])
        month = int(string.split("-")[1])
        day = int(string.split("-")[2].split("T")[0])
        hour = int(string.split("T")[1].split(":")[0])
        minute = int(string.split("T")[1].split(":")[1])
        second = int(string.split("T")[1].split(":")[2].split("+")[0])
        millis = 0
        return [year, month, day, hour, minute, second]

    def getTimeDialation():
        staArray = clock.getDateTime()
        utcArray = clock.getDateTime(True)
        diaArray = [0, 0, 0, 0, 0, 0]
        # i = 0
        # while i < len(diaArray):
        #     diaArray[i] = staArray[i] - utcArray[i]
        #     i = i + 1
        diaArray[3] = 24 - (staArray[3] - utcArray[3])
        return diaArray

    def fixDateArray(dateArray):
        while dateArray[4] > 60:
            dateArray[4] = dateArray[4] - 60
            dateArray[3] = dateArray[3] + 1
        while dateArray[3] > 24:
            dateArray[3] = dateArray[3] - 24
            dateArray[2] = dateArray[2] + 1
        while dateArray[2] > clock.getMonthEnd(dateArray[1]):
            dateArray[2] = dateArray[2] - clock.getMonthEnd(dateArray[1])
            dateArray[1] = dateArray[1] + 1
        while dateArray[1] > 12:
            dateArray[1] = dateArray[1] - 12
            dateArray[0] = dateArray[0] + 1
        return dateArray

    def solveForDialation(diaArray, staArray):
        outArray = [0, 0, 0, 0, 0, 0]
        xArray = [1, 12, "me", 24, 60, 60]
        i = 0
        while i < len(diaArray):
            outArray[i] = (staArray[i] - diaArray[i])
            i = i + 1
        i = len(outArray) - 1
        while i > 1:
            while outArray[i] < 0:
                    if xArray[i] != "me":
                        outArray[i] = outArray[i] + xArray[i]
                    else:
                        outArray[i] = outArray[i] + clock.getMonthEnd(outArray[1])
                    outArray[i - 1] = outArray[i - 1] - 1
            i = i - 1
        return outArray

    def getDayOfWeek():
        out = datetime.today().weekday() + 1
        if out == 7:
            out = 0
        return out
        
    def getMonthEnd(month):
        mon31 = [12, 10, 8, 7, 5, 3, 1]
        i = 0
        out = 28
        while i < len(mon31):
            if (mon31[i] == month):
                out = 31
            i = i + 1
        if out != 31:
            if month != 2:
                out = 30
        return out

    def getMidnight(dateArray):
        datef = clock.getMonthEnd(dateArray[1])
        midnight = [dateArray[0], dateArray[1], dateArray[2] + 1, 0, 0, 0]
        if midnight[2] > datef:
            midnight[1] = midnight[1] + 1
            if midnight[1] > 12:
                midnight[1] = 1
                midnight[0] = midnight[0] + 1
        return midnight
        
    def dateArrayToUTC(dateArray):
        out = ((dateArray[0]) * 365 * 24 * 60 * 60)
        i = 1
        while i < dateArray[1]:
            out = out + (clock.getMonthEnd(i) * 24 * 60 * 60)
            i = i + 1
        out = out + (dateArray[2] * 24 * 60 * 60) + (dateArray[3] * 60 * 60) + (dateArray[4] * 60) + dateArray[5]
        return out
    
def dummy(*args):
    if args[0] == args[0]:
        pass
    return 0
    
def runFile(path):
    code = IO.getFile(path)
    out = exec(code)
    return out

def libHelp(self):
    help(self)

print("type help(pytools) or pytools.libHelp(pytools) to get more info about the library!")