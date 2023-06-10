
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





; -------------------------------------------------- Q --------------------------------------------------
; Q Ctrl
^q::
Send, SomeText{Enter}
return

; Q Alt
!q::
Send, SomeText{Enter}
return

; Q CtrlShift
^+q::
Send, SomeText{Enter}
return

; Q AltShift
!+q::
Send, SomeText{Enter}
return

; Q CtrlAlt
^!q::
Send, SomeText{Enter}
return

; Q CtrlAltShift
^!+q::
Send, SomeText{Enter}
return


; Q LMB
~q & LButton::
Send, {BackSpace}SomeText{Enter}
return

; Q RMB
~q & RButton::
Send, {BackSpace}SomeText{Enter}
return

; Q MMB
~q & MButton::
Send, {BackSpace}SomeText{Enter}
return


; Q MWUp
~q & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; Q MWDown
~q & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; Q M ->
~q & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; Q M <-
~q & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; Q DBL
if (A_PriorHotkey <> "~q" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, q
	return
}
Send, ^!+q

; Q W
~q & w::
Send, {BackSpace}SomeText{Enter}
return

; Q E
~q & e::
Send, {BackSpace}SomeText{Enter}
return

; Q R
~q & r::
Send, {BackSpace}SomeText{Enter}
return

; Q T
~q & t::
Send, {BackSpace}SomeText{Enter}
return

; Q Y
~q & y::
Send, {BackSpace}SomeText{Enter}
return

; Q A
~q & a::
Send, {BackSpace}SomeText{Enter}
return

; Q S
~q & s::
Send, {BackSpace}SomeText{Enter}
return

; Q D
~q & d::
Send, {BackSpace}SomeText{Enter}
return

; Q F
~q & f::
Send, {BackSpace}SomeText{Enter}
return

; Q G
~q & g::
Send, {BackSpace}SomeText{Enter}
return

; Q H
~q & h::
Send, {BackSpace}SomeText{Enter}
return

; Q Z
~q & z::
Send, {BackSpace}SomeText{Enter}
return

; Q X
~q & x::
Send, {BackSpace}SomeText{Enter}
return

; Q C
~q & c::
Send, {BackSpace}SomeText{Enter}
return

; Q V
~q & v::
Send, {BackSpace}SomeText{Enter}
return

; Q B
~q & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- W --------------------------------------------------
; W Ctrl
^w::
Send, SomeText{Enter}
return

; W Alt
!w::
Send, SomeText{Enter}
return

; W CtrlShift
^+w::
Send, SomeText{Enter}
return

; W AltShift
!+w::
Send, SomeText{Enter}
return

; W CtrlAlt
^!w::
Send, SomeText{Enter}
return

; W CtrlAltShift
^!+w::
Send, SomeText{Enter}
return


; W LMB
~w & LButton::
Send, {BackSpace}SomeText{Enter}
return

; W RMB
~w & RButton::
Send, {BackSpace}SomeText{Enter}
return

; W MMB
~w & MButton::
Send, {BackSpace}SomeText{Enter}
return


; W MWUp
~w & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; W MWDown
~w & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; W M ->
~w & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; W M <-
~w & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; W DBL
if (A_PriorHotkey <> "~w" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, w
	return
}
Send, ^!+w

; W Q
~w & q::
Send, {BackSpace}SomeText{Enter}
return

; W E
~w & e::
Send, {BackSpace}SomeText{Enter}
return

; W R
~w & r::
Send, {BackSpace}SomeText{Enter}
return

; W T
~w & t::
Send, {BackSpace}SomeText{Enter}
return

; W Y
~w & y::
Send, {BackSpace}SomeText{Enter}
return

; W A
~w & a::
Send, {BackSpace}SomeText{Enter}
return

; W S
~w & s::
Send, {BackSpace}SomeText{Enter}
return

; W D
~w & d::
Send, {BackSpace}SomeText{Enter}
return

; W F
~w & f::
Send, {BackSpace}SomeText{Enter}
return

; W G
~w & g::
Send, {BackSpace}SomeText{Enter}
return

; W H
~w & h::
Send, {BackSpace}SomeText{Enter}
return

; W Z
~w & z::
Send, {BackSpace}SomeText{Enter}
return

; W X
~w & x::
Send, {BackSpace}SomeText{Enter}
return

; W C
~w & c::
Send, {BackSpace}SomeText{Enter}
return

; W V
~w & v::
Send, {BackSpace}SomeText{Enter}
return

; W B
~w & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- E --------------------------------------------------
; E Ctrl
^e::
Send, SomeText{Enter}
return

; E Alt
!e::
Send, SomeText{Enter}
return

; E CtrlShift
^+e::
Send, SomeText{Enter}
return

