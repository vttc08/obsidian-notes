### Optimize Space used up by Docker in Windows
The same also applies for WSL.
Check WSL usage
```bash
sudo ncdu / --exclude /mnt
```
WSL Disk Location
```c
%LOCALAPPDATA%\Packages\TheDebianProject.DebianGNULinux_76v4gfsz19hv4\LocalState\ext4.vhdx
```
Docker Disk Location
```c
%LOCALAPPDATA%\Docker\wsl\data\ext4.vhdx
```
Shrink VHD size
- first shutdown wsl first
```c
diskpart
select vdisk file="%LOCALAPPDATA%\Docker\wsl\data\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
```



<hr class="__chatgpt_plugin">

### role::assistant<span style="font-size: small;"> (gemini-2.5-flash-lite)</span>

This is a great guide for managing Docker and WSL disk space in Windows! Here are a few suggestions to enhance its clarity and usability within an Obsidian note:

### Optimize Space Used by Docker and WSL in Windows

This guide provides steps to reclaim disk space used by Docker and the Windows Subsystem for Linux (WSL).

#### 1. Check WSL Disk Usage

To identify large files and directories within your WSL distribution, use `ncdu`. This command excludes the mounted Windows drives (`/mnt`) to focus solely on WSL's internal storage.

```bash
sudo ncdu / --exclude /mnt
```

#### 2. Locate WSL and Docker Virtual Disk Files

The virtual hard disk files (`.vhdx`) for WSL and Docker are typically stored in your user's local application data folder.

*   **WSL Disk Location:**
    ```c
    %LOCALAPPDATA%\Packages\TheDebianProject.DebianGNULinux_76v4gfsz19hv4\LocalState\ext4.vhdx
    ```
    *(Note: The `Packages` subfolder name might vary slightly depending on your specific WSL distribution.)*

*   **Docker Disk Location:**
    ```c
    %LOCALAPPDATA%\Docker\wsl\data\ext4.vhdx
    ```

#### 3. Shrink VHD Size

Before shrinking the virtual disk, ensure that both WSL and Docker are shut down to prevent data corruption.

**Steps:**

1.  **Shut down WSL:**
    Open PowerShell or Command Prompt as an administrator and run:
    ```powershell
    wsl --shutdown
    ```

2.  **Use `diskpart` to compact the VHD:**
    Open PowerShell or Command Prompt as an administrator and execute the following commands:
    ```diskpart
    diskpart
    select vdisk file="%LOCALAPPDATA%\Docker\wsl\data\ext4.vhdx"
    attach vdisk readonly
    compact vdisk
    detach vdisk
    exit
    ```

By following these steps, you can effectively reduce the disk space occupied by your Docker and WSL instances on Windows.



