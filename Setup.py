from setuptools import setup

APP = ["main"]
OPTION = {
    'argv_emulation': True,
}

setup(
    app=APP
    options={'py2app': OPTION},
    set_uprequires=['py2app']
)