; E AltShift
!+e::
Send, SomeText{Enter}
return

; E CtrlAlt
^!e::
Send, SomeText{Enter}
return

; E CtrlAltShift
^!+e::
Send, SomeText{Enter}
return


; E LMB
~e & LButton::
Send, {BackSpace}SomeText{Enter}
return

; E RMB
~e & RButton::
Send, {BackSpace}SomeText{Enter}
return

; E MMB
~e & MButton::
Send, {BackSpace}SomeText{Enter}
return


; E MWUp
~e & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; E MWDown
~e & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; E M ->
~e & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; E M <-
~e & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; E DBL
if (A_PriorHotkey <> "~e" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, e
	return
}
Send, ^!+e

; E Q
~e & q::
Send, {BackSpace}SomeText{Enter}
return

; E W
~e & w::
Send, {BackSpace}SomeText{Enter}
return

; E R
~e & r::
Send, {BackSpace}SomeText{Enter}
return

; E T
~e & t::
Send, {BackSpace}SomeText{Enter}
return

; E Y
~e & y::
Send, {BackSpace}SomeText{Enter}
return

; E A
~e & a::
Send, {BackSpace}SomeText{Enter}
return

; E S
~e & s::
Send, {BackSpace}SomeText{Enter}
return

; E D
~e & d::
Send, {BackSpace}SomeText{Enter}
return

; E F
~e & f::
Send, {BackSpace}SomeText{Enter}
return

; E G
~e & g::
Send, {BackSpace}SomeText{Enter}
return

; E H
~e & h::
Send, {BackSpace}SomeText{Enter}
return

; E Z
~e & z::
Send, {BackSpace}SomeText{Enter}
return

; E X
~e & x::
Send, {BackSpace}SomeText{Enter}
return

; E C
~e & c::
Send, {BackSpace}SomeText{Enter}
return

; E V
~e & v::
Send, {BackSpace}SomeText{Enter}
return

; E B
~e & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- R --------------------------------------------------
; R Ctrl
^r::
Send, SomeText{Enter}
return

; R Alt
!r::
Send, SomeText{Enter}
return

; R CtrlShift
^+r::
Send, SomeText{Enter}
return

; R AltShift
!+r::
Send, SomeText{Enter}
return

; R CtrlAlt
^!r::
Send, SomeText{Enter}
return

; R CtrlAltShift
^!+r::
Send, SomeText{Enter}
return


; R LMB
~r & LButton::
Send, {BackSpace}SomeText{Enter}
return

; R RMB
~r & RButton::
Send, {BackSpace}SomeText{Enter}
return

; R MMB
~r & MButton::
Send, {BackSpace}SomeText{Enter}
return


; R MWUp
~r & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; R MWDown
~r & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; R M ->
~r & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; R M <-
~r & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; R DBL
if (A_PriorHotkey <> "~r" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, r
	return
}
Send, ^!+r

; R Q
~r & q::
Send, {BackSpace}SomeText{Enter}
return

; R W
~r & w::
Send, {BackSpace}SomeText{Enter}
return

; R E
~r & e::
Send, {BackSpace}SomeText{Enter}
return

; R T
~r & t::
Send, {BackSpace}SomeText{Enter}
return

; R Y
~r & y::
Send, {BackSpace}SomeText{Enter}
return

; R A
~r & a::
Send, {BackSpace}SomeText{Enter}
return

; R S
~r & s::
Send, {BackSpace}SomeText{Enter}
return

; R D
~r & d::
Send, {BackSpace}SomeText{Enter}
return

; R F
~r & f::
Send, {BackSpace}SomeText{Enter}
return

; R G
~r & g::
Send, {BackSpace}SomeText{Enter}
return

; R H
~r & h::
Send, {BackSpace}SomeText{Enter}
return

; R Z
~r & z::
Send, {BackSpace}SomeText{Enter}
return

; R X
~r & x::
Send, {BackSpace}SomeText{Enter}
return

; R C
~r & c::
Send, {BackSpace}SomeText{Enter}
return

; R V
~r & v::
Send, {BackSpace}SomeText{Enter}
return

; R B
~r & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- T --------------------------------------------------
; T Ctrl
^t::
Send, SomeText{Enter}
return

; T Alt
!t::
Send, SomeText{Enter}
return

; T CtrlShift
^+t::
Send, SomeText{Enter}
return

; T AltShift
!+t::
Send, SomeText{Enter}
return

; T CtrlAlt
^!t::
Send, SomeText{Enter}
return

; T CtrlAltShift
^!+t::
Send, SomeText{Enter}
return


; T LMB
~t & LButton::
Send, {BackSpace}SomeText{Enter}
return

; T RMB
~t & RButton::
Send, {BackSpace}SomeText{Enter}
return

