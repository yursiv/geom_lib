import os
import string

letters = list("QWERTYASDFGHZXCVB")
skeys = ["DBL"] + letters + []

numpad = (
    "NP_+",
    "NP_-",
    "NP_*",
    "NP_/",

    "NP_1",
    "NP_2",
    "NP_3",
    "NP_4",
    "NP_5",
    "NP_6",
    "NP_7",
    "NP_8",
    "NP_9",
    "NP_0",
)

mods = (
    (True, False, False),
    (False, True, False),
    (False, False, True),

    (True, False, True),
    (False, True, True),
    (True, True, False),

    (True, True, True),
)

digits = list(string.digits)

mouse_keys = (
    "LMB",
    "RMB",
    "MMB",

    "MWUp",
    "MWDown",

    "M ->",
    "M <-",

)

space_ids = [7, 10, 14, 15]

ahk_header = """
;ahk_class StudioProxy
SetTitleMatchMode, 2 ; This let's any window that partially matches the given name get activated

ahk_class=Afx:000007FECDCF0000:8:0000000000010003:0000000000000000:0000000042590F8B
wtitle=Rhinoceros 7 
subsexe = Rhino.exe
#IfWinActive, ahk_exe Rhino.exe

/*
ctrl  ^
shift +
alt ! 
win # 
double letter key ~k1 & k2
Esc
MouseClick, right, , 
MouseMove, 35, 35 , 0, R
MouseClick, left, , 
MouseMove, 40, 120 , 10, R
MouseClick, left, , 

LButton Left mouse button 
RButton Right mouse button 
MButton Middle or wheel mouse button 
XButton2 5th mouse button. Typically performs the same function as Browser_Forward. 
XButton1 4th mouse button. Typically performs the same function as Browser_Back. 
WheelDown Turn the wheel downward (toward you). 
WheelUp Turn the wheel upward (away from you). 
WheelLeft
WheelRight 

----------------Toggler
Isolate selected
IsolateSelected := False
!x::
if IsolateSelected{
    Send, +h
    IsolateSelected := False
    }
else {
    Send, !+h
    IsolateSelected := True
}
return


----------------Double Click
; DBL S
~s::
if (A_PriorHotkey <> "~s" or A_TimeSincePriorHotkey > 400)
{
    ; Too much time between presses, so this isn't a double-press.
    KeyWait, s
    return
}
Send, ^!+q
return

*/  
"""

ahk_dict = {
    "ctrl": "^",
    "alt": "!",
    "shift": "+",
    "win": "#",

    "LMB": "LButton",
    "MMB": "MButton",

    "MWUp": "WheelUp",
    "MWDown": "WheelDown",
    "RMB": "RButton",
    "M ->": "XButton2",
    "M <-": "XButton1",

    "NP_+": "NumpadAdd",
    "NP_-": "NumpadSub",
    "NP_*": "NumpadMult",
    "NP_/": "NumpadDiv",

    "NP_": "Numpad",
}


