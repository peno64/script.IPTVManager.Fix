import xbmcaddon
import xbmcgui
import xbmcplugin
import re
import sys
#import pathlib
import glob, os
import urllib.parse
from urllib.parse import parse_qsl
import xbmcvfs
import shutil

quote_plus = urllib.parse.quote_plus

AddonID = 'script.IPTVManager.Fix'

def addonFanart():
    return xbmcvfs.translatePath(os.path.join('special://home/addons/' + AddonID , 'fanart.jpg'))

def addonIcon():
    path = xbmcvfs.translatePath(os.path.join('special://home/addons/' + AddonID , 'icon.png'))
    return path

# ICONS FANARTS
ADDON_FANART  = addonFanart()
ADDON_ICON    = addonIcon()

IPTV_MANAGER_ID = 'service.iptv.manager'
IPTV_SIMPLE_ID = 'pvr.iptvsimple'

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

addon_iptvManager = xbmcaddon.Addon(IPTV_MANAGER_ID)
addon_iptvsimple = xbmcaddon.Addon(IPTV_SIMPLE_ID)

def CreateDir(name, url, action, icon, fanart, description, isFolder=False, iconImage="DefaultFolder.png"):
        if icon == None or icon == '': icon = ADDON_ICON
        u=sys.argv[0]+"?url="+quote_plus(url)+"&action="+str(action)+"&name="+quote_plus(name)+"&icon="+quote_plus(icon)+"&fanart="+quote_plus(fanart)+"&description="+quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name)
        liz.setArt({'icon': iconImage})
        liz.setArt({'thumbnailImage': icon})
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
        return ok

def MainMenu():
  CreateDir('[COLOR white][B]IPTV Manager Data Folder:[/B][/COLOR]','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)

  line = '   ' + xbmcvfs.translatePath(addon_iptvManager.getAddonInfo('profile'))
  CreateDir(line,'ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)


  CreateDir('[COLOR white][B]IPTV Simple Client Manager Data Folder:[/B][/COLOR]','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)

  line = '   ' + xbmcvfs.translatePath(addon_iptvsimple.getAddonInfo('profile'))
  CreateDir(line,'ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)


  CreateDir('[COLOR white][B]IPTV Simple Client Manager Configuration Files:[/B][/COLOR]','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)

  path = xbmcvfs.translatePath(addon_iptvsimple.getAddonInfo('profile'))
  settingsxml = xbmcvfs.translatePath(addon_iptvsimple.getAddonInfo('profile')) + 'settings.xml'
  settingsxmlexists = os.path.isfile(settingsxml)
  for f in glob.glob(path + "*.xml"):
    if os.path.basename(f) == 'settings.xml':
      CreateDir('   ' + '[COLOR yellow]' + f + '[/COLOR]','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)
    else:
      CreateDir('   ' + '[COLOR green]' + f + '[/COLOR]',f, 'copy', ADDON_ICON,ADDON_FANART,'', isFolder=settingsxmlexists)

  if settingsxmlexists:
    CreateDir('[COLOR yellow]settings.xml[/COLOR] is generated from IPTV Manager.','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)
    CreateDir('If also [COLOR green]another .xml[/COLOR] configuration file exists, select [COLOR green]it[/COLOR] and press ENTER','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)
    CreateDir('to copy [COLOR yellow]settings.xml[/COLOR] to the [COLOR green]chosen configuration file[/COLOR].','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)
    CreateDir('Afterwards, [COLOR yellow]settings.xml[/COLOR] will be deleted.','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)
  else:
    CreateDir('[COLOR yellow]settings.xml[/COLOR] does not exist (anymore).','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)
    CreateDir('Nothing to do.','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)

params = dict(parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

if action == None: MainMenu()
elif action == 'copy':
  settingsxml = xbmcvfs.translatePath(addon_iptvsimple.getAddonInfo('profile')) + 'settings.xml'
  if os.path.isfile(settingsxml):
    url = params.get('url')
    shutil.copyfile(settingsxml, url)
    os.remove(settingsxml)
    CreateDir('[COLOR white][B]Done[/B][/COLOR]','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)
  else:
    CreateDir('[COLOR red][B]Unexisting ' + settingsxml + '[/B][/COLOR]','ur', '', ADDON_ICON,ADDON_FANART,'', isFolder=False)

xbmcplugin.setContent(int(sys.argv[1]), 'files')

xbmcplugin.endOfDirectory(int(sys.argv[1]))
