# Fix IPTV Manager configuration
Fix IPTV Manager configuration

After configure IPTV Simple automatically in IPTV Manager settings, no TV channels are visible.

This is because IPTV Manager generates a settings.xml configuration file for IPTV Simple Client but IPTV Simple Client uses another name for it and this name can vary.
This addon will make it possible to choose the setting file from IPTV Simple Client and it will then copy settings.xml over that selected settings file and remove settings.xml

# Installation in kodi:
Via repository https://peno64.github.io/repository.peno64/

Addon is installed and can be found in Add-ons under section Program add-ons

# Usage:
To use this addon, do the following:

Prerequisite: IPTV Manager and IPTV Simple Client are installed. This will be the case if from IPTV Manager settings, IPTV Simple, Configure IPTV Simple automatically was run.

- Install this addon
- Run it. The following will be shown:

   . IPTV Manager Data Folder:<br>
   .   <path>/service.iptv.manager/<br>
   . IPTV Simple Client Manager Data Folder:<br>
   .   <path>/pvr.iptvsimple/<br>
   . IPTV Simple Client Manager Configuration Files:<br>
   D   <path>/pvr.iptvsimple/instance-settings-number.xml<br>
   .   <path>/pvr.iptvsimple/settings.xml<br>
   . settings.xml is generated from IPTV Manager.<br>
   . If also another xml configuration file exists, select it and press ENTER<br>
   . to copy settings.xml to the chosen configuration file.<br>
   . Afterwards, settings.xml will be deleted.<br>

- Now navigate to the line that has the folder icon (here shown as D) and press ENTER to copy settings.xml over this file.
- A new menu with only Done will be shown.
- Press back or ..

- The following will be shown:

   . IPTV Manager Data Folder:<br>
   .   <path>/service.iptv.manager/<br>
   . IPTV Simple Client Manager Data Folder:<br>
   .   <path>/pvr.iptvsimple/<br>
   . IPTV Simple Client Manager Configuration Files:<br>
   .   <path>/pvr.iptvsimple/instance-settings-number.xml<br>
   . settings.xml does not exist (anymore).<br>
   . Nothing to do.<br>

- This means the addon worked as expected. Note also that there is no folder icon anymore so nothing can be chosen.
- Exit the addon

- Run IPTV Manager and in Channels choose Refresh channels and guide now, even if this was done already previously.
- Restart kodi.

This is it. TV should now show the channels.
