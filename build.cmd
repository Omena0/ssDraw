echo ### Building Main ###
echo ## PyPath-1 ##
pyinstaller --specpath "build/spec" --distpath "dist" --workpath "build/build" --noconfirm --onefile --windowed --add-data "C:\Program Files\Python312\lib\Site-packages\customtkinter;customtkinter"  "main.pyw"
echo ## PyPath-2 ##
pyinstaller --specpath "build/spec" --distpath "dist" --workpath "build/build" --noconfirm --onefile --windowed --add-data "%appdata%\Python\Python312\site-packages\customtkinter;customtkinter"  "main.pyw"
echo ## PyPath-3 ##
pyinstaller --specpath "build/spec" --distpath "dist" --workpath "build/build" --noconfirm --onefile --windowed --add-data "%localappdata%\Programs\Python\Python311\Lib\site-packages\customtkinter;customtkinter"  "main.pyw"