; T MMB
~t & MButton::
Send, {BackSpace}SomeText{Enter}
return


; T MWUp
~t & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; T MWDown
~t & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; T M ->
~t & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; T M <-
~t & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; T DBL
if (A_PriorHotkey <> "~t" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, t
	return
}
Send, ^!+t

; T Q
~t & q::
Send, {BackSpace}SomeText{Enter}
return

; T W
~t & w::
Send, {BackSpace}SomeText{Enter}
return

; T E
~t & e::
Send, {BackSpace}SomeText{Enter}
return

; T R
~t & r::
Send, {BackSpace}SomeText{Enter}
return

; T Y
~t & y::
Send, {BackSpace}SomeText{Enter}
return

; T A
~t & a::
Send, {BackSpace}SomeText{Enter}
return

; T S
~t & s::
Send, {BackSpace}SomeText{Enter}
return

; T D
~t & d::
Send, {BackSpace}SomeText{Enter}
return

; T F
~t & f::
Send, {BackSpace}SomeText{Enter}
return

; T G
~t & g::
Send, {BackSpace}SomeText{Enter}
return

; T H
~t & h::
Send, {BackSpace}SomeText{Enter}
return

; T Z
~t & z::
Send, {BackSpace}SomeText{Enter}
return

; T X
~t & x::
Send, {BackSpace}SomeText{Enter}
return

; T C
~t & c::
Send, {BackSpace}SomeText{Enter}
return

; T V
~t & v::
Send, {BackSpace}SomeText{Enter}
return

; T B
~t & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- Y --------------------------------------------------
; Y Ctrl
^y::
Send, SomeText{Enter}
return

; Y Alt
!y::
Send, SomeText{Enter}
return

; Y CtrlShift
^+y::
Send, SomeText{Enter}
return

; Y AltShift
!+y::
Send, SomeText{Enter}
return

; Y CtrlAlt
^!y::
Send, SomeText{Enter}
return

; Y CtrlAltShift
^!+y::
Send, SomeText{Enter}
return


; Y LMB
~y & LButton::
Send, {BackSpace}SomeText{Enter}
return

; Y RMB
~y & RButton::
Send, {BackSpace}SomeText{Enter}
return

; Y MMB
~y & MButton::
Send, {BackSpace}SomeText{Enter}
return


; Y MWUp
~y & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; Y MWDown
~y & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; Y M ->
~y & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; Y M <-
~y & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; Y DBL
if (A_PriorHotkey <> "~y" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, y
	return
}
Send, ^!+y

; Y Q
~y & q::
Send, {BackSpace}SomeText{Enter}
return

; Y W
~y & w::
Send, {BackSpace}SomeText{Enter}
return

; Y E
~y & e::
Send, {BackSpace}SomeText{Enter}
return

; Y R
~y & r::
Send, {BackSpace}SomeText{Enter}
return

; Y T
~y & t::
Send, {BackSpace}SomeText{Enter}
return

; Y A
~y & a::
Send, {BackSpace}SomeText{Enter}
return

; Y S
~y & s::
Send, {BackSpace}SomeText{Enter}
return

; Y D
~y & d::
Send, {BackSpace}SomeText{Enter}
return

; Y F
~y & f::
Send, {BackSpace}SomeText{Enter}
return

; Y G
~y & g::
Send, {BackSpace}SomeText{Enter}
return

; Y H
~y & h::
Send, {BackSpace}SomeText{Enter}
return

; Y Z
~y & z::
Send, {BackSpace}SomeText{Enter}
return

; Y X
~y & x::
Send, {BackSpace}SomeText{Enter}
return

; Y C
~y & c::
Send, {BackSpace}SomeText{Enter}
return

; Y V
~y & v::
Send, {BackSpace}SomeText{Enter}
return

; Y B
~y & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- A --------------------------------------------------
; A Ctrl
^a::
Send, SomeText{Enter}
return

; A Alt
!a::
Send, SomeText{Enter}
return

; A CtrlShift
^+a::
Send, SomeText{Enter}
return

; A AltShift
!+a::
Send, SomeText{Enter}
return

; A CtrlAlt
^!a::
Send, SomeText{Enter}
return

; A CtrlAltShift
^!+a::
Send, SomeText{Enter}
return


; A LMB
~a & LButton::
Send, {BackSpace}SomeText{Enter}
return

; A RMB
~a & RButton::
Send, {BackSpace}SomeText{Enter}
return

; A MMB
~a & MButton::
Send, {BackSpace}SomeText{Enter}
return


; A MWUp
~a & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; A MWDown
~a & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; A M ->
~a & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; A M <-
~a & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; A DBL
if (A_PriorHotkey <> "~a" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, a
	return
}
Send, ^!+a

