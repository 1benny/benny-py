import os

wingets = [
    "7zip.7zip", 
    "Git.Git", 
    "Microsoft.HEIFImageExtension_8wekyb3d8bbwe",
    "Microsoft.HEVCVideoExtensions_8wekyb3d8bbwe",
    "Notepad++.Notepad++",
    "JohnMacFarlane.Pandoc",
    "gerardog.gsudo",
    "SpotifyAB.SpotifyMusic_zpdnekdrzrea0",
    "Valve.Steam", 
    "NVIDIACorp.NVIDIAControlPanel_56jybvy8sckqj",
    "LLVM.LLVM",
    "JernejSimoncic.Wget",
    "Git.Git",
    "XP8K0J757HHRDW",
    "9P8Q2XRW9CV7",
    "XP9MKFMRRCVKX1",
    "Microsoft.DesktopAppInstaller_8wekyb3d8bbwe",
]

for i in wingets:
    os.system(f"winget install {i} --accept-source-agreements --accept-package-agreements")
