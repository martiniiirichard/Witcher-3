using System;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;

namespace Witcher3DirectLauncher
{
    internal static class Program
    {
        [STAThread]
        private static int Main(string[] args)
        {
            string executableName = Path.GetFileNameWithoutExtension(Application.ExecutablePath).ToLowerInvariant();
            string mode = args.Length > 0 ? args[0].Trim().ToLowerInvariant() : (executableName.Contains("dx11") ? "dx11" : "dx12");
            string gameRoot = @"C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY";
            string relativeExe = mode == "dx11" ? @"bin\x64\witcher3.exe" : @"bin\x64_dx12\witcher3.exe";
            string exePath = Path.Combine(gameRoot, relativeExe);

            if (!File.Exists(exePath))
            {
                MessageBox.Show(
                    "Could not find Witcher 3 executable:\n\n" + exePath,
                    "Witcher 3 Direct Launcher",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
                return 1;
            }

            try
            {
                ProcessStartInfo startInfo = new ProcessStartInfo
                {
                    FileName = exePath,
                    WorkingDirectory = Path.GetDirectoryName(exePath),
                    UseShellExecute = true
                };

                Process.Start(startInfo);
                return 0;
            }
            catch (Exception ex)
            {
                MessageBox.Show(
                    "Failed to launch Witcher 3:\n\n" + ex.Message,
                    "Witcher 3 Direct Launcher",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
                return 2;
            }
        }
    }
}