; A Q
~a & q::
Send, {BackSpace}SomeText{Enter}
return

; A W
~a & w::
Send, {BackSpace}SomeText{Enter}
return

; A E
~a & e::
Send, {BackSpace}SomeText{Enter}
return

; A R
~a & r::
Send, {BackSpace}SomeText{Enter}
return

; A T
~a & t::
Send, {BackSpace}SomeText{Enter}
return

; A Y
~a & y::
Send, {BackSpace}SomeText{Enter}
return

; A S
~a & s::
Send, {BackSpace}SomeText{Enter}
return

; A D
~a & d::
Send, {BackSpace}SomeText{Enter}
return

; A F
~a & f::
Send, {BackSpace}SomeText{Enter}
return

; A G
~a & g::
Send, {BackSpace}SomeText{Enter}
return

; A H
~a & h::
Send, {BackSpace}SomeText{Enter}
return

; A Z
~a & z::
Send, {BackSpace}SomeText{Enter}
return

; A X
~a & x::
Send, {BackSpace}SomeText{Enter}
return

; A C
~a & c::
Send, {BackSpace}SomeText{Enter}
return

; A V
~a & v::
Send, {BackSpace}SomeText{Enter}
return

; A B
~a & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- S --------------------------------------------------
; S Ctrl
^s::
Send, SomeText{Enter}
return

; S Alt
!s::
Send, SomeText{Enter}
return

; S CtrlShift
^+s::
Send, SomeText{Enter}
return

; S AltShift
!+s::
Send, SomeText{Enter}
return

; S CtrlAlt
^!s::
Send, SomeText{Enter}
return

; S CtrlAltShift
^!+s::
Send, SomeText{Enter}
return


; S LMB
~s & LButton::
Send, {BackSpace}SomeText{Enter}
return

; S RMB
~s & RButton::
Send, {BackSpace}SomeText{Enter}
return

; S MMB
~s & MButton::
Send, {BackSpace}SomeText{Enter}
return


; S MWUp
~s & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; S MWDown
~s & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; S M ->
~s & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; S M <-
~s & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; S DBL
if (A_PriorHotkey <> "~s" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, s
	return
}
Send, ^!+s

; S Q
~s & q::
Send, {BackSpace}SomeText{Enter}
return

; S W
~s & w::
Send, {BackSpace}SomeText{Enter}
return

; S E
~s & e::
Send, {BackSpace}SomeText{Enter}
return

; S R
~s & r::
Send, {BackSpace}SomeText{Enter}
return

; S T
~s & t::
Send, {BackSpace}SomeText{Enter}
return

; S Y
~s & y::
Send, {BackSpace}SomeText{Enter}
return

; S A
~s & a::
Send, {BackSpace}SomeText{Enter}
return

; S D
~s & d::
Send, {BackSpace}SomeText{Enter}
return

; S F
~s & f::
Send, {BackSpace}SomeText{Enter}
return

; S G
~s & g::
Send, {BackSpace}SomeText{Enter}
return

; S H
~s & h::
Send, {BackSpace}SomeText{Enter}
return

; S Z
~s & z::
Send, {BackSpace}SomeText{Enter}
return

; S X
~s & x::
Send, {BackSpace}SomeText{Enter}
return

; S C
~s & c::
Send, {BackSpace}SomeText{Enter}
return

; S V
~s & v::
Send, {BackSpace}SomeText{Enter}
return

; S B
~s & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- D --------------------------------------------------
; D Ctrl
^d::
Send, SomeText{Enter}
return

; D Alt
!d::
Send, SomeText{Enter}
return

; D CtrlShift
^+d::
Send, SomeText{Enter}
return

; D AltShift
!+d::
Send, SomeText{Enter}
return

; D CtrlAlt
^!d::
Send, SomeText{Enter}
return

; D CtrlAltShift
^!+d::
Send, SomeText{Enter}
return


; D LMB
~d & LButton::
Send, {BackSpace}SomeText{Enter}
return

; D RMB
~d & RButton::
Send, {BackSpace}SomeText{Enter}
return

; D MMB
~d & MButton::
Send, {BackSpace}SomeText{Enter}
return


; D MWUp
~d & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; D MWDown
~d & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; D M ->
~d & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; D M <-
~d & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; D DBL
if (A_PriorHotkey <> "~d" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, d
	return
}
Send, ^!+d

; D Q
~d & q::
Send, {BackSpace}SomeText{Enter}
return

; D W
~d & w::
Send, {BackSpace}SomeText{Enter}
return

; D E
~d & e::
Send, {BackSpace}SomeText{Enter}
return

; D R
~d & r::
Send, {BackSpace}SomeText{Enter}
return

