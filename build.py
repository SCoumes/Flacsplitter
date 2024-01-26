import PyInstaller.__main__
import shutil
import os
import glob
import platform

# Build on windows
if platform.system() == "Windows":
    windows_build_dir = os.path.join("dist","FlackTrackSplitter_v1.0_windows")
    shutil.rmtree(windows_build_dir)
    # Run PyInstaller to create the executable
    PyInstaller.__main__.run([
        "main.py",
        "--onefile",
        "--noconsole",
        "--name",
        "FlacTrackSplitter",
        "--icon=icon.ico"
    ])
    # Create a zip file containing the executable and other relevant files for the windows build
    os.makedirs(windows_build_dir)
    shutil.copy(os.path.join("dist","FlacTrackSplitter.exe"), windows_build_dir)
    shutil.copy("icon.png", windows_build_dir)
    shutil.copy(os.path.join("Licenses","Release_license_text.txt"), os.path.join(windows_build_dir,"LICENSE.txt"))
    shutil.copy("README.md", windows_build_dir)
    shutil.make_archive(windows_build_dir, 'zip', windows_build_dir)