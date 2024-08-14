import os
import shutil
import subprocess

def delete_folder(folder_path):
    """Delete the specified folder and its contents."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Deleted folder: {folder_path}")
    else:
        print(f"Folder not found: {folder_path}")

def install_tmac():
    """Download and install Technitium MAC Address Changer (TMAC)."""
    tmac_url = "https://download.technitium.com/tmac/TMACv6.0.7_Setup.zip"
    tmac_zip_path = "C:/TMACv6.0.7_Setup.zip"
    
    # Download the TMAC zip file
    try:
        import urllib.request
        urllib.request.urlretrieve(tmac_url, tmac_zip_path)
        print("Downloaded TMAC.")
        
        # Unzip the file
        tmac_install_path = "C:/TMAC_Setup"
        shutil.unpack_archive(tmac_zip_path, tmac_install_path)
        print("Unzipped TMAC.")
        
        # Run the TMAC setup
        tmac_exe_path = os.path.join(tmac_install_path, "TMACv6.0.7_Setup.exe")
        subprocess.run([tmac_exe_path, "/SILENT"])
        print("Installed TMAC.")
        
        # Clean up the downloaded files
        os.remove(tmac_zip_path)
        shutil.rmtree(tmac_install_path)
        print("Cleaned up temporary files.")
        
    except Exception as e:
        print(f"Error installing TMAC: {e}")

def main():
    # Delete the SolaraTab folder
    delete_folder("C:/SolaraTab")
    
    # Delete the ROBLOX app data folder
    roblox_appdata = os.path.join(os.getenv('LOCALAPPDATA'), "Roblox")
    delete_folder(roblox_appdata)
    
    # Install TMAC
    install_tmac()

if __name__ == "__main__":
    main()