; D T
~d & t::
Send, {BackSpace}SomeText{Enter}
return

; D Y
~d & y::
Send, {BackSpace}SomeText{Enter}
return

; D A
~d & a::
Send, {BackSpace}SomeText{Enter}
return

; D S
~d & s::
Send, {BackSpace}SomeText{Enter}
return

; D F
~d & f::
Send, {BackSpace}SomeText{Enter}
return

; D G
~d & g::
Send, {BackSpace}SomeText{Enter}
return

; D H
~d & h::
Send, {BackSpace}SomeText{Enter}
return

; D Z
~d & z::
Send, {BackSpace}SomeText{Enter}
return

; D X
~d & x::
Send, {BackSpace}SomeText{Enter}
return

; D C
~d & c::
Send, {BackSpace}SomeText{Enter}
return

; D V
~d & v::
Send, {BackSpace}SomeText{Enter}
return

; D B
~d & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- F --------------------------------------------------
; F Ctrl
^f::
Send, SomeText{Enter}
return

; F Alt
!f::
Send, SomeText{Enter}
return

; F CtrlShift
^+f::
Send, SomeText{Enter}
return

; F AltShift
!+f::
Send, SomeText{Enter}
return

; F CtrlAlt
^!f::
Send, SomeText{Enter}
return

; F CtrlAltShift
^!+f::
Send, SomeText{Enter}
return


; F LMB
~f & LButton::
Send, {BackSpace}SomeText{Enter}
return

; F RMB
~f & RButton::
Send, {BackSpace}SomeText{Enter}
return

; F MMB
~f & MButton::
Send, {BackSpace}SomeText{Enter}
return


; F MWUp
~f & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; F MWDown
~f & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; F M ->
~f & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; F M <-
~f & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; F DBL
if (A_PriorHotkey <> "~f" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, f
	return
}
Send, ^!+f

; F Q
~f & q::
Send, {BackSpace}SomeText{Enter}
return

; F W
~f & w::
Send, {BackSpace}SomeText{Enter}
return

; F E
~f & e::
Send, {BackSpace}SomeText{Enter}
return

; F R
~f & r::
Send, {BackSpace}SomeText{Enter}
return

; F T
~f & t::
Send, {BackSpace}SomeText{Enter}
return

; F Y
~f & y::
Send, {BackSpace}SomeText{Enter}
return

; F A
~f & a::
Send, {BackSpace}SomeText{Enter}
return

; F S
~f & s::
Send, {BackSpace}SomeText{Enter}
return

; F D
~f & d::
Send, {BackSpace}SomeText{Enter}
return

; F G
~f & g::
Send, {BackSpace}SomeText{Enter}
return

; F H
~f & h::
Send, {BackSpace}SomeText{Enter}
return

; F Z
~f & z::
Send, {BackSpace}SomeText{Enter}
return

; F X
~f & x::
Send, {BackSpace}SomeText{Enter}
return

; F C
~f & c::
Send, {BackSpace}SomeText{Enter}
return

; F V
~f & v::
Send, {BackSpace}SomeText{Enter}
return

; F B
~f & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- G --------------------------------------------------
; G Ctrl
^g::
Send, SomeText{Enter}
return

; G Alt
!g::
Send, SomeText{Enter}
return

; G CtrlShift
^+g::
Send, SomeText{Enter}
return

; G AltShift
!+g::
Send, SomeText{Enter}
return

; G CtrlAlt
^!g::
Send, SomeText{Enter}
return

; G CtrlAltShift
^!+g::
Send, SomeText{Enter}
return


; G LMB
~g & LButton::
Send, {BackSpace}SomeText{Enter}
return

; G RMB
~g & RButton::
Send, {BackSpace}SomeText{Enter}
return

; G MMB
~g & MButton::
Send, {BackSpace}SomeText{Enter}
return


; G MWUp
~g & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; G MWDown
~g & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; G M ->
~g & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; G M <-
~g & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; G DBL
if (A_PriorHotkey <> "~g" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, g
	return
}
Send, ^!+g

; G Q
~g & q::
Send, {BackSpace}SomeText{Enter}
return

; G W
~g & w::
Send, {BackSpace}SomeText{Enter}
return

; G E
~g & e::
Send, {BackSpace}SomeText{Enter}
return

; G R
~g & r::
Send, {BackSpace}SomeText{Enter}
return

; G T
~g & t::
Send, {BackSpace}SomeText{Enter}
return

; G Y
~g & y::
Send, {BackSpace}SomeText{Enter}
return

; G A
~g & a::
Send, {BackSpace}SomeText{Enter}
return

; G S
~g & s::
Send, {BackSpace}SomeText{Enter}
return

; G D
~g & d::
Send, {BackSpace}SomeText{Enter}
return

