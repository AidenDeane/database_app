import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    'database_array.py',
    'employee_service.py',
    'financial_service.py',
    'GUI_service.py',
    'pos_service.py',
    '--windowed'
])