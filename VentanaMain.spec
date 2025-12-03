# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['VentanaMain.py'],
    pathex=[],
    binaries=[],
    datas=[('salud-financiera.png', '.'), ('busqueda-de-lupa.png', '.'), ('base_datos_salud.xlsx', '.'), ('base_datos_salud_procesada.xlsx', '.'), ('paises_mayor_gasto_2010_2020.xlsx', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='VentanaMain',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
