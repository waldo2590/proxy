import os
import wx
import PySimpleGUIWx as sg

from setup import Proxy

class ProxyConnection(object):
    def __init__(self):
        super(ProxyConnection, self).__init__()

        self.CONNECT = 'Connect'
        self.DISCONNECT = 'Disconnect'
        self.EXIT = 'Exit'
        
        # tray icon details
        self.icon_dir = os.path.join(os.getcwd().replace(os.sep, '/')+'/assets/icons')
        self.on_icon = os.path.join(self.icon_dir+'/on.png')
        self.off_icon = os.path.join(self.icon_dir+'/off.png')
        print('on {} off {}'.format(self.on_icon, self.off_icon))
        # ##

        # system tray items
        self.context_items = [self.CONNECT, self.DISCONNECT, '---', self.EXIT]
        self.menu_def = ['UNUSED', self.context_items]
        self.tray = sg.SystemTray(menu=self.menu_def, filename=self.on_icon)
        # ##
        
        # proxy details
        self.proxy = Proxy()
        # ##

        # flags
        self.is_connected = False
    
    def _toggle_tray_icon(self, is_connected=True):
        tooltip_msg = 'Cloud Server {}'.format('connected' if is_connected else 'disconnected')
        self.tray.Update(menu=self.menu_def, filename=self.on_icon if is_connected else self.off_icon, tooltip=tooltip_msg)
        self.is_connected = is_connected
        return True
        
    def _connect(self):
        # try:
        self.tray.ShowMessage('Starting', 'Intialising..')
        self.proxy._run()
        self.tray.ShowMessage('Connected', 'Start exploring')
        self._toggle_tray_icon(is_connected=True)
        # except Exception as ex:
            # self.tray.ShowMessage('Error', '{}'.format(ex))
    def _disconnect(self):
        try:
            self.tray.ShowMessage('Reverting', 'Please Wait')
            self.proxy._revert_system_proxy()
            self._toggle_tray_icon(is_connected=False)
            self.tray.ShowMessage('Disconnected', 'All settings reverted')
        except Exception as ex:
            self.tray.ShowMessage('Error', '{}'.format(ex))
    def _start(self):
        if not self.is_connected:
            self._connect()
        while True:
            event = self.tray.Read()
            if event == self.EXIT:
                break
            elif event == self.CONNECT:
                self._connect()
            elif event == self.DISCONNECT:
                self._disconnect()

if __name__ == "__main__":
    proxy_conn = ProxyConnection()
    try:
        proxy_conn.proxy._revert_system_proxy()
        proxy_conn._start()
    except Exception as ex:
        proxy_conn.proxy._revert_system_proxy()
        raise ex
    
    