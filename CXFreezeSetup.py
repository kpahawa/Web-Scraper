__author__ = 'kpahawa'
from cx_Freeze import  setup, Executable
import sys

includefiles = ['GUI.py', 'Scraper.py']
includes = ['csv']
excludes = []
packages = ['tkinter','urllib','bs4','urllib.request']

build_exe_options = {"packages": packages, "excludes": excludes, "includes": includes, "include_files":includefiles}

base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = 'AnimeWebScraperDemo',
    version = '1.0.0',
    description = 'This is a working prototype built for web scraping shows for AnimeFanpage.com',
    author = 'kP',
    options = {'build_exe': build_exe_options},
    executables = [Executable('GUI.py', base=base)]
)