; G F
~g & f::
Send, {BackSpace}SomeText{Enter}
return

; G H
~g & h::
Send, {BackSpace}SomeText{Enter}
return

; G Z
~g & z::
Send, {BackSpace}SomeText{Enter}
return

; G X
~g & x::
Send, {BackSpace}SomeText{Enter}
return

; G C
~g & c::
Send, {BackSpace}SomeText{Enter}
return

; G V
~g & v::
Send, {BackSpace}SomeText{Enter}
return

; G B
~g & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- H --------------------------------------------------
; H Ctrl
^h::
Send, SomeText{Enter}
return

; H Alt
!h::
Send, SomeText{Enter}
return

; H CtrlShift
^+h::
Send, SomeText{Enter}
return

; H AltShift
!+h::
Send, SomeText{Enter}
return

; H CtrlAlt
^!h::
Send, SomeText{Enter}
return

; H CtrlAltShift
^!+h::
Send, SomeText{Enter}
return


; H LMB
~h & LButton::
Send, {BackSpace}SomeText{Enter}
return

; H RMB
~h & RButton::
Send, {BackSpace}SomeText{Enter}
return

; H MMB
~h & MButton::
Send, {BackSpace}SomeText{Enter}
return


; H MWUp
~h & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; H MWDown
~h & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; H M ->
~h & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; H M <-
~h & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; H DBL
if (A_PriorHotkey <> "~h" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, h
	return
}
Send, ^!+h

; H Q
~h & q::
Send, {BackSpace}SomeText{Enter}
return

; H W
~h & w::
Send, {BackSpace}SomeText{Enter}
return

; H E
~h & e::
Send, {BackSpace}SomeText{Enter}
return

; H R
~h & r::
Send, {BackSpace}SomeText{Enter}
return

; H T
~h & t::
Send, {BackSpace}SomeText{Enter}
return

; H Y
~h & y::
Send, {BackSpace}SomeText{Enter}
return

; H A
~h & a::
Send, {BackSpace}SomeText{Enter}
return

; H S
~h & s::
Send, {BackSpace}SomeText{Enter}
return

; H D
~h & d::
Send, {BackSpace}SomeText{Enter}
return

; H F
~h & f::
Send, {BackSpace}SomeText{Enter}
return

; H G
~h & g::
Send, {BackSpace}SomeText{Enter}
return

; H Z
~h & z::
Send, {BackSpace}SomeText{Enter}
return

; H X
~h & x::
Send, {BackSpace}SomeText{Enter}
return

; H C
~h & c::
Send, {BackSpace}SomeText{Enter}
return

; H V
~h & v::
Send, {BackSpace}SomeText{Enter}
return

; H B
~h & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- Z --------------------------------------------------
; Z Ctrl
^z::
Send, SomeText{Enter}
return

; Z Alt
!z::
Send, SomeText{Enter}
return

; Z CtrlShift
^+z::
Send, SomeText{Enter}
return

; Z AltShift
!+z::
Send, SomeText{Enter}
return

; Z CtrlAlt
^!z::
Send, SomeText{Enter}
return

; Z CtrlAltShift
^!+z::
Send, SomeText{Enter}
return


; Z LMB
~z & LButton::
Send, {BackSpace}SomeText{Enter}
return

; Z RMB
~z & RButton::
Send, {BackSpace}SomeText{Enter}
return

; Z MMB
~z & MButton::
Send, {BackSpace}SomeText{Enter}
return


; Z MWUp
~z & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; Z MWDown
~z & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; Z M ->
~z & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; Z M <-
~z & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; Z DBL
if (A_PriorHotkey <> "~z" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, z
	return
}
Send, ^!+z

; Z Q
~z & q::
Send, {BackSpace}SomeText{Enter}
return

; Z W
~z & w::
Send, {BackSpace}SomeText{Enter}
return

; Z E
~z & e::
Send, {BackSpace}SomeText{Enter}
return

; Z R
~z & r::
Send, {BackSpace}SomeText{Enter}
return

; Z T
~z & t::
Send, {BackSpace}SomeText{Enter}
return

; Z Y
~z & y::
Send, {BackSpace}SomeText{Enter}
return

; Z A
~z & a::
Send, {BackSpace}SomeText{Enter}
return

; Z S
~z & s::
Send, {BackSpace}SomeText{Enter}
return

; Z D
~z & d::
Send, {BackSpace}SomeText{Enter}
return

; Z F
~z & f::
Send, {BackSpace}SomeText{Enter}
return

; Z G
~z & g::
Send, {BackSpace}SomeText{Enter}
return

; Z H
~z & h::
Send, {BackSpace}SomeText{Enter}
return