class HKeyComb:
    def __init__(self, pkey, skey=None, mods=(False, False, False)):
        self.pkey = pkey
        self.skey = skey
        self.mods = mods
        self.mods_str = [
            "ctrl" if self.mods[0] else "",
            "alt" if self.mods[1] else "",
            "shift" if self.mods[2] else "",
        ]

    def __str__(self):
        # ctrl = "Ctrl" if self.mods[0] else ""
        # alt = "Alt" if self.mods[1] else ""
        # shift = "Shift" if self.mods[2] else ""

        ctrl, alt, shift = (m.capitalize() for m in self.mods_str)

        if self.skey:
            mod = self.skey
        else:
            mod = "{0}{1}{2}".format(ctrl, alt, shift)

        return f"{self.pkey} {mod}"

    @property
    def ahkey_lines(self):
        """
        #Double Key
        ~Q & W::
        Send, {BackSpace}SomeText{Enter}
        return

        #Mod Key
        ^!+Q::
        Send, {BackSpace}SomeText{Enter}
        return

        :return:
        """

        nice_name = str(self)
        pkey = self.pkey.lower()
        skey = self.skey.lower() if self.skey else None

        lines = []
        lines.append(f"; {nice_name}\n")

        if any(self.mods):
            ahk_mods = "".join([ahk_dict.get(m, "") for m in self.mods_str])
            lines.append(f"{ahk_mods}{pkey}::\n")
            lines.append("Send, SomeText{Enter}\n")
            lines.append("return\n")

        elif skey == "dbl":
            lines.append(f"if (A_PriorHotkey <> \"~{pkey}\" or A_TimeSincePriorHotkey > 400)\n")
            lines.append("{\n")
            lines.append(f"\tKeyWait, {pkey}\n")
            lines.append("\treturn\n")
            lines.append("}\n")
            lines.append(f"Send, ^!+{pkey}")
            # lines = """
            #             if (A_PriorHotkey <> "~s" or A_TimeSincePriorHotkey > 400)
            # {
            #     ; Too much time between presses, so this isn't a double-press.
            #     KeyWait, s
            #     return
            # }
            # Send, ^!+q
            # return
            # """

        elif skey:
            ahk_skey = ahk_dict.get(self.skey) or skey
            lines.append(f"~{pkey} & {ahk_skey}::\n")
            lines.append("Send, {BackSpace}SomeText{Enter}\n")
            lines.append("return\n")

        lines.append("\n")

        return lines

    @property
    def ctrl(self):
        return self.mods[0]

    @property
    def alt(self):
        return self.mods[1]

    @property
    def shift(self):
        return self.mods[2]


def make_pkey_combs(pkey="Q"):
    # combs = [HKeyComb(pkey)]
    combs = []

    for mod in mods:
        combs.append(HKeyComb(pkey, mods=mod))

    for mkey in mouse_keys:
        combs.append(HKeyComb(pkey, mkey))

    for skey in skeys:
        if skey != pkey:
            combs.append(HKeyComb(pkey, skey))

    return combs


def make_ahk_lines(separator=";"):  # ";" for AutoHotkey
    lines = []
    for l in ahk_header.split("\n"):
        lines.append(l)
        lines.append("\n")
    lines.append("\n\n")

    for pkey in letters:
        lines.append("\n\n" + separator + " " + "-" * 50 + f" {pkey} " + "-" * 50 + "\n")

        combs = make_pkey_combs(pkey)

        comb_lines = []
        for ci, comb in enumerate(combs):
            if comb.mods == (False, False, True):
                continue

            if ci in space_ids:
                comb_lines.append("\n")

            # comb_lines.append(str(comb) + "\n")
            comb_lines.extend(comb.ahkey_lines)

        lines.extend(comb_lines)

    return lines


def make_exel_lines(separator="|"):
    lines = []

    for pkey in letters:
        combs = make_pkey_combs(pkey)

        comb_lines = []
        for ci, comb in enumerate(combs):
            if comb.mods == (False, False, True):
                continue

            if ci in space_ids:
                comb_lines.append("\n")

            s1, _, s2 = str(comb).partition(" ")

            str_comb = s1 + separator + s2

            comb_lines.append(str_comb + "\n")

        lines.extend(comb_lines)
        lines.append("\n")

    return lines


def writefile(fpath, lines):
    with open(fpath, "w") as f:
        f.writelines(lines)


def test_key_comb():
    comb1 = HKeyComb("Q", )
    comb2 = HKeyComb("Q", mods=(True, True, False))
    comb3 = HKeyComb("Q", "MWUp")
    print(comb1)
    print(comb2)
    print(comb3)

    print("------------")
    q_combs = make_pkey_combs("Q")

    for ci, comb in enumerate(q_combs):
        if ci in space_ids:
            print("")

        print(comb)


if __name__ == '__main__':
    # test_key_comb()

    # fpath = r"D:\Autohotkey\___rhino_template.ahk"
    fpath = r"D:\Python\geom\texts_generation\ah_template.ahk"
    lines = make_ahk_lines()
    writefile(fpath, lines)

    fpath2 = r"D:\Python\geom\texts_generation\_hotkeys_exel_template.txt"
    lines2 = make_exel_lines()
    writefile(fpath2, lines2)
