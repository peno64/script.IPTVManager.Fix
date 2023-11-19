Fix IPTV Manager configuration

After configure IPTV Simple automatically in IPTV Manager settings, no TV channels are visible.

This is because IPTV Manager generates a settings.xml configuration file for IPTV Simple Client but IPTV Simple Client uses another name for it and this name can vary.
This addon will make it possible to choose the setting file from IPTV Simple Client and it will then copy settings.xml over that selected settings file and remove settings.xml

Installation in kodi via repository https://peno64.github.io/repository.peno64/

Addon is installed and can be found in Add-ons under section Program add-ons

To use this addon, do the following:

Prerequisite: IPTV Manager and IPTV Simple Client are installed. This will be the case if from IPTV Manager settings, IPTV Simple, Configure IPTV Simple automatically was run.

- Install this addon
- Run it. The following will be shown:

   . IPTV Manager Data Folder:
   .   <path>/service.iptv.manager/
   . IPTV Simple Client Manager Data Folder:
   .   <path>/pvr.iptvsimple/
   . IPTV Simple Client Manager Configuration Files:
   D   <path>/pvr.iptvsimple/instance-settings-number.xml
   .   <path>/pvr.iptvsimple/settings.xml
   . settings.xml is generated from IPTV Manager.
   . If also another xml configuration file exists, select it and press ENTER
   . to copy settings.xml to the chosen configuration file.
   . Afterwards, settings.xml will be deleted.

- Now navigate to the line that has the folder icon (here shown as D) and press ENTER to copy settings.xml over this file.
- A new menu with only Done will be shown.
- Press back or ..

- The following will be shown:

   . IPTV Manager Data Folder:
   .   <path>/service.iptv.manager/
   . IPTV Simple Client Manager Data Folder:
   .   <path>/pvr.iptvsimple/
   . IPTV Simple Client Manager Configuration Files:
   .   <path>/pvr.iptvsimple/instance-settings-number.xml
   . settings.xml does not exist (anymore).
   . Nothing to do.

- This means the addon worked as expected. Note also that there is no folder icon anymore so nothing can be chosen.
- Exit the addon

- Run IPTV Manager and in Channels choose Refresh channels and guide now, even if this was done already previously.
- Restart kodi.

This is it. TV should now show the channels.