; Z X
~z & x::
Send, {BackSpace}SomeText{Enter}
return

; Z C
~z & c::
Send, {BackSpace}SomeText{Enter}
return

; Z V
~z & v::
Send, {BackSpace}SomeText{Enter}
return

; Z B
~z & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- X --------------------------------------------------
; X Ctrl
^x::
Send, SomeText{Enter}
return

; X Alt
!x::
Send, SomeText{Enter}
return

; X CtrlShift
^+x::
Send, SomeText{Enter}
return

; X AltShift
!+x::
Send, SomeText{Enter}
return

; X CtrlAlt
^!x::
Send, SomeText{Enter}
return

; X CtrlAltShift
^!+x::
Send, SomeText{Enter}
return


; X LMB
~x & LButton::
Send, {BackSpace}SomeText{Enter}
return

; X RMB
~x & RButton::
Send, {BackSpace}SomeText{Enter}
return

; X MMB
~x & MButton::
Send, {BackSpace}SomeText{Enter}
return


; X MWUp
~x & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; X MWDown
~x & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; X M ->
~x & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; X M <-
~x & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; X DBL
if (A_PriorHotkey <> "~x" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, x
	return
}
Send, ^!+x

; X Q
~x & q::
Send, {BackSpace}SomeText{Enter}
return

; X W
~x & w::
Send, {BackSpace}SomeText{Enter}
return

; X E
~x & e::
Send, {BackSpace}SomeText{Enter}
return

; X R
~x & r::
Send, {BackSpace}SomeText{Enter}
return

; X T
~x & t::
Send, {BackSpace}SomeText{Enter}
return

; X Y
~x & y::
Send, {BackSpace}SomeText{Enter}
return

; X A
~x & a::
Send, {BackSpace}SomeText{Enter}
return

; X S
~x & s::
Send, {BackSpace}SomeText{Enter}
return

; X D
~x & d::
Send, {BackSpace}SomeText{Enter}
return

; X F
~x & f::
Send, {BackSpace}SomeText{Enter}
return

; X G
~x & g::
Send, {BackSpace}SomeText{Enter}
return

; X H
~x & h::
Send, {BackSpace}SomeText{Enter}
return

; X Z
~x & z::
Send, {BackSpace}SomeText{Enter}
return

; X C
~x & c::
Send, {BackSpace}SomeText{Enter}
return

; X V
~x & v::
Send, {BackSpace}SomeText{Enter}
return

; X B
~x & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- C --------------------------------------------------
; C Ctrl
^c::
Send, SomeText{Enter}
return

; C Alt
!c::
Send, SomeText{Enter}
return

; C CtrlShift
^+c::
Send, SomeText{Enter}
return

; C AltShift
!+c::
Send, SomeText{Enter}
return

; C CtrlAlt
^!c::
Send, SomeText{Enter}
return

; C CtrlAltShift
^!+c::
Send, SomeText{Enter}
return


; C LMB
~c & LButton::
Send, {BackSpace}SomeText{Enter}
return

; C RMB
~c & RButton::
Send, {BackSpace}SomeText{Enter}
return

; C MMB
~c & MButton::
Send, {BackSpace}SomeText{Enter}
return


; C MWUp
~c & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; C MWDown
~c & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; C M ->
~c & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; C M <-
~c & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; C DBL
if (A_PriorHotkey <> "~c" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, c
	return
}
Send, ^!+c

; C Q
~c & q::
Send, {BackSpace}SomeText{Enter}
return

; C W
~c & w::
Send, {BackSpace}SomeText{Enter}
return

; C E
~c & e::
Send, {BackSpace}SomeText{Enter}
return

; C R
~c & r::
Send, {BackSpace}SomeText{Enter}
return

; C T
~c & t::
Send, {BackSpace}SomeText{Enter}
return

; C Y
~c & y::
Send, {BackSpace}SomeText{Enter}
return

; C A
~c & a::
Send, {BackSpace}SomeText{Enter}
return

; C S
~c & s::
Send, {BackSpace}SomeText{Enter}
return

; C D
~c & d::
Send, {BackSpace}SomeText{Enter}
return

; C F
~c & f::
Send, {BackSpace}SomeText{Enter}
return

; C G
~c & g::
Send, {BackSpace}SomeText{Enter}
return

; C H
~c & h::
Send, {BackSpace}SomeText{Enter}
return

; C Z
~c & z::
Send, {BackSpace}SomeText{Enter}
return

; C X
~c & x::
Send, {BackSpace}SomeText{Enter}
return

; C V
~c & v::
Send, {BackSpace}SomeText{Enter}
return

; C B
~c & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- V --------------------------------------------------
; V Ctrl
^v::
Send, SomeText{Enter}
return

