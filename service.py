# -*- coding: UTF-8 -*-

"""
    Infinity Add-on (C) 2019
    Credits to Lastship, Placenta and Covenant; our thanks go to their creators

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Addon Name: Infinity
# Addon id: plugin.video.infinity
# Addon Provider: Infinity

from resources.lib.modules import log_utils
from resources.lib.modules import control
import threading

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

def syncTraktLibrary():
    control.execute(
        'RunPlugin(plugin://%s)' % 'plugin.video.infinity/?action=tvshowsToLibrarySilent&url=traktcollection')
    control.execute(
        'RunPlugin(plugin://%s)' % 'plugin.video.infinity/?action=moviesToLibrarySilent&url=traktcollection')

try:
    AddonVersion = control.addon('plugin.video.infinity').getAddonInfo('version')
    #RepoVersion = control.addon('repository.infinity').getAddonInfo('version')

    log_utils.log('######################### infinity ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT infinity VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### infinity PLUGIN VERSION: %s ###' % str(AddonVersion), log_utils.LOGNOTICE)
    #log_utils.log('### infinity REPOSITORY VERSION: %s ###' % str(RepoVersion), log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
except:
    log_utils.log('######################### infinity ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT infinity VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### ERROR GETTING infinity VERSIONS - NO HELP WILL BE GIVEN AS THIS IS NOT AN OFFICIAL INFINITY INSTALL. ###', log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)

if control.setting('autoTraktOnStart') == 'true':
    syncTraktLibrary()

if int(control.setting('schedTraktTime')) > 0:
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
    log_utils.log('#################### STARTING TRAKT SCHEDULING ################', log_utils.LOGNOTICE)
    log_utils.log('#################### SCHEDULED TIME FRAME '+ control.setting('schedTraktTime')  + ' HOURS ################', log_utils.LOGNOTICE)
    timeout = 3600 * int(control.setting('schedTraktTime'))
    schedTrakt = threading.Timer(timeout, syncTraktLibrary)
    schedTrakt.start()