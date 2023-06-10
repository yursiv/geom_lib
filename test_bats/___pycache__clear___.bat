@echo off
setlocal enabledelayedexpansion

rem Удаление всех папок "__pycache__" и их содержимого в дереве каталогов

rem Устанавливаем начальный каталог для обхода дерева каталогов
set "ROOT_DIR=%CD%"

rem Вызываем рекурсивную функцию для удаления "__pycache__"
call :DeletePycache "%ROOT_DIR%"

rem Ожидаем нажатия клавиши для выхода
pause
exit

rem Рекурсивная функция для удаления "__pycache__"
:DeletePycache
set "DIR=%~1"

rem Перебираем все файлы и подкаталоги в текущем каталоге
for /d /r "%DIR%" %%f in (*) do (
    rem Проверяем, является ли текущий элемент директорией "__pycache__"
    if "%%~nxf"=="__pycache__" (
        rem Печатаем путь удаляемой папки "__pycache__"
        echo Removing directory: "%%~dpf"
        rem Удаляем текущую папку "__pycache__" вместе с содержимым
        rmdir /s /q "%%~dpf" >nul
    )
)

exit /b

