//Adapted from original script by Grossley
using System.Text;
using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using UndertaleModLib.Util;

EnsureDataLoaded();

string exportFolder = PromptChooseDirectory();
if (exportFolder == null)
    throw new ScriptException("The export folder was not set.");

//Overwrite Check One
if (File.Exists(exportFolder + "vars.txt"))
{
    bool overwriteCheckOne = ScriptQuestion(@"A 'vars.txt' file already exists.
Would you like to overwrite it?");
    if (overwriteCheckOne)
        File.Delete(exportFolder + "vars.txt");
    if (!overwriteCheckOne)
    {
        ScriptError("A 'vars.txt' file already exists. Please remove it and try again.", "Error: Export already exists.");
        return;
    }
}

using (StreamWriter writer = new StreamWriter(exportFolder + "vars.txt"))
{
    foreach (var scr in Data.Scripts)
    {
        writer.WriteLine(scr.Name);
    }
    foreach (var obj in Data.GameObjects)
    {
        writer.WriteLine(obj.Name);
    }
     foreach (var snd in Data.Sounds)
    {
        writer.WriteLine(snd.Name);
    }
    foreach (var spr in Data.Sprites)
    {
        writer.WriteLine(spr.Name);
    }
    foreach (var shd in Data.Shaders)
    {
        writer.WriteLine(shd.Name);
    }
    foreach (var fnt in Data.Fonts)
    {
        writer.WriteLine(fnt.Name);
        writer.WriteLine(fnt.DisplayName);
    }
    foreach (var rm in Data.Rooms)
    {
        writer.WriteLine(rm.Name);
    }
    foreach (var aug in Data.AudioGroups)
    {
        writer.WriteLine(aug.Name);
    }
    foreach (var tgin in Data.TextureGroupInfo)
    {
        writer.WriteLine(tgin.Name);
    }
}
