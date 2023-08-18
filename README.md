# HoloCure-YYC-String-Things
Some terrible code that extracts strings from HoloCure.exe (0.6, YYC-compiled) and imports modified strings back. Might be useful for unofficial translation.  
This only deals with texts, use [UndertaleModTool](https://github.com/krzys-h/UndertaleModTool) if you need to deal with fonts.

## Usage
* `String_extract.py` - Extracts strings from `HoloCure.exe`.
* `String_inject.py` - Imports modified strings into `HoloCure.exe`.
* `String_patch.py` - Migrates translated strings to strings exported from new version.
* `String_trim.py` - Throws away trash strings in extracted string file, good for translator's eyes. Use with `ExportVarNames.csx` and `String_patch.py`.
* `ExportVarNames.csx` - Exports trash strings from `data.win`, run it with [UndertaleModTool](https://github.com/krzys-h/UndertaleModTool).

## Notice
Poorly written code, it works anyway.  
Translated strings longer than the original ones might be broken.  
**Don't import trimmed strings directly**, most likely to break the game unless all translated strings are not longer than the original ones.  