; V Alt
!v::
Send, SomeText{Enter}
return

; V CtrlShift
^+v::
Send, SomeText{Enter}
return

; V AltShift
!+v::
Send, SomeText{Enter}
return

; V CtrlAlt
^!v::
Send, SomeText{Enter}
return

; V CtrlAltShift
^!+v::
Send, SomeText{Enter}
return


; V LMB
~v & LButton::
Send, {BackSpace}SomeText{Enter}
return

; V RMB
~v & RButton::
Send, {BackSpace}SomeText{Enter}
return

; V MMB
~v & MButton::
Send, {BackSpace}SomeText{Enter}
return


; V MWUp
~v & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; V MWDown
~v & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; V M ->
~v & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; V M <-
~v & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; V DBL
if (A_PriorHotkey <> "~v" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, v
	return
}
Send, ^!+v

; V Q
~v & q::
Send, {BackSpace}SomeText{Enter}
return

; V W
~v & w::
Send, {BackSpace}SomeText{Enter}
return

; V E
~v & e::
Send, {BackSpace}SomeText{Enter}
return

; V R
~v & r::
Send, {BackSpace}SomeText{Enter}
return

; V T
~v & t::
Send, {BackSpace}SomeText{Enter}
return

; V Y
~v & y::
Send, {BackSpace}SomeText{Enter}
return

; V A
~v & a::
Send, {BackSpace}SomeText{Enter}
return

; V S
~v & s::
Send, {BackSpace}SomeText{Enter}
return

; V D
~v & d::
Send, {BackSpace}SomeText{Enter}
return

; V F
~v & f::
Send, {BackSpace}SomeText{Enter}
return

; V G
~v & g::
Send, {BackSpace}SomeText{Enter}
return

; V H
~v & h::
Send, {BackSpace}SomeText{Enter}
return

; V Z
~v & z::
Send, {BackSpace}SomeText{Enter}
return

; V X
~v & x::
Send, {BackSpace}SomeText{Enter}
return

; V C
~v & c::
Send, {BackSpace}SomeText{Enter}
return

; V B
~v & b::
Send, {BackSpace}SomeText{Enter}
return



; -------------------------------------------------- B --------------------------------------------------
; B Ctrl
^b::
Send, SomeText{Enter}
return

; B Alt
!b::
Send, SomeText{Enter}
return

; B CtrlShift
^+b::
Send, SomeText{Enter}
return

; B AltShift
!+b::
Send, SomeText{Enter}
return

; B CtrlAlt
^!b::
Send, SomeText{Enter}
return

; B CtrlAltShift
^!+b::
Send, SomeText{Enter}
return


; B LMB
~b & LButton::
Send, {BackSpace}SomeText{Enter}
return

; B RMB
~b & RButton::
Send, {BackSpace}SomeText{Enter}
return

; B MMB
~b & MButton::
Send, {BackSpace}SomeText{Enter}
return


; B MWUp
~b & WheelUp::
Send, {BackSpace}SomeText{Enter}
return

; B MWDown
~b & WheelDown::
Send, {BackSpace}SomeText{Enter}
return

; B M ->
~b & XButton2::
Send, {BackSpace}SomeText{Enter}
return

; B M <-
~b & XButton1::
Send, {BackSpace}SomeText{Enter}
return


; B DBL
if (A_PriorHotkey <> "~b" or A_TimeSincePriorHotkey > 400)
{
	KeyWait, b
	return
}
Send, ^!+b

; B Q
~b & q::
Send, {BackSpace}SomeText{Enter}
return

; B W
~b & w::
Send, {BackSpace}SomeText{Enter}
return

; B E
~b & e::
Send, {BackSpace}SomeText{Enter}
return

; B R
~b & r::
Send, {BackSpace}SomeText{Enter}
return

; B T
~b & t::
Send, {BackSpace}SomeText{Enter}
return

; B Y
~b & y::
Send, {BackSpace}SomeText{Enter}
return

; B A
~b & a::
Send, {BackSpace}SomeText{Enter}
return

; B S
~b & s::
Send, {BackSpace}SomeText{Enter}
return

; B D
~b & d::
Send, {BackSpace}SomeText{Enter}
return

; B F
~b & f::
Send, {BackSpace}SomeText{Enter}
return

; B G
~b & g::
Send, {BackSpace}SomeText{Enter}
return

; B H
~b & h::
Send, {BackSpace}SomeText{Enter}
return

; B Z
~b & z::
Send, {BackSpace}SomeText{Enter}
return

; B X
~b & x::
Send, {BackSpace}SomeText{Enter}
return

; B C
~b & c::
Send, {BackSpace}SomeText{Enter}
return

; B V
~b & v::
Send, {BackSpace}SomeText{Enter}
return

