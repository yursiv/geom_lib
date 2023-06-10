@echo off

setlocal enabledelayedexpansion

set "PYPATH=C:\Python\Python310\python.exe"
set "ARGS=build_ext --inplace"

rem Находим все файлы "setup*.py" в текущем каталоге
for %%f in (setup*.py) do (
    rem Выполняем команду %SOMEPATH% для каждого найденного файла
    echo "%PYPATH%" %%~nxf %ARGS%
    "%PYPATH%" %%~nxf %ARGS%
)

::for %%f in (_test_*.py) do (
::    echo %PYPATH% %%~nxf
::    %PYPATH% "%%~nxf"
::)


pause
::exit

