<p align="center">
  <img src="src/Filee.App/Assets/Icons/filee.png" alt="Flip" width="128">
</p>

<h1 align="center">Flip</h1>

<p align="center">
  <b>Drag, drop, converted.</b> An offline file converter for Windows that you use by dragging.<br>
  Hold <kbd>Ctrl</kbd> while dragging files and drop them on a format in the donut that opens at your cursor.
</p>

<p align="center">
  <a href="https://github.com/SYQD1/flip/releases/latest"><b>Download</b></a> ·
  <a href="#install">Install</a> ·
  <a href="#build">Build</a> ·
  <a href="#credits">Credits</a>
</p>

<p dir="rtl" align="center">
  <b>Flip</b> محوّل ملفات يشتغل بدون إنترنت على ويندوز: اسحب الملف، اضغط <kbd>Ctrl</kbd>، وأفلته على الصيغة اللي تريدها.
</p>

---

## Features

- **Hundreds of conversions, all local**: images (JPG, PNG, WebP, HEIC, AVIF, TIFF, BMP, PSD...), PDF, Word, Excel,
  PowerPoint, HWP/HWPX, e-books, archives, fonts, CAD and 3D models, video and audio (with FFmpeg).
- **Donut toolbar**: hold a key while dragging files and a ring of formats opens at your cursor.
- **File tools**: compress, crop, annotate, redact, add a background, edit metadata, merge PDFs, OCR and more.
- **Presets and watch folders**: save conversions you repeat, and convert new files in a folder automatically.
- **Your files never leave your PC.** Nothing is uploaded.
- **Arabic interface**: Settings → General → Language → العربية (and 22 more languages).

## Install

1. Download `Flip-<version>-win-Setup.exe` from the [latest release](https://github.com/SYQD1/flip/releases/latest).
2. Run it. Windows SmartScreen may warn because the installer is not code-signed: choose **More info → Run anyway**.
3. Flip starts in the tray. Drag files while holding <kbd>Ctrl</kbd> to open the donut.

Windows 10 and 11, x64. Flip installs next to Filee without touching it, but run only one of them at a time.

## Build

Requirements: .NET 10 SDK and PowerShell 7.

```powershell
dotnet build src/Filee.App -c Release           # the app: src/Filee.App/bin/Release/net10.0/Flip.exe
pwsh build/build-installer.ps1                   # the installer: Releases/Flip-<version>-win-Setup.exe
python build/make-flip-icon.py                   # regenerates the app icon
```

The project folders keep their original `Filee.*` names; the program, its settings folder (`%AppData%\Flip`), its
installer and its command (`flip`) are Flip. Automatic updates are turned off.

## Developer

**SY_QD**

## Credits

Flip is based on [Filee](https://github.com/KnifeLemon/Filee) by KnifeLemon, used under the
[MIT license](LICENSE). Third-party components are listed in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
Filee's original README is kept in [docs/UPSTREAM-README.md](docs/UPSTREAM-README.md).
