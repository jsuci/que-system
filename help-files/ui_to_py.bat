@echo off
set /p ui_file="Enter .ui file name: "
set /p py_file="Enter .py file name: "
pyuic5 %ui_file% -o %py_file%
echo "Done."
pause