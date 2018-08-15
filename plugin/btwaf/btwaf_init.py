# uncompyle6 version 3.2.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.12 (default, Dec  4 2017, 14:50:18)
# [GCC 5.4.0 20160609]
# Embedded file name: /www/server/panel/plugin/btwaf/btwaf_init.py
# Compiled at: 2018-06-25 18:45:56
import sys
sys.path.append('/www/server/panel/class')
reload(sys)
import json, os, time, public, string, web
from panelAuth import panelAuth

class plugin_nginx_init:
    __OOOOOOO00O0O000O0 = '/www/server/btwaf/'
    __OO0O0000OOO0O00OO = {True: '\xe5\xbc\x80\xe5\x90\xaf', False: '\xe5\x85\xb3\xe9\x97\xad', 0: '\xe5\x81\x9c\xe7\x94\xa8', 1: '\xe5\x90\xaf\xe7\x94\xa8'}
    __O000OOOOOOOO00OO0 = None

    def get_config(OO00000O0O000OO0O, OO000OOO0OO0OO000):
        OO000OOO0O0O0000O = json.loads(public.readFile(OO00000O0O000OO0O.__OOOOOOO00O0O000O0 + 'config.json'))
        if 'retry_cycle' not in OO000OOO0O0O0000O:
            OO000OOO0O0O0000O['retry_cycle'] = 60
            OO00000O0O000OO0O.__OOO00OO0OOO00OOO0(OO000OOO0O0O0000O)
        if OO000OOO0O0O0000O['start_time'] == 0:
            OO000OOO0O0O0000O['start_time'] = time.time()
            OO00000O0O000OO0O.__OOO00OO0OOO00OOO0(OO000OOO0O0O0000O)
        return OO000OOO0O0O0000O

    def get_site_config(O0OOO000O0O0OOOO0, OOO000OOOO000OOOO):
        OO00OO0O0000OO000 = public.readFile(O0OOO000O0O0OOOO0.__OOOOOOO00O0O000O0 + 'site.json')
        O00OO0O0OO0OO00OO = O0OOO000O0O0OOOO0.__O0OOOOO0OOO00OO00(json.loads(OO00OO0O0000OO000))
        if OOO000OOOO000OOOO:
            OOO0OO000OOO0O0O0 = O0OOO000O0O0OOOO0.get_total(None)['sites']
            OOO00OOOO0O000000 = []
            for OOO0O0O0OO0O00O0O in O00OO0O0OO0OO00OO.keys():
                if OOO0O0O0OO0O00O0O not in OOO0OO000OOO0O0O0:
                    OOO0OO000OOO0O0O0[OOO0O0O0OO0O00O0O] = {}
                O00OO0O0OO0OO00OO[OOO0O0O0OO0O00O0O]['total'] = O0OOO000O0O0OOOO0.__OO0O00O0O0O0OO0O0(OOO0OO000OOO0O0O0[OOO0O0O0OO0O00O0O])
                O000O000OO000O0OO = O00OO0O0OO0OO00OO[OOO0O0O0OO0O00O0O]
                O000O000OO000O0OO['siteName'] = OOO0O0O0OO0O00O0O
                OOO00OOOO0O000000.append(O000O000OO000O0OO)

            O00OO0O0OO0OO00OO = sorted(OOO00OOOO0O000000, key=lambda OO0OO0OO0O0O00OO0: OO0OO0OO0O0O00OO0['log_size'], reverse=True)
        return O00OO0O0OO0OO00OO

    def get_site_config_byname(OOOOO0OOOO0O00OOO, OO000OO0O0O0OOOOO):
        OOO0O00OOO00O0O00 = OOOOO0OOOO0O00OOO.get_site_config(None)
        O0O00O00OO00O0O00 = OOO0O00OOO00O0O00[OO000OO0O0O0OOOOO.siteName]
        O0O00O00OO00O0O00['top'] = OOOOO0OOOO0O00OOO.get_config(None)
        return O0O00O00OO00O0O00

    def set_open(OO00O0O0OO0000OO0, OO00000OO00O00OOO):
        O00O0O00O0OO0OOO0 = OO00O0O0OO0000OO0.get_config(None)
        if O00O0O00O0OO0OOO0['open']:
            O00O0O00O0OO0OOO0['open'] = False
            O00O0O00O0OO0OOO0['start_time'] = 0
        else:
            O00O0O00O0OO0OOO0['open'] = True
            O00O0O00O0OO0OOO0['start_time'] = int(time.time())
        OO00O0O0OO0000OO0.__OO0000000OOO00O0O(OO00O0O0OO0000OO0.__OO0O0000OOO0O00OO[O00O0O00O0OO0OOO0['open']] + '\xe7\xbd\x91\xe7\xab\x99\xe9\x98\xb2\xe7\x81\xab\xe5\xa2\x99(WAF)')
        OO00O0O0OO0000OO0.__OOO00OO0OOO00OOO0(O00O0O00O0OO0OOO0)
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def set_obj_open(O00O00O0OOO0OOO00, O00OO0OO000O0O0OO):
        O00OOO00O0OO0O00O = O00O00O0OOO0OOO00.get_config(None)
        if type(O00OOO00O0OO0O00O[O00OO0OO000O0O0OO.obj]) != bool:
            if O00OOO00O0OO0O00O[O00OO0OO000O0O0OO.obj]['open']:
                O00OOO00O0OO0O00O[O00OO0OO000O0O0OO.obj]['open'] = False
            else:
                O00OOO00O0OO0O00O[O00OO0OO000O0O0OO.obj]['open'] = True
            O00O00O0OOO0OOO00.__OO0000000OOO00O0O(O00O00O0OOO0OOO00.__OO0O0000OOO0O00OO[O00OOO00O0OO0O00O[O00OO0OO000O0O0OO.obj]['open']] + '\xe3\x80\x90' + O00OO0OO000O0O0OO.obj + '\xe3\x80\x91\xe5\x8a\x9f\xe8\x83\xbd')
        else:
            if O00OOO00O0OO0O00O[O00OO0OO000O0O0OO.obj]:
                O00OOO00O0OO0O00O[O00OO0OO000O0O0OO.obj] = False
            else:
                O00OOO00O0OO0O00O[O00OO0OO000O0O0OO.obj] = True
            O00O00O0OOO0OOO00.__OO0000000OOO00O0O(O00O00O0OOO0OOO00.__OO0O0000OOO0O00OO[O00OOO00O0OO0O00O[O00OO0OO000O0O0OO.obj]] + '\xe3\x80\x90' + O00OO0OO000O0O0OO.obj + '\xe3\x80\x91\xe5\x8a\x9f\xe8\x83\xbd')
        O00O00O0OOO0OOO00.__OOO00OO0OOO00OOO0(O00OOO00O0OO0O00O)
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def set_site_obj_open(O0O0O0OO000OOOO00, O000O0OO000OO000O):
        OO00O00OO0000OOOO = O0O0O0OO000OOOO00.get_site_config(None)
        if type(OO00O00OO0000OOOO[O000O0OO000OO000O.siteName][O000O0OO000OO000O.obj]) != bool:
            if OO00O00OO0000OOOO[O000O0OO000OO000O.siteName][O000O0OO000OO000O.obj]['open']:
                OO00O00OO0000OOOO[O000O0OO000OO000O.siteName][O000O0OO000OO000O.obj]['open'] = False
            else:
                OO00O00OO0000OOOO[O000O0OO000OO000O.siteName][O000O0OO000OO000O.obj]['open'] = True
            O0O0O0OO000OOOO00.__OO0000000OOO00O0O(O0O0O0OO000OOOO00.__OO0O0000OOO0O00OO[OO00O00OO0000OOOO[O000O0OO000OO000O.siteName][O000O0OO000OO000O.obj]['open']] + '\xe7\xbd\x91\xe7\xab\x99\xe3\x80\x90' + O000O0OO000OO000O.siteName + '\xe3\x80\x91\xe3\x80\x90' + O000O0OO000OO000O.obj + '\xe3\x80\x91\xe5\x8a\x9f\xe8\x83\xbd')
        else:
            if OO00O00OO0000OOOO[O000O0OO000OO000O.siteName][O000O0OO000OO000O.obj]:
                OO00O00OO0000OOOO[O000O0OO000OO000O.siteName][O000O0OO000OO000O.obj] = False
            else:
                OO00O00OO0000OOOO[O000O0OO000OO000O.siteName][O000O0OO000OO000O.obj] = True
            O0O0O0OO000OOOO00.__OO0000000OOO00O0O(O0O0O0OO000OOOO00.__OO0O0000OOO0O00OO[OO00O00OO0000OOOO[O000O0OO000OO000O.siteName][O000O0OO000OO000O.obj]] + '\xe7\xbd\x91\xe7\xab\x99\xe3\x80\x90' + O000O0OO000OO000O.siteName + '\xe3\x80\x91\xe3\x80\x90' + O000O0OO000OO000O.obj + '\xe3\x80\x91\xe5\x8a\x9f\xe8\x83\xbd')
        if O000O0OO000OO000O.obj == 'drop_abroad':
            O0O0O0OO000OOOO00.__O000OOO0OO0OOOO0O()
        O0O0O0OO000OOOO00.__OO000000OO00O00O0(OO00O00OO0000OOOO)
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def set_obj_status(OOOOO0OO000OO00OO, O0O000OO0O0O0O000):
        O0000O0O0O0OO000O = OOOOO0OO000OO00OO.get_config(None)
        O0000O0O0O0OO000O[O0O000OO0O0O0O000.obj]['status'] = int(O0O000OO0O0O0O000.statusCode)
        OOOOO0OO000OO00OO.__OOO00OO0OOO00OOO0(O0000O0O0O0OO000O)
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def set_cc_conf(OO00OOOOO0OO00OO0, O0O0O000O0OOOO00O):
        OO0OO0O0OO00OOOOO = OO00OOOOO0OO00OO0.get_config(None)
        OO0OO0O0OO00OOOOO['cc']['cycle'] = int(O0O0O000O0OOOO00O.cycle)
        OO0OO0O0OO00OOOOO['cc']['limit'] = int(O0O0O000O0OOOO00O.limit)
        OO0OO0O0OO00OOOOO['cc']['endtime'] = int(O0O0O000O0OOOO00O.endtime)
        OO0OO0O0OO00OOOOO['cc']['increase'] = (O0O0O000O0OOOO00O.increase == '1') | False
        OO00OOOOO0OO00OO0.__OOO00OO0OOO00OOO0(OO0OO0O0OO00OOOOO)
        OO00OOOOO0OO00OO0.__OO0000000OOO00O0O('\xe8\xae\xbe\xe7\xbd\xae\xe5\x85\xa8\xe5\xb1\x80CC\xe9\x85\x8d\xe7\xbd\xae\xe4\xb8\xba\xef\xbc\x9a' + O0O0O000O0OOOO00O.cycle + ' \xe7\xa7\x92\xe5\x86\x85\xe7\xb4\xaf\xe8\xae\xa1\xe8\xaf\xb7\xe6\xb1\x82\xe8\xb6\x85\xe8\xbf\x87 ' + O0O0O000O0OOOO00O.limit + ' \xe6\xac\xa1\xe5\x90\x8e,\xe5\xb0\x81\xe9\x94\x81 ' + O0O0O000O0OOOO00O.endtime + ' \xe7\xa7\x92' + ',\xe5\xa2\x9e\xe5\xbc\xba:' + O0O0O000O0OOOO00O.increase)
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def set_site_cc_conf(O000O0OOOO0000O00, O00OO0OO000OO0O00):
        O000O0OO00000000O = O000O0OOOO0000O00.get_site_config(None)
        O000O0OO00000000O[O00OO0OO000OO0O00.siteName]['cc']['cycle'] = int(O00OO0OO000OO0O00.cycle)
        O000O0OO00000000O[O00OO0OO000OO0O00.siteName]['cc']['limit'] = int(O00OO0OO000OO0O00.limit)
        O000O0OO00000000O[O00OO0OO000OO0O00.siteName]['cc']['endtime'] = int(O00OO0OO000OO0O00.endtime)
        O000O0OO00000000O[O00OO0OO000OO0O00.siteName]['cc']['increase'] = (O00OO0OO000OO0O00.increase == '1') | False
        O000O0OOOO0000O00.__OO000000OO00O00O0(O000O0OO00000000O)
        O000O0OOOO0000O00.__OO0000000OOO00O0O('\xe8\xae\xbe\xe7\xbd\xae\xe7\xab\x99\xe7\x82\xb9\xe3\x80\x90' + O00OO0OO000OO0O00.siteName + '\xe3\x80\x91CC\xe9\x85\x8d\xe7\xbd\xae\xe4\xb8\xba\xef\xbc\x9a' + O00OO0OO000OO0O00.cycle + ' \xe7\xa7\x92\xe5\x86\x85\xe7\xb4\xaf\xe8\xae\xa1\xe8\xaf\xb7\xe6\xb1\x82\xe8\xb6\x85\xe8\xbf\x87 ' + O00OO0OO000OO0O00.limit + ' \xe6\xac\xa1\xe5\x90\x8e,\xe5\xb0\x81\xe9\x94\x81 ' + O00OO0OO000OO0O00.endtime + ' \xe7\xa7\x92' + ',\xe5\xa2\x9e\xe5\xbc\xba:' + O00OO0OO000OO0O00.increase)
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def add_cnip(O0O0OOOOO0O0000O0, OOO0OOOO00O0000OO):
        OO0O0OOO00OO0O00O = [O0O0OOOOO0O0000O0.__OO00O00OO00OO000O(OOO0OOOO00O0000OO.start_ip), O0O0OOOOO0O0000O0.__OO00O00OO00OO000O(OOO0OOOO00O0000OO.end_ip)]
        if not OO0O0OOO00OO0O00O[0] or not OO0O0OOO00OO0O00O[1]:
            return public.returnMsg(False, 'IP\xe6\xae\xb5\xe6\xa0\xbc\xe5\xbc\x8f\xe4\xb8\x8d\xe6\xad\xa3\xe7\xa1\xae')
        if not O0O0OOOOO0O0000O0.__O00OOOO0OO00OOOOO(OO0O0OOO00OO0O00O):
            return public.returnMsg(False, '\xe8\xb5\xb7\xe5\xa7\x8bIP\xe4\xb8\x8d\xe8\x83\xbd\xe5\xa4\xa7\xe4\xba\x8e\xe7\xbb\x93\xe6\x9d\x9fIP')
        OO00OO0000O00O000 = O0O0OOOOO0O0000O0.__O000O0OO000O0OO0O('cn')
        if OO0O0OOO00OO0O00O in OO00OO0000O00O000:
            return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9aIP\xe6\xae\xb5\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8!')
        OO00OO0000O00O000.insert(0, OO0O0OOO00OO0O00O)
        O0O0OOOOO0O0000O0.__OO0OO000O000O0O0O('cn', OO00OO0000O00O000)
        O0O0OOOOO0O0000O0.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0IP\xe6\xae\xb5[' + OOO0OOOO00O0000OO.start_ip + '-' + OOO0OOOO00O0000OO.end_ip + ']\xe5\x88\xb0\xe5\x9b\xbd\xe5\x86\x85IP\xe5\xba\x93')
        return public.returnMsg(True, '\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x88\x90\xe5\x8a\x9f!')

    def remove_cnip(OO0OO000OOOO00OOO, O0OOO0O0O0000O0O0):
        OOO0000O0OOO0OOO0 = int(O0OOO0O0O0000O0O0.index)
        O00O0000O0O00O00O = OO0OO000OOOO00OOO.__O000O0OO000O0OO0O('cn')
        OO000O0O000O0O000 = O00O0000O0O00O00O[OOO0000O0OOO0OOO0]
        del O00O0000O0O00O00O[OOO0000O0OOO0OOO0]
        OO0OO000OOOO00OOO.__OO0OO000O000O0O0O('cn', O00O0000O0O00O00O)
        OO0OO000OOOO00OOO.__OO0000000OOO00O0O('\xe4\xbb\x8e\xe5\x9b\xbd\xe5\x86\x85IP\xe5\xba\x93\xe5\x88\xa0\xe9\x99\xa4[' + ('.').join(map(str, OO000O0O000O0O000[0])) + '-' + ('.').join(map(str, OO000O0O000O0O000[1])) + ']')
        return public.returnMsg(True, '\xe5\x88\xa0\xe9\x99\xa4\xe6\x88\x90\xe5\x8a\x9f!')

    def add_ip_white(OOO00OOOO0OO0OOOO, OOOOOO0000O00000O):
        O0OO00O0000OO0O0O = [OOO00OOOO0OO0OOOO.__OO00O00OO00OO000O(OOOOOO0000O00000O.start_ip), OOO00OOOO0OO0OOOO.__OO00O00OO00OO000O(OOOOOO0000O00000O.end_ip)]
        if not O0OO00O0000OO0O0O[0] or not O0OO00O0000OO0O0O[1]:
            return public.returnMsg(False, 'IP\xe6\xae\xb5\xe6\xa0\xbc\xe5\xbc\x8f\xe4\xb8\x8d\xe6\xad\xa3\xe7\xa1\xae')
        if not OOO00OOOO0OO0OOOO.__O00OOOO0OO00OOOOO(O0OO00O0000OO0O0O):
            return public.returnMsg(False, '\xe8\xb5\xb7\xe5\xa7\x8bIP\xe4\xb8\x8d\xe8\x83\xbd\xe5\xa4\xa7\xe4\xba\x8e\xe7\xbb\x93\xe6\x9d\x9fIP')
        O0OO00O000O00OOO0 = OOO00OOOO0OO0OOOO.__O000O0OO000O0OO0O('ip_white')
        if O0OO00O0000OO0O0O in O0OO00O000O00OOO0:
            return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9aIP\xe6\xae\xb5\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8!')
        O0OO00O000O00OOO0.insert(0, O0OO00O0000OO0O0O)
        OOO00OOOO0OO0OOOO.__OO0OO000O000O0O0O('ip_white', O0OO00O000O00OOO0)
        OOO00OOOO0OO0OOOO.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0IP\xe6\xae\xb5[' + OOOOOO0000O00000O.start_ip + '-' + OOOOOO0000O00000O.end_ip + ']\xe5\x88\xb0IP\xe7\x99\xbd\xe5\x90\x8d\xe5\x8d\x95')
        return public.returnMsg(True, '\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x88\x90\xe5\x8a\x9f!')

    def remove_ip_white(O0O0OOO0O00OO00OO, OOOOO0O0O0OO00000):
        O00OOO0O0OOOOOOO0 = int(OOOOO0O0O0OO00000.index)
        OO0O0O000OOOO000O = O0O0OOO0O00OO00OO.__O000O0OO000O0OO0O('ip_white')
        OOO0000OOO0000O00 = OO0O0O000OOOO000O[O00OOO0O0OOOOOOO0]
        del OO0O0O000OOOO000O[O00OOO0O0OOOOOOO0]
        O0O0OOO0O00OO00OO.__OO0OO000O000O0O0O('ip_white', OO0O0O000OOOO000O)
        O0O0OOO0O00OO00OO.__OO0000000OOO00O0O('\xe4\xbb\x8eIP\xe7\x99\xbd\xe5\x90\x8d\xe5\x8d\x95\xe5\x88\xa0\xe9\x99\xa4[' + ('.').join(map(str, OOO0000OOO0000O00[0])) + '-' + ('.').join(map(str, OOO0000OOO0000O00[1])) + ']')
        return public.returnMsg(True, '\xe5\x88\xa0\xe9\x99\xa4\xe6\x88\x90\xe5\x8a\x9f!')

    def add_ip_black(O0O00OOOO00OO0O0O, O0OOO0O0O00000O0O):
        O00O00000O0O0OOOO = [O0O00OOOO00OO0O0O.__OO00O00OO00OO000O(O0OOO0O0O00000O0O.start_ip), O0O00OOOO00OO0O0O.__OO00O00OO00OO000O(O0OOO0O0O00000O0O.end_ip)]
        if not O00O00000O0O0OOOO[0] or not O00O00000O0O0OOOO[1]:
            return public.returnMsg(False, 'IP\xe6\xae\xb5\xe6\xa0\xbc\xe5\xbc\x8f\xe4\xb8\x8d\xe6\xad\xa3\xe7\xa1\xae')
        if not O0O00OOOO00OO0O0O.__O00OOOO0OO00OOOOO(O00O00000O0O0OOOO):
            return public.returnMsg(False, '\xe8\xb5\xb7\xe5\xa7\x8bIP\xe4\xb8\x8d\xe8\x83\xbd\xe5\xa4\xa7\xe4\xba\x8e\xe7\xbb\x93\xe6\x9d\x9fIP')
        O0OOOOOO000O000OO = O0O00OOOO00OO0O0O.__O000O0OO000O0OO0O('ip_black')
        if O00O00000O0O0OOOO in O0OOOOOO000O000OO:
            return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9aIP\xe6\xae\xb5\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8!')
        O0OOOOOO000O000OO.insert(0, O00O00000O0O0OOOO)
        O0O00OOOO00OO0O0O.__OO0OO000O000O0O0O('ip_black', O0OOOOOO000O000OO)
        O0O00OOOO00OO0O0O.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0IP\xe6\xae\xb5[' + O0OOO0O0O00000O0O.start_ip + '-' + O0OOO0O0O00000O0O.end_ip + ']\xe5\x88\xb0IP\xe9\xbb\x91\xe5\x90\x8d\xe5\x8d\x95')
        return public.returnMsg(True, '\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x88\x90\xe5\x8a\x9f!')

    def remove_ip_black(OOO00O00O000O0000, O0O0000OO0O000000):
        OO0O0000000000OO0 = int(O0O0000OO0O000000.index)
        O0O0000OOOO000OO0 = OOO00O00O000O0000.__O000O0OO000O0OO0O('ip_black')
        O0000OO000O0O00OO = O0O0000OOOO000OO0[OO0O0000000000OO0]
        del O0O0000OOOO000OO0[OO0O0000000000OO0]
        OOO00O00O000O0000.__OO0OO000O000O0O0O('ip_black', O0O0000OOOO000OO0)
        OOO00O00O000O0000.__OO0000000OOO00O0O('\xe4\xbb\x8eIP\xe9\xbb\x91\xe5\x90\x8d\xe5\x8d\x95\xe5\x88\xa0\xe9\x99\xa4[' + ('.').join(map(str, O0000OO000O0O00OO[0])) + '-' + ('.').join(map(str, O0000OO000O0O00OO[1])) + ']')
        return public.returnMsg(True, '\xe5\x88\xa0\xe9\x99\xa4\xe6\x88\x90\xe5\x8a\x9f!')

    def add_url_white(O0O00OOOOOO0OOO00, OO0000O0OOOOOO0O0):
        O0OOO000OO000O0O0 = O0O00OOOOOO0OOO00.__O000O0OO000O0OO0O('url_white')
        O000OO0OOOOOO0O00 = OO0000O0OOOOOO0O0.url_rule.strip()
        if OO0000O0OOOOOO0O0.url_rule in O0OOO000OO000O0O0:
            return public.returnMsg(False, '\xe6\x82\xa8\xe6\xb7\xbb\xe5\x8a\xa0\xe7\x9a\x84URL\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8')
        O0OOO000OO000O0O0.insert(0, O000OO0OOOOOO0O00)
        O0O00OOOOOO0OOO00.__OO0OO000O000O0O0O('url_white', O0OOO000OO000O0O0)
        O0O00OOOOOO0OOO00.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0url\xe8\xa7\x84\xe5\x88\x99[' + O000OO0OOOOOO0O00 + ']\xe5\x88\xb0URL\xe7\x99\xbd\xe5\x90\x8d\xe5\x8d\x95')
        return public.returnMsg(True, '\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x88\x90\xe5\x8a\x9f!')

    def remove_url_white(O0000O00O0OO0O00O, OO0O0OO0O0O000O00):
        O0OOOO0OOO0O00OO0 = O0000O00O0OO0O00O.__O000O0OO000O0OO0O('url_white')
        O0O0OO000000O00OO = int(OO0O0OO0O0O000O00.index)
        OO0O0O0O000O0OOOO = O0OOOO0OOO0O00OO0[O0O0OO000000O00OO]
        del O0OOOO0OOO0O00OO0[O0O0OO000000O00OO]
        O0000O00O0OO0O00O.__OO0OO000O000O0O0O('url_white', O0OOOO0OOO0O00OO0)
        O0000O00O0OO0O00O.__OO0000000OOO00O0O('\xe4\xbb\x8eURL\xe7\x99\xbd\xe5\x90\x8d\xe5\x8d\x95\xe5\x88\xa0\xe9\x99\xa4URL\xe8\xa7\x84\xe5\x88\x99[' + OO0O0O0O000O0OOOO + ']')
        return public.returnMsg(True, '\xe5\x88\xa0\xe9\x99\xa4\xe6\x88\x90\xe5\x8a\x9f!')

    def add_url_black(O0OO0000000O0OOO0, OOOOOO00OO00OO0OO):
        O0000OO0O00OO0O0O = O0OO0000000O0OOO0.__O000O0OO000O0OO0O('url_black')
        O0O00O00O00OOOOOO = OOOOOO00OO00OO0OO.url_rule.strip()
        if OOOOOO00OO00OO0OO.url_rule in O0000OO0O00OO0O0O:
            return public.returnMsg(False, '\xe6\x82\xa8\xe6\xb7\xbb\xe5\x8a\xa0\xe7\x9a\x84URL\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8')
        O0000OO0O00OO0O0O.insert(0, O0O00O00O00OOOOOO)
        O0OO0000000O0OOO0.__OO0OO000O000O0O0O('url_black', O0000OO0O00OO0O0O)
        O0OO0000000O0OOO0.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0url\xe8\xa7\x84\xe5\x88\x99[' + O0O00O00O00OOOOOO + ']\xe5\x88\xb0URL\xe9\xbb\x91\xe5\x90\x8d\xe5\x8d\x95')
        return public.returnMsg(True, '\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x88\x90\xe5\x8a\x9f!')

    def remove_url_black(OO0OO00O0O00O0OOO, OOOO000OOOOO00OO0):
        O000OO0O000000OOO = OO0OO00O0O00O0OOO.__O000O0OO000O0OO0O('url_black')
        O000OOOOO00000O00 = int(OOOO000OOOOO00OO0.index)
        OOO000O0O00O000O0 = O000OO0O000000OOO[O000OOOOO00000O00]
        del O000OO0O000000OOO[O000OOOOO00000O00]
        OO0OO00O0O00O0OOO.__OO0OO000O000O0O0O('url_black', O000OO0O000000OOO)
        OO0OO00O0O00O0OOO.__OO0000000OOO00O0O('\xe4\xbb\x8eURL\xe9\xbb\x91\xe5\x90\x8d\xe5\x8d\x95\xe5\x88\xa0\xe9\x99\xa4URL\xe8\xa7\x84\xe5\x88\x99[' + OOO000O0O00O000O0 + ']')
        return public.returnMsg(True, '\xe5\x88\xa0\xe9\x99\xa4\xe6\x88\x90\xe5\x8a\x9f!')

    def save_scan_rule(O0O00O0O000OO0000, O00OO0OOO0O00O0O0):
        OO00OOOOO0OOOO0OO = {'header': O00OO0OOO0O00O0O0.header, 'cookie': O00OO0OOO0O00O0O0.cookie, 'args': O00OO0OOO0O00O0O0.args}
        O0O00O0O000OO0000.__OO0OO000O000O0O0O('scan_black', OO00OOOOO0OOOO0OO)
        O0O00O0O000OO0000.__OO0000000OOO00O0O('\xe4\xbf\xae\xe6\x94\xb9\xe6\x89\xab\xe6\x8f\x8f\xe5\x99\xa8\xe8\xbf\x87\xe6\xbb\xa4\xe8\xa7\x84\xe5\x88\x99')
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f')

    def set_retry(O0OO0OOOOO00000OO, OO00O00O0O0O00OO0):
        O0O0O00O0O0O0O000 = O0OO0OOOOO00000OO.get_config(None)
        O0O0O00O0O0O0O000['retry'] = int(OO00O00O0O0O00OO0.retry)
        O0O0O00O0O0O0O000['retry_cycle'] = int(OO00O00O0O0O00OO0.retry_cycle)
        O0O0O00O0O0O0O000['retry_time'] = int(OO00O00O0O0O00OO0.retry_time)
        O0OO0OOOOO00000OO.__OOO00OO0OOO00OOO0(O0O0O00O0O0O0O000)
        O0OO0OOOOO00000OO.__OO0000000OOO00O0O('\xe8\xae\xbe\xe7\xbd\xae\xe9\x9d\x9e\xe6\xb3\x95\xe8\xaf\xb7\xe6\xb1\x82\xe5\xae\xb9\xe5\xbf\x8d\xe9\x98\x88\xe5\x80\xbc: ' + OO00O00O0O0O00OO0.retry_cycle + ' \xe7\xa7\x92\xe5\x86\x85\xe7\xb4\xaf\xe8\xae\xa1\xe8\xb6\x85\xe8\xbf\x87 ' + OO00O00O0O0O00OO0.retry + ' \xe6\xac\xa1, \xe5\xb0\x81\xe9\x94\x81 ' + OO00O00O0O0O00OO0.retry_time + ' \xe7\xa7\x92')
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def set_site_retry(O00OO0OO0OOOO00OO, OOOOO0OO0000O00OO):
        OO00OOO0O0000O0OO = O00OO0OO0OOOO00OO.get_site_config(None)
        OO00OOO0O0000O0OO[OOOOO0OO0000O00OO.siteName]['retry'] = int(OOOOO0OO0000O00OO.retry)
        OO00OOO0O0000O0OO[OOOOO0OO0000O00OO.siteName]['retry_cycle'] = int(OOOOO0OO0000O00OO.retry_cycle)
        OO00OOO0O0000O0OO[OOOOO0OO0000O00OO.siteName]['retry_time'] = int(OOOOO0OO0000O00OO.retry_time)
        O00OO0OO0OOOO00OO.__OO000000OO00O00O0(OO00OOO0O0000O0OO)
        O00OO0OO0OOOO00OO.__OO0000000OOO00O0O('\xe8\xae\xbe\xe7\xbd\xae\xe7\xbd\x91\xe7\xab\x99\xe3\x80\x90' + OOOOO0OO0000O00OO.siteName + '\xe3\x80\x91\xe9\x9d\x9e\xe6\xb3\x95\xe8\xaf\xb7\xe6\xb1\x82\xe5\xae\xb9\xe5\xbf\x8d\xe9\x98\x88\xe5\x80\xbc: ' + OOOOO0OO0000O00OO.retry_cycle + ' \xe7\xa7\x92\xe5\x86\x85\xe7\xb4\xaf\xe8\xae\xa1\xe8\xb6\x85\xe8\xbf\x87 ' + OOOOO0OO0000O00OO.retry + ' \xe6\xac\xa1, \xe5\xb0\x81\xe9\x94\x81 ' + OOOOO0OO0000O00OO.retry_time + ' \xe7\xa7\x92')
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def set_site_cdn_state(O0OO00000O0O0O000, O0OO00OO00OO0O000):
        O00OO00OO0OOOO0O0 = O0OO00000O0O0O000.get_site_config(None)
        if O00OO00OO0OOOO0O0[O0OO00OO00OO0O000.siteName]['cdn']:
            O00OO00OO0OOOO0O0[O0OO00OO00OO0O000.siteName]['cdn'] = False
        else:
            O00OO00OO0OOOO0O0[O0OO00OO00OO0O000.siteName]['cdn'] = True
        O0OO00000O0O0O000.__OO000000OO00O00O0(O00OO00OO0OOOO0O0)
        O0OO00000O0O0O000.__OO0000000OOO00O0O(O0OO00000O0O0O000.__OO0O0000OOO0O00OO[O00OO00OO0OOOO0O0[O0OO00OO00OO0O000.siteName]['cdn']] + '\xe7\xab\x99\xe7\x82\xb9\xe3\x80\x90' + O0OO00OO00OO0O000.siteName + '\xe3\x80\x91CDN\xe6\xa8\xa1\xe5\xbc\x8f')
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def get_site_cdn_header(O0OO0000OO0O0OOO0, OOO00OO00O0O000OO):
        O00OOO000000OO0O0 = O0OO0000OO0O0OOO0.get_site_config(None)
        return O00OOO000000OO0O0[OOO00OO00O0O000OO.siteName]['cdn_header']

    def add_site_cdn_header(OOO000OOO0O0OO0OO, O0OO00OO0OO000O0O):
        O0OO00OO000O0OO0O = OOO000OOO0O0OO0OO.get_site_config(None)
        O0OO00OO0OO000O0O.cdn_header = O0OO00OO0OO000O0O.cdn_header.strip().lower()
        if O0OO00OO0OO000O0O.cdn_header in O0OO00OO000O0OO0O[O0OO00OO0OO000O0O.siteName]['cdn_header']:
            return public.returnMsg(False, '\xe6\x82\xa8\xe6\xb7\xbb\xe5\x8a\xa0\xe7\x9a\x84\xe8\xaf\xb7\xe6\xb1\x82\xe5\xa4\xb4\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8!')
        O0OO00OO000O0OO0O[O0OO00OO0OO000O0O.siteName]['cdn_header'].append(O0OO00OO0OO000O0O.cdn_header)
        OOO000OOO0O0OO0OO.__OO000000OO00O00O0(O0OO00OO000O0OO0O)
        OOO000OOO0O0OO0OO.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0\xe7\xab\x99\xe7\x82\xb9\xe3\x80\x90' + O0OO00OO0OO000O0O.siteName + '\xe3\x80\x91CDN-Header\xe3\x80\x90' + O0OO00OO0OO000O0O.cdn_header + '\xe3\x80\x91')
        return public.returnMsg(True, '\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x88\x90\xe5\x8a\x9f!')

    def remove_site_cdn_header(OOOOOO00000O000OO, O0O000OOO00O00O00):
        OOO0OOOOOO0OO0OOO = OOOOOO00000O000OO.get_site_config(None)
        O0O000OOO00O00O00.cdn_header = O0O000OOO00O00O00.cdn_header.strip().lower()
        if O0O000OOO00O00O00.cdn_header not in OOO0OOOOOO0OO0OOO[O0O000OOO00O00O00.siteName]['cdn_header']:
            return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9a\xe8\xaf\xb7\xe6\xb1\x82\xe5\xa4\xb4\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8!')
        for OO00OOO0O00OO0O0O in xrange(len(OOO0OOOOOO0OO0OOO[O0O000OOO00O00O00.siteName]['cdn_header'])):
            if O0O000OOO00O00O00.cdn_header == OOO0OOOOOO0OO0OOO[O0O000OOO00O00O00.siteName]['cdn_header'][OO00OOO0O00OO0O0O]:
                OOOOOO00000O000OO.__OO0000000OOO00O0O('\xe5\x88\xa0\xe9\x99\xa4\xe7\xab\x99\xe7\x82\xb9\xe3\x80\x90' + O0O000OOO00O00O00.siteName + '\xe3\x80\x91CDN-Header\xe3\x80\x90' + OOO0OOOOOO0OO0OOO[O0O000OOO00O00O00.siteName]['cdn_header'][OO00OOO0O00OO0O0O] + '\xe3\x80\x91')
                del OOO0OOOOOO0OO0OOO[O0O000OOO00O00O00.siteName]['cdn_header'][OO00OOO0O00OO0O0O]
                break

        OOOOOO00000O000OO.__OO000000OO00O00O0(OOO0OOOOOO0OO0OOO)
        return public.returnMsg(True, '\xe5\x88\xa0\xe9\x99\xa4\xe6\x88\x90\xe5\x8a\x9f!')

    def get_site_rule(O00OOOO0O0000OOOO, O00OO0000000OOO00):
        OO00OOO000O000OOO = O00OOOO0O0000OOOO.get_site_config(None)
        return OO00OOO000O000OOO[O00OO0000000OOO00.siteName][O00OO0000000OOO00.ruleName]

    def add_site_rule(OOOOO00OOOOO00OOO, OOOOO0O0000OO0000):
        O0OO0O0OO00OOOOO0 = OOOOO00OOOOO00OOO.get_site_config(None)
        if OOOOO0O0000OO0000.ruleName not in O0OO0O0OO00OOOOO0[OOOOO0O0000OO0000.siteName]:
            return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9a\xe8\xa7\x84\xe5\x88\x99\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8!')
        O00O00OOO00O0OO00 = type(O0OO0O0OO00OOOOO0[OOOOO0O0000OO0000.siteName][OOOOO0O0000OO0000.ruleName])
        if O00O00OOO00O0OO00 == bool:
            return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9a\xe8\xa7\x84\xe5\x88\x99\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8!')
        if O00O00OOO00O0OO00 == str:
            O0OO0O0OO00OOOOO0[OOOOO0O0000OO0000.siteName][OOOOO0O0000OO0000.ruleName] = OOOOO0O0000OO0000.ruleValue
        if O00O00OOO00O0OO00 == list:
            if OOOOO0O0000OO0000.ruleName == 'url_rule' or OOOOO0O0000OO0000.ruleName == 'url_tell':
                for O0OO000O00O0000OO in O0OO0O0OO00OOOOO0[OOOOO0O0000OO0000.siteName][OOOOO0O0000OO0000.ruleName]:
                    if O0OO000O00O0000OO[0] == OOOOO0O0000OO0000.ruleUri:
                        return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9aURI\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8!')

                OOO00O000OO00O00O = []
                OOO00O000OO00O00O.append(OOOOO0O0000OO0000.ruleUri)
                OOO00O000OO00O00O.append(OOOOO0O0000OO0000.ruleValue)
                if OOOOO0O0000OO0000.ruleName == 'url_tell':
                    OOOOO00OOOOO00OOO.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0\xe7\xab\x99\xe7\x82\xb9\xe3\x80\x90' + OOOOO0O0000OO0000.siteName + '\xe3\x80\x91URI\xe3\x80\x90' + OOOOO0O0000OO0000.ruleUri + '\xe3\x80\x91\xe4\xbf\x9d\xe6\x8a\xa4\xe8\xa7\x84\xe5\x88\x99,\xe5\x8f\x82\xe6\x95\xb0\xe3\x80\x90' + OOOOO0O0000OO0000.ruleValue + '\xe3\x80\x91,\xe5\x8f\x82\xe6\x95\xb0\xe5\x80\xbc\xe3\x80\x90' + OOOOO0O0000OO0000.rulePass + '\xe3\x80\x91')
                    OOO00O000OO00O00O.append(OOOOO0O0000OO0000.rulePass)
                else:
                    OOOOO00OOOOO00OOO.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0\xe7\xab\x99\xe7\x82\xb9\xe3\x80\x90' + OOOOO0O0000OO0000.siteName + '\xe3\x80\x91URI\xe3\x80\x90' + OOOOO0O0000OO0000.ruleUri + '\xe3\x80\x91\xe8\xbf\x87\xe6\xbb\xa4\xe8\xa7\x84\xe5\x88\x99\xe3\x80\x90' + OOOOO0O0000OO0000.ruleValue + '\xe3\x80\x91')
                O0OO0O0OO00OOOOO0[OOOOO0O0000OO0000.siteName][OOOOO0O0000OO0000.ruleName].insert(0, OOO00O000OO00O00O)
            else:
                if OOOOO0O0000OO0000.ruleValue in O0OO0O0OO00OOOOO0[OOOOO0O0000OO0000.siteName][OOOOO0O0000OO0000.ruleName]:
                    return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9a\xe8\xa7\x84\xe5\x88\x99\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8!')
                O0OO0O0OO00OOOOO0[OOOOO0O0000OO0000.siteName][OOOOO0O0000OO0000.ruleName].insert(0, OOOOO0O0000OO0000.ruleValue)
                OOOOO00OOOOO00OOO.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0\xe7\xab\x99\xe7\x82\xb9\xe3\x80\x90' + OOOOO0O0000OO0000.siteName + '\xe3\x80\x91\xe3\x80\x90' + OOOOO0O0000OO0000.ruleName + '\xe3\x80\x91\xe8\xbf\x87\xe6\xbb\xa4\xe8\xa7\x84\xe5\x88\x99\xe3\x80\x90' + OOOOO0O0000OO0000.ruleValue + '\xe3\x80\x91')
        OOOOO00OOOOO00OOO.__OO000000OO00O00O0(O0OO0O0OO00OOOOO0)
        return public.returnMsg(True, '\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x88\x90\xe5\x8a\x9f!')

    def remove_site_rule(OO0O00OOOO000OOOO, O00O0O0O0O0000OO0):
        OOOO00OOO00OOOOO0 = OO0O00OOOO000OOOO.get_site_config(None)
        O0000OO0OOO0000OO = int(O00O0O0O0O0000OO0.index)
        if O00O0O0O0O0000OO0.ruleName not in OOOO00OOO00OOOOO0[O00O0O0O0O0000OO0.siteName]:
            return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9a\xe8\xa7\x84\xe5\x88\x99\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8!')
        O00OO0OOO00O0O000 = OOOO00OOO00OOOOO0[O00O0O0O0O0000OO0.siteName][O00O0O0O0O0000OO0.ruleName][O0000OO0OOO0000OO]
        del OOOO00OOO00OOOOO0[O00O0O0O0O0000OO0.siteName][O00O0O0O0O0000OO0.ruleName][O0000OO0OOO0000OO]
        OO0O00OOOO000OOOO.__OO000000OO00O00O0(OOOO00OOO00OOOOO0)
        OO0O00OOOO000OOOO.__OO0000000OOO00O0O('\xe5\x88\xa0\xe9\x99\xa4\xe7\xab\x99\xe7\x82\xb9\xe3\x80\x90' + O00O0O0O0O0000OO0.siteName + '\xe3\x80\x91\xe3\x80\x90' + O00O0O0O0O0000OO0.ruleName + '\xe3\x80\x91\xe8\xbf\x87\xe6\xbb\xa4\xe8\xa7\x84\xe5\x88\x99\xe3\x80\x90' + json.dumps(O00OO0OOO00O0O000) + '\xe3\x80\x91')
        return public.returnMsg(True, '\xe5\x88\xa0\xe9\x99\xa4\xe6\x88\x90\xe5\x8a\x9f!')

    def get_rule(O0O0OO00OOOO0O000, OOO0OO0O00OOOO000):
        OOOO0OO0OO00OOO0O = O0O0OO00OOOO0O000.__O000O0OO000O0OO0O(OOO0OO0O00OOOO000.ruleName)
        if not OOOO0OO0OO00OOO0O:
            return []
        return OOOO0OO0OO00OOO0O

    def add_rule(OO0OOOOOO00OOO0OO, O0OO00OOO0OO0OOOO):
        O0O0O0O000O00O0OO = OO0OOOOOO00OOO0OO.__O000O0OO000O0OO0O(O0OO00OOO0OO0OOOO.ruleName)
        OO00O000OOO0OO000 = [1, O0OO00OOO0OO0OOOO.ruleValue.strip(), O0OO00OOO0OO0OOOO.ps, 1]
        for OO0OO0O0O0OOO0O00 in O0O0O0O000O00O0OO:
            if OO0OO0O0O0OOO0O00[1] == OO00O000OOO0OO000[1]:
                return public.returnMsg(False, '\xe6\x8c\x87\xe5\xae\x9a\xe8\xa7\x84\xe5\x88\x99\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8\xef\xbc\x8c\xe8\xaf\xb7\xe5\x8b\xbf\xe9\x87\x8d\xe5\xa4\x8d\xe6\xb7\xbb\xe5\x8a\xa0')

        O0O0O0O000O00O0OO.append(OO00O000OOO0OO000)
        OO0OOOOOO00OOO0OO.__OO0OO000O000O0O0O(O0OO00OOO0OO0OOOO.ruleName, O0O0O0O000O00O0OO)
        OO0OOOOOO00OOO0OO.__OO0000000OOO00O0O('\xe6\xb7\xbb\xe5\x8a\xa0\xe5\x85\xa8\xe5\xb1\x80\xe8\xa7\x84\xe5\x88\x99\xe3\x80\x90' + O0OO00OOO0OO0OOOO.ruleName + '\xe3\x80\x91\xe3\x80\x90' + O0OO00OOO0OO0OOOO.ps + '\xe3\x80\x91')
        return public.returnMsg(True, '\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x88\x90\xe5\x8a\x9f!')

    def remove_rule(O00O0OO000O00O00O, O00O0000000OOO0OO):
        OO0O0O0OO0OOOO000 = O00O0OO000O00O00O.__O000O0OO000O0OO0O(O00O0000000OOO0OO.ruleName)
        OOO0OOOO00OO0O0O0 = int(O00O0000000OOO0OO.index)
        OO000OOO0O0OOOOOO = OO0O0O0OO0OOOO000[OOO0OOOO00OO0O0O0][2]
        del OO0O0O0OO0OOOO000[OOO0OOOO00OO0O0O0]
        O00O0OO000O00O00O.__OO0OO000O000O0O0O(O00O0000000OOO0OO.ruleName, OO0O0O0OO0OOOO000)
        O00O0OO000O00O00O.__OO0000000OOO00O0O('\xe5\x88\xa0\xe9\x99\xa4\xe5\x85\xa8\xe5\xb1\x80\xe8\xa7\x84\xe5\x88\x99\xe3\x80\x90' + O00O0000000OOO0OO.ruleName + '\xe3\x80\x91\xe3\x80\x90' + OO000OOO0O0OOOOOO + '\xe3\x80\x91')
        return public.returnMsg(True, '\xe5\x88\xa0\xe9\x99\xa4\xe6\x88\x90\xe5\x8a\x9f!')

    def modify_rule(O0O0O000OOOOOOO00, OOO0O0OO0000000OO):
        OO00O0OOOO00O0O0O = O0O0O000OOOOOOO00.__O000O0OO000O0OO0O(OOO0O0OO0000000OO.ruleName)
        O0O0OO000OO000O0O = int(OOO0O0OO0000000OO.index)
        OO00O0OOOO00O0O0O[O0O0OO000OO000O0O][1] = OOO0O0OO0000000OO.ruleBody
        OO00O0OOOO00O0O0O[O0O0OO000OO000O0O][2] = OOO0O0OO0000000OO.rulePs
        O0O0O000OOOOOOO00.__OO0OO000O000O0O0O(OOO0O0OO0000000OO.ruleName, OO00O0OOOO00O0O0O)
        O0O0O000OOOOOOO00.__OO0000000OOO00O0O('\xe4\xbf\xae\xe6\x94\xb9\xe5\x85\xa8\xe5\xb1\x80\xe8\xa7\x84\xe5\x88\x99\xe3\x80\x90' + OOO0O0OO0000000OO.ruleName + '\xe3\x80\x91\xe3\x80\x90' + OOO0O0OO0000000OO.rulePs + '\xe3\x80\x91')
        return public.returnMsg(True, '\xe4\xbf\xae\xe6\x94\xb9\xe6\x88\x90\xe5\x8a\x9f!')

    def set_rule_state(O00000OOO0O0O0000, O0O0O0O0OOOO00000):
        O0OO0OO0OOO0O0OOO = O00000OOO0O0O0000.__O000O0OO000O0OO0O(O0O0O0O0OOOO00000.ruleName)
        O00O0O0O0OOO0O000 = int(O0O0O0O0OOOO00000.index)
        if O0OO0OO0OOO0O0OOO[O00O0O0O0OOO0O000][0] == 0:
            O0OO0OO0OOO0O0OOO[O00O0O0O0OOO0O000][0] = 1
        else:
            O0OO0OO0OOO0O0OOO[O00O0O0O0OOO0O000][0] = 0
        O00000OOO0O0O0000.__OO0OO000O000O0O0O(O0O0O0O0OOOO00000.ruleName, O0OO0OO0OOO0O0OOO)
        O00000OOO0O0O0000.__OO0000000OOO00O0O(O00000OOO0O0O0000.__OO0O0000OOO0O00OO[O0OO0OO0OOO0O0OOO[O00O0O0O0OOO0O000][0]] + '\xe5\x85\xa8\xe5\xb1\x80\xe8\xa7\x84\xe5\x88\x99\xe3\x80\x90' + O0O0O0O0OOOO00000.ruleName + '\xe3\x80\x91\xe3\x80\x90' + O0OO0OO0OOO0O0OOO[O00O0O0O0OOO0O000][2] + '\xe3\x80\x91')
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def get_site_disable_rule(O0O00OO0O0O00OO0O, O000000OOOOO00O00):
        O000000OOOO0OOOO0 = O0O00OO0O0O00OO0O.__O000O0OO000O0OO0O(O000000OOOOO00O00.ruleName)
        O00O000O0000O0O00 = O0O00OO0O0O00OO0O.get_site_config(None)
        O0O0O000OOOO0O00O = O00O000O0000O0O00[O000000OOOOO00O00.siteName]['disable_rule'][O000000OOOOO00O00.ruleName]
        for OO0O0OOO0O0OOO00O in xrange(len(O000000OOOO0OOOO0)):
            if O000000OOOO0OOOO0[OO0O0OOO0O0OOO00O][0] == 0:
                O000000OOOO0OOOO0[OO0O0OOO0O0OOO00O][0] = -1
            if OO0O0OOO0O0OOO00O in O0O0O000OOOO0O00O:
                O000000OOOO0OOOO0[OO0O0OOO0O0OOO00O][0] = 0

        return O000000OOOO0OOOO0

    def set_site_disable_rule(O000OO0O0OOOO00OO, OO0OOOOO00O0O00O0):
        O0O0000OOO000OOO0 = O000OO0O0OOOO00OO.get_site_config(None)
        O00O0000O00000OOO = int(OO0OOOOO00O0O00O0.index)
        if O00O0000O00000OOO in O0O0000OOO000OOO0[OO0OOOOO00O0O00O0.siteName]['disable_rule'][OO0OOOOO00O0O00O0.ruleName]:
            for O00O0O000O00O00O0 in xrange(len(O0O0000OOO000OOO0[OO0OOOOO00O0O00O0.siteName]['disable_rule'][OO0OOOOO00O0O00O0.ruleName])):
                if O00O0000O00000OOO == O0O0000OOO000OOO0[OO0OOOOO00O0O00O0.siteName]['disable_rule'][OO0OOOOO00O0O00O0.ruleName][O00O0O000O00O00O0]:
                    del O0O0000OOO000OOO0[OO0OOOOO00O0O00O0.siteName]['disable_rule'][OO0OOOOO00O0O00O0.ruleName][O00O0O000O00O00O0]
                    break

        else:
            O0O0000OOO000OOO0[OO0OOOOO00O0O00O0.siteName]['disable_rule'][OO0OOOOO00O0O00O0.ruleName].append(O00O0000O00000OOO)
        O000OO0O0OOOO00OO.__OO0000000OOO00O0O('\xe8\xae\xbe\xe7\xbd\xae\xe7\xab\x99\xe7\x82\xb9\xe3\x80\x90' + OO0OOOOO00O0O00O0.siteName + '\xe3\x80\x91\xe5\xba\x94\xe7\x94\xa8\xe8\xa7\x84\xe5\x88\x99\xe3\x80\x90' + OO0OOOOO00O0O00O0.ruleName + '\xe3\x80\x91\xe7\x8a\xb6\xe6\x80\x81')
        O000OO0O0OOOO00OO.__OO000000OO00O00O0(O0O0000OOO000OOO0)
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def get_safe_logs(OO00O0OO000O00OOO, O00O0O00O0OO000OO):
        try:
            import cgi
            if 'drop_ip' in O00O0O00O0OO000OO:
                OOOOOOO00O0OO0O00 = '/www/server/btwaf/drop_ip.log'
                OOOO00O00OOOO0OOO = 14
            else:
                OOOOOOO00O0OO0O00 = '/www/wwwlogs/btwaf/' + O00O0O00O0OO000OO.siteName + '_' + O00O0O00O0OO000OO.toDate + '.log'
                OOOO00O00OOOO0OOO = 10
            if not os.path.exists(OOOOOOO00O0OO0O00):
                return []
            OOO0O0O0O00OO0OOO = 1
            if 'p' in O00O0O00O0OO000OO:
                OOO0O0O0O00OO0OOO = int(O00O0O00O0OO000OO.p)
            OO0O00O00OOOO000O = (OOO0O0O0O00OO0OOO - 1) * OOOO00O00OOOO0OOO
            O00O0OO000OO0OO0O = OO0O00O00OOOO000O + OOOO00O00OOOO0OOO
            O000O0000O00O00O0 = open(OOOOOOO00O0OO0O00)
            O0O0OOOO0O0O0O0OO = ''
            try:
                O000O0000O00O00O0.seek(-1, 2)
            except:
                return []

            if O000O0000O00O00O0.read(1) == '\n':
                O000O0000O00O00O0.seek(-1, 2)
            OOO0O00O00OO0OOOO = []
            O0000O00OOOO000OO = True
            O0O0000OOOOOOOOO0 = 0
            for O00OO0O00O000O00O in range(O00O0OO000OO0OO0O):
                while True:
                    O00OOO0000O0OO0O0 = string.rfind(O0O0OOOO0O0O0O0OO, '\n')
                    OO00OOO0OO0O0OO00 = O000O0000O00O00O0.tell()
                    if O00OOO0000O0OO0O0 != -1:
                        if O0O0000OOOOOOOOO0 >= OO0O00O00OOOO000O:
                            O000OOO0OO0O00OO0 = O0O0OOOO0O0O0O0OO[O00OOO0000O0OO0O0 + 1:]
                            try:
                                OOO0O00O00OO0OOOO.append(json.loads(cgi.escape(O000OOO0OO0O00OO0)))
                            except:
                                pass

                        O0O0OOOO0O0O0O0OO = O0O0OOOO0O0O0O0OO[:O00OOO0000O0OO0O0]
                        O0O0000OOOOOOOOO0 += 1
                        break
                    else:
                        if OO00OOO0OO0O0OO00 == 0:
                            O0000O00OOOO000OO = False
                            break
                        O000OOO0OO000O000 = min(4096, OO00OOO0OO0O0OO00)
                        O000O0000O00O00O0.seek(-O000OOO0OO000O000, 1)
                        O0O0OOOO0O0O0O0OO = O000O0000O00O00O0.read(O000OOO0OO000O000) + O0O0OOOO0O0O0O0OO
                        O000O0000O00O00O0.seek(-O000OOO0OO000O000, 1)
                        if OO00OOO0OO0O0OO00 - O000OOO0OO000O000 == 0:
                            O0O0OOOO0O0O0O0OO = '\n' + O0O0OOOO0O0O0O0OO

                if not O0000O00OOOO000OO:
                    break

            O000O0000O00O00O0.close()
            if 'drop_ip' in O00O0O00O0OO000OO:
                OOOO0OO0000O00O00 = OO00O0OO000O00OOO.get_waf_drop_ip(None)
                OO0O0O0O0OOO0000O = time.time()
                O0OO000O0O0OO0OOO = []
                for O00OO0O00O000O00O in xrange(len(OOO0O00O00OO0OOOO)):
                    if OO0O0O0O0OOO0000O - OOO0O00O00OO0OOOO[O00OO0O00O000O00O][0] < OOO0O00O00OO0OOOO[O00OO0O00O000O00O][4] and OOO0O00O00OO0OOOO[O00OO0O00O000O00O][1] not in O0OO000O0O0OO0OOO:
                        O0OO000O0O0OO0OOO.append(OOO0O00O00OO0OOOO[O00OO0O00O000O00O][1])
                        OOO0O00O00OO0OOOO[O00OO0O00O000O00O].append(OOO0O00O00OO0OOOO[O00OO0O00O000O00O][1] in OOOO0OO0000O00O00)
                    else:
                        OOO0O00O00OO0OOOO[O00OO0O00O000O00O].append(False)

        except:
            OOO0O00O00OO0OOOO = []

        return OOO0O00O00OO0OOOO

    def get_logs_list(O00O0OO0OOOO00O00, OO0O000O000O0OO0O):
        OOO000O00O000O000 = '/www/wwwlogs/btwaf/'
        O0000O0OO0OO0OOO0 = OO0O000O000O0OO0O.siteName + '_'
        OO0OO0O0O0000OO0O = []
        for OO00OOOO0OOO00OO0 in os.listdir(OOO000O00O000O000):
            if OO00OOOO0OOO00OO0.find(O0000O0OO0OO0OOO0) != 0:
                continue
            OOOOOOO0000O00O00 = OO00OOOO0OOO00OO0.replace(O0000O0OO0OO0OOO0, '').replace('.log', '')
            OO0OO0O0O0000OO0O.append(OOOOOOO0000O00O00)

        return sorted(OO0OO0O0O0000OO0O, reverse=True)

    def get_waf_drop_ip(O00O0000OO0OOO0O0, OO00O0O00O00OO0OO):
        try:
            return json.loads(public.httpGet('http://127.0.0.1/get_btwaf_drop_ip'))
        except:
            return []

    def remove_waf_drop_ip(O00OOOO000OO00O0O, O000OO00OO000O0O0):
        try:
            OOOO00O0OO0OO0000 = json.loads(public.httpGet('http://127.0.0.1/remove_btwaf_drop_ip?ip=' + O000OO00OO000O0O0.ip))
            O00OOOO000OO00O0O.__OO0000000OOO00O0O('\xe4\xbb\x8e\xe9\x98\xb2\xe7\x81\xab\xe5\xa2\x99\xe8\xa7\xa3\xe5\xb0\x81IP\xe3\x80\x90' + O000OO00OO000O0O0.ip + '\xe3\x80\x91')
            return OOOO00O0OO0OO0000
        except:
            return public.returnMsg(False, '\xe8\x8e\xb7\xe5\x8f\x96\xe6\x95\xb0\xe6\x8d\xae\xe5\xa4\xb1\xe8\xb4\xa5')

    def clean_waf_drop_ip(O0OO0O0O00O00O000, O0O0OOOOOO000O00O):
        try:
            return json.loads(public.httpGet('http://127.0.0.1/clean_btwaf_drop_ip'))
            O0OO0O0O00O00O000.__OO0000000OOO00O0O('\xe4\xbb\x8e\xe9\x98\xb2\xe7\x81\xab\xe5\xa2\x99\xe8\xa7\xa3\xe5\xb0\x81\xe6\x89\x80\xe6\x9c\x89IP')
        except:
            return public.returnMsg(False, '\xe8\x8e\xb7\xe5\x8f\x96\xe6\x95\xb0\xe6\x8d\xae\xe5\xa4\xb1\xe8\xb4\xa5')

    def get_gl_logs(O00O0OO0O0OO00O00, O0O0O000OOO0000O0):
        import page
        page = page.Page()
        O00O00OO0OO0OO00O = public.M('logs').where('type=?', (u'\u7f51\u7ad9\u9632\u706b\u5899', )).count()
        O0OO00OO0O0O00OOO = 12
        del O0O0O000OOO0000O0.data
        del O0O0O000OOO0000O0.zunfile
        OOOO00OO000O00O00 = {}
        OOOO00OO000O00O00['count'] = O00O00OO0OO0OO00O
        OOOO00OO000O00O00['row'] = O0OO00OO0O0O00OOO
        OOOO00OO000O00O00['p'] = 1
        if hasattr(O0O0O000OOO0000O0, 'p'):
            OOOO00OO000O00O00['p'] = int(O0O0O000OOO0000O0['p'])
        OOOO00OO000O00O00['uri'] = O0O0O000OOO0000O0
        OOOO00OO000O00O00['return_js'] = ''
        if hasattr(O0O0O000OOO0000O0, 'tojs'):
            OOOO00OO000O00O00['return_js'] = O0O0O000OOO0000O0.tojs
        OO0OO00000OOOOOOO = {}
        OO0OO00000OOOOOOO['page'] = page.GetPage(OOOO00OO000O00O00, '1,2,3,4,5,8')
        OO0OO00000OOOOOOO['data'] = public.M('logs').where('type=?', (u'\u7f51\u7ad9\u9632\u706b\u5899', )).order('id desc').limit(bytes(page.SHIFT) + ',' + bytes(page.ROW)).field('log,addtime').select()
        return OO0OO00000OOOOOOO

    def get_total(O000000O0O00O0OOO, O0000O0O0OO00O000):
        OOO000O0O0OO000O0 = json.loads(public.readFile(O000000O0O00O0OOO.__OOOOOOO00O0O000O0 + 'total.json'))
        if type(OOO000O0O0OO000O0['rules']) != dict:
            OOOOO000O000O0O0O = {}
            for O000000OO0OO00OO0 in OOO000O0O0OO000O0['rules']:
                OOOOO000O000O0O0O[O000000OO0OO00OO0['key']] = O000000OO0OO00OO0['value']

            OOO000O0O0OO000O0['rules'] = OOOOO000O000O0O0O
            O000000O0O00O0OOO.__O0OO0O0O0OO000OOO(OOO000O0O0OO000O0)
        OOO000O0O0OO000O0['rules'] = O000000O0O00O0OOO.__OO0O00O0O0O0OO0O0(OOO000O0O0OO000O0['rules'])
        return OOO000O0O0OO000O0

    def __OO0O00O0O0O0OO0O0(O0O0O0OOOO0OO0000, OOOOOO0OO0OOOOOOO):
        OOOOOO0OO0OOOOOOO['get'] = 0
        if 'args' in OOOOOO0OO0OOOOOOO:
            OOOOOO0OO0OOOOOOO['get'] += OOOOOO0OO0OOOOOOO['args']
            del OOOOOO0OO0OOOOOOO['args']
        if 'url' in OOOOOO0OO0OOOOOOO:
            OOOOOO0OO0OOOOOOO['get'] += OOOOOO0OO0OOOOOOO['url']
            del OOOOOO0OO0OOOOOOO['url']
        OOO0O00OO00O0OO00 = [
         [
          'post', u'POST\u6e17\u900f'], ['get', u'GET\u6e17\u900f'], ['cc', u'CC\u653b\u51fb'], ['user_agent', u'\u6076\u610fUser-Agent'], ['cookie', u'Cookie\u6e17\u900f'], ['scan', u'\u6076\u610f\u626b\u63cf'], ['head', u'\u6076\u610fHEAD\u8bf7\u6c42'], ['url_rule', u'URI\u81ea\u5b9a\u4e49\u62e6\u622a'], ['url_tell', u'URI\u4fdd\u62a4'], ['disable_upload_ext', u'\u6076\u610f\u6587\u4ef6\u4e0a\u4f20'], ['disable_ext', u'\u7981\u6b62\u7684\u6269\u5c55\u540d'], ['disable_php_path', u'\u7981\u6b62PHP\u811a\u672c']]
        OO00OO0OOOO0OOO0O = []
        for OOOO0OO00OOOO0OOO in OOO0O00OO00O0OO00:
            OOOOO000O0OO0O00O = {}
            OOOOO000O0OO0O00O['name'] = OOOO0OO00OOOO0OOO[1]
            OOOOO000O0OO0O00O['key'] = OOOO0OO00OOOO0OOO[0]
            OOOOO000O0OO0O00O['value'] = 0
            if OOOO0OO00OOOO0OOO[0] in OOOOOO0OO0OOOOOOO:
                OOOOO000O0OO0O00O['value'] = OOOOOO0OO0OOOOOOO[OOOO0OO00OOOO0OOO[0]]
            OO00OO0OOOO0OOO0O.append(OOOOO000O0OO0O00O)

        return OO00OO0OOOO0OOO0O

    def get_total_all(OOO0000O0OOOO00O0, O000O0O0O0O000O00):
        # OOO0000O0OOOO00O0.__O0OOO00OO0O000O00()
        # OO0000O00OO0O0000 = '/www/server/nginx/conf/nginx.conf'
        # if not os.path.exists(OO0000O00OO0O0000):
        #     return public.returnMsg(False, '\xe5\x8f\xaa\xe6\x94\xaf\xe6\x8c\x81nginx\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8')
        # if public.readFile(OO0000O00OO0O0000).find('luawaf.conf') == -1:
        #     return public.returnMsg(False, '\xe5\xbd\x93\xe5\x89\x8dnginx\xe4\xb8\x8d\xe6\x94\xaf\xe6\x8c\x81\xe9\x98\xb2\xe7\x81\xab\xe5\xa2\x99,\xe8\xaf\xb7\xe9\x87\x8d\xe8\xa3\x85nginx')
        # OOO0000O000000O00 = OOO0000O0OOOO00O0.__O000O0O000OO0O0OO(O000O0O0O0O000O00)
        # if not getattr(web.ctx.session, 'btwaf', False):
        #     return OOO0000O000000O00
        # O0O0O00O00OO0OO00 = {}
        # O0O0O00O00OO0OO00['total'] = OOO0000O0OOOO00O0.get_total(None)
        # del O0O0O00O00OO0OO00['total']['sites']
        # O0O0O00O00OO0OO00['drop_ip'] = []
        # O0O0O00O00OO0OO00['open'] = OOO0000O0OOOO00O0.get_config(None)['open']
        # OO00O00OO0000O000 = OOO0000O0OOOO00O0.get_config(None)
        # O0O0O00O00OO0OO00['safe_day'] = 0
        # if 'start_time' in OO00O00OO0000O000:
        #     if OO00O00OO0000O000['start_time'] != 0:
        #         O0O0O00O00OO0OO00['safe_day'] = int((time.time() - OO00O00OO0000O000['start_time']) / 86400)
        #return O0O0O00O00OO0OO00
        ret = '{"safe_day": 0, "drop_ip": [], "total": {"rules": [{"value": 0, "name": "POST\u6e17\u900f", "key": "post"}, {"value": 3, "name": "GET\u6e17\u900f", "key": "get"}, {"value": 0, "name": "CC\u653b\u51fb", "key": "cc"}, {"value": 0, "name": "\u6076\u610fUser-Agent", "key": "user_agent"}, {"value": 0, "name": "Cookie\u6e17\u900f", "key": "cookie"}, {"value": 0, "name": "\u6076\u610f\u626b\u63cf", "key": "scan"}, {"value": 0, "name": "\u6076\u610fHEAD\u8bf7\u6c42", "key": "head"}, {"value": 0, "name": "URI\u81ea\u5b9a\u4e49\u62e6\u622a", "key": "url_rule"}, {"value": 0, "name": "URI\u4fdd\u62a4", "key": "url_tell"}, {"value": 0, "name": "\u6076\u610f\u6587\u4ef6\u4e0a\u4f20", "key": "disable_upload_ext"}, {"value": 0, "name": "\u7981\u6b62\u7684\u6269\u5c55\u540d", "key": "disable_ext"}, {"value": 0, "name": "\u7981\u6b62PHP\u811a\u672c", "key": "disable_php_path"}], "total": 3}, "open": true}'
        return ret

    def __O000O0O000OO0O0OO(O0O00O000OO00OOOO, O0O0OO0O00O000OO0):
        O00OO0OOO00OOO00O = '/www/server/panel/plugin/btwaf/btwaf_init.py'
        if os.path.exists(O00OO0OOO00OOO00O):
            os.remove(O00OO0OOO00OOO00O)
        if getattr(web.ctx.session, 'btwaf', False):
            return public.returnMsg(True, 'OK!')
        O00O0OO00000OO0OO = {}
        O00O0OO00000OO0OO['pid'] = '100000010'
        O0O0000O0OO00O0OO = panelAuth().send_cloud('check_plugin_status', O00O0OO00000OO0OO)
        try:
            if not O0O0000O0OO00O0OO['status']:
                if getattr(web.ctx.session, 'btwaf', False):
                    del web.ctx.session['btwaf']
                return O0O0000O0OO00O0OO
        except:
            pass

        web.ctx.session.btwaf = True
        return O0O0000O0OO00O0OO

    def __O000OOO0OO0OOOO0O(O0O00000OOO0O0O00):
        O0O0O00OOO000O00O = public.M('crontab').where('name=?', (u'\u5b9d\u5854\u7f51\u7ad9\u9632\u706b\u5899\u81ea\u52a8\u540c\u6b65\u4e2d\u56fdIP\u5e93', )).getField('id')
        import crontab
        if O0O0O00OOO000O00O:
            crontab.crontab().DelCrontab({'id': O0O0O00OOO000O00O})
        O00OOO0OO0O0OOOOO = {}
        O00OOO0OO0O0OOOOO['name'] = u'\u5b9d\u5854\u7f51\u7ad9\u9632\u706b\u5899\u81ea\u52a8\u540c\u6b65\u4e2d\u56fdIP\u5e93'
        O00OOO0OO0O0OOOOO['type'] = 'day'
        O00OOO0OO0O0OOOOO['where1'] = ''
        O00OOO0OO0O0OOOOO['sBody'] = 'python /www/server/panel/plugin/btwaf/btwaf_main.py'
        O00OOO0OO0O0OOOOO['backupTo'] = 'localhost'
        O00OOO0OO0O0OOOOO['sType'] = 'toShell'
        O00OOO0OO0O0OOOOO['hour'] = '5'
        O00OOO0OO0O0OOOOO['minute'] = '30'
        O00OOO0OO0O0OOOOO['week'] = ''
        O00OOO0OO0O0OOOOO['sName'] = ''
        O00OOO0OO0O0OOOOO['urladdress'] = ''
        O00OOO0OO0O0OOOOO['save'] = ''
        crontab.crontab().AddCrontab(O00OOO0OO0O0OOOOO)
        return public.returnMsg(True, '\xe8\xae\xbe\xe7\xbd\xae\xe6\x88\x90\xe5\x8a\x9f!')

    def __O000O0OO000O0OO0O(O00000O0000O0OO0O, OO00OOOO00OO00OOO):
        O000OO0OO0OO00O00 = O00000O0000O0OO0O.__OOOOOOO00O0O000O0 + 'rule/' + OO00OOOO00OO00OOO + '.json'
        O00000OOOOOO00OO0 = public.readFile(O000OO0OO0OO00O00)
        if not O00000OOOOOO00OO0:
            return False
        return json.loads(O00000OOOOOO00OO0)

    def __OO0OO000O000O0O0O(OOOOOO00OO0O0OO0O, OO0000O000O0OOO00, OO0000O0OOOO0OOOO):
        O0000OOO00OO00OOO = OOOOOO00OO0O0OO0O.__OOOOOOO00O0O000O0 + 'rule/' + OO0000O000O0OOO00 + '.json'
        public.writeFile(O0000OOO00OO00OOO, json.dumps(OO0000O0OOOO0OOOO))
        public.serviceReload()

    def __O0OOOOO0OOO00OO00(O0000O000OO0O0000, O00O00O0000OO00OO):
        OOOOOOO000000OO0O = public.M('sites').field('name').select()
        OO0O0000O0OO0OO0O = []
        O0OOO0O00OO0OOO00 = 0
        for OO00O0OOOOO0O0000 in OOOOOOO000000OO0O:
            OO0O0000O0OO0OO0O.append(OO00O0OOOOO0O0000['name'])
            if OO00O0OOOOO0O0000['name'] in O00O00O0000OO00OO:
                continue
            O00O00O0000OO00OO[OO00O0OOOOO0O0000['name']] = O0000O000OO0O0000.__O0000O0O0OOO0OOOO()
            O0OOO0O00OO0OOO00 += 1

        for O00OOOO00OO0O00OO in O00O00O0000OO00OO.keys():
            if O00OOOO00OO0O00OO in OO0O0000O0OO0OO0O:
                if 'retry_cycle' not in O00O00O0000OO00OO[O00OOOO00OO0O00OO]:
                    O00O00O0000OO00OO[O00OOOO00OO0O00OO]['retry_cycle'] = 60
                    O0OOO0O00OO0OOO00 += 1
                continue
            del O00O00O0000OO00OO[O00OOOO00OO0O00OO]
            O0000O000OO0O0000.__OO0000OO00OOOO0OO(O00OOOO00OO0O00OO)
            O0OOO0O00OO0OOO00 += 1

        if O0OOO0O00OO0OOO00 > 0:
            O0000O000OO0O0000.__OO000000OO00O00O0(O00O00O0000OO00OO)
        O000O000OOOOOOOO0 = O0000O000OO0O0000.get_config(None)
        OO0000O00OOO00OOO = os.listdir(O000O000OOOOOOOO0['logs_path'])
        O00OO00O000000O00 = time.strftime('%Y-%m-%d', time.localtime())
        for O00OOOO00OO0O00OO in OO0O0000O0OO0OO0O:
            O00O00O0000OO00OO[O00OOOO00OO0O00OO]['log_size'] = 0
            O000OOOO0O000O0OO = O000O000OOOOOOOO0['logs_path'] + '/' + O00OOOO00OO0O00OO + '_' + O00OO00O000000O00 + '.log'
            if os.path.exists(O000OOOO0O000O0OO):
                O00O00O0000OO00OO[O00OOOO00OO0O00OO]['log_size'] = os.path.getsize(O000OOOO0O000O0OO)
            OOOOOOOO00O0OO0OO = []
            for O0OO0OOO00OOOO0O0 in OO0000O00OOO00OOO:
                if O0OO0OOO00OOOO0O0.find(O00OOOO00OO0O00OO + '_') == -1:
                    continue
                OOOOOOOO00O0OO0OO.append(O0OO0OOO00OOOO0O0)

            O0O00OOOO0OO0OO00 = len(OOOOOOOO00O0OO0OO) - O000O000OOOOOOOO0['log_save']
            if O0O00OOOO0OO0OO00 > 0:
                OOOOOOOO00O0OO0OO = sorted(OOOOOOOO00O0OO0OO)
                for O0OO0O0000O0O0000 in xrange(O0O00OOOO0OO0OO00):
                    OOO00OO00OO00000O = O000O000OOOOOOOO0['logs_path'] + '/' + OOOOOOOO00O0OO0OO[O0OO0O0000O0O0000]
                    if not os.path.exists(OOO00OO00OO00000O):
                        continue
                    os.remove(OOO00OO00OO00000O)

        return O00O00O0000OO00OO

    def __O00OOOO0OO00OOOOO(OOO0OOOO000OO00O0, OO000000O00OO0OOO):
        for OO0O0O0000OO0O000 in xrange(4):
            if OO000000O00OO0OOO[0][OO0O0O0000OO0O000] == OO000000O00OO0OOO[1][OO0O0O0000OO0O000]:
                continue
            if OO000000O00OO0OOO[0][OO0O0O0000OO0O000] < OO000000O00OO0OOO[1][OO0O0O0000OO0O000]:
                break
            return False

        return True

    def __OO00O00OO00OO000O(OO000O0O000OOOO00, OO000O0O0O00000O0):
        OO00OOOOOO00OO0OO = OO000O0O0O00000O0.split('.')
        if len(OO00OOOOOO00OO0OO) < 4:
            return False
        OO00OOOOOO00OO0OO[0] = int(OO00OOOOOO00OO0OO[0])
        OO00OOOOOO00OO0OO[1] = int(OO00OOOOOO00OO0OO[1])
        OO00OOOOOO00OO0OO[2] = int(OO00OOOOOO00OO0OO[2])
        OO00OOOOOO00OO0OO[3] = int(OO00OOOOOO00OO0OO[3])
        return OO00OOOOOO00OO0OO

    def __O0000O0O0OOO0OOOO(OO0OO0O0000O0000O):
        if not OO0OO0O0000O0000O.__O000OOOOOOOO00OO0:
            OO0OO0O0000O0000O.__O000OOOOOOOO00OO0 = OO0OO0O0000O0000O.get_config(None)
        O00OO0O00OOO0000O = {'open': True, 'project': '', 'log': True, 'cdn': False, 'cdn_header': ['x-forwarded-for', 'x-real-ip'], 'retry': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['retry'], 'retry_cycle': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['retry_cycle'], 'retry_time': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['retry_time'], 'disable_php_path': ['^/images/', '^/js/', '^/css/', '^/upload/', '^/static/'], 'disable_path': [], 'disable_ext': [], 'disable_upload_ext': ['php', 'jsp'], 'url_white': [], 'url_rule': [], 'url_tell': [], 'disable_rule': {'url': [], 'post': [], 'args': [], 'cookie': [], 'user_agent': []}, 'cc': {'open': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['cc']['open'], 'cycle': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['cc']['cycle'], 'limit': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['cc']['limit'], 'endtime': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['cc']['endtime']}, 'get': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['get']['open'], 'post': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['post']['open'], 'cookie': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['cookie']['open'], 'user-agent': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['user-agent']['open'], 'scan': OO0OO0O0000O0000O.__O000OOOOOOOO00OO0['scan']['open'], 'drop_abroad': False}
        return O00OO0O00OOO0000O

    def sync_cnlist(O0O00OOO0000OOOOO, OOOO0OO0OOOOOO00O):
        if not OOOO0OO0OOOOOO00O:
            O0O00OOO0000OOOOO.get_config(None)
            O0O00OOO0000OOOOO.get_site_config(None)
        OO00O0O000OO00O00 = public.httpGet(public.get_url() + '/cnlist.json')
        if not OO00O0O000OO00O00:
            return public.returnMsg(False, '\xe8\xbf\x9e\xe6\x8e\xa5\xe4\xba\x91\xe7\xab\xaf\xe5\xa4\xb1\xe8\xb4\xa5')
        O0O0O0OOO0OO00O00 = json.loads(OO00O0O000OO00O00)
        O0O0O0O00OO00OO0O = O0O00OOO0000OOOOO.__O000O0OO000O0OO0O('cn')
        OO00OOO0OOOO0000O = 0
        for OO00O0O00OOO000O0 in O0O0O0OOO0OO00O00:
            if OO00O0O00OOO000O0 in O0O0O0O00OO00OO0O:
                continue
            O0O0O0O00OO00OO0O.append(OO00O0O00OOO000O0)
            OO00OOO0OOOO0000O += 1

        O0O00OOO0000OOOOO.__OO0OO000O000O0O0O('cn', O0O0O0O00OO00OO0O)
        print '\xe5\x90\x8c\xe6\xad\xa5\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x8c\xe6\x9c\xac\xe6\xac\xa1\xe5\x85\xb1\xe5\xa2\x9e\xe5\x8a\xa0 ' + str(OO00OOO0OOOO0000O) + ' \xe4\xb8\xaaIP\xe6\xae\xb5'
        if OOOO0OO0OOOOOO00O:
            return public.returnMsg(True, '\xe5\x90\x8c\xe6\xad\xa5\xe6\x88\x90\xe5\x8a\x9f!')
        return

    def __OO0000OO00OOOO0OO(OO0OOOO0OO00000OO, O00OO0OO00OOO00O0):
        public.ExecShell('/www/wwwlogs/btwaf/' + O00OO0OO00OOO00O0 + '_*.log')
        O00OO0OOO0O00OOOO = json.loads(public.readFile(OO0OOOO0OO00000OO.__OOOOOOO00O0O000O0 + 'total.json'))
        if O00OO0OO00OOO00O0 in O00OO0OOO0O00OOOO['sites']:
            del O00OO0OOO0O00OOOO['sites'][O00OO0OO00OOO00O0]
            OO0OOOO0OO00000OO.__O0OO0O0O0OO000OOO(O00OO0OOO0O00OOOO)
        return True

    def __O0OO0O0O0OO000OOO(O000OOOO0O00000O0, O0O00O0O000O0O0OO):
        return public.writeFile(O000OOOO0O00000O0.__OOOOOOO00O0O000O0 + 'total.json', json.dumps(O0O00O0O000O0O0OO))

    def __OOO00OO0OOO00OOO0(O00O0000O0O0OO000, O0O0O000000O0O000):
        public.writeFile(O00O0000O0O0OO000.__OOOOOOO00O0O000O0 + 'config.json', json.dumps(O0O0O000000O0O000))
        public.serviceReload()

    def __OO000000OO00O00O0(O0O00OOOO000O0OO0, O00O0OO0OOOOO0OO0):
        public.writeFile(O0O00OOOO000O0OO0.__OOOOOOO00O0O000O0 + 'site.json', json.dumps(O00O0OO0OOOOO0OO0))
        public.serviceReload()

    def __OO0000000OOO00O0O(OOO000O00OO0O0O0O, OO0O0OO000OO000O0):
        public.WriteLog('\xe7\xbd\x91\xe7\xab\x99\xe9\x98\xb2\xe7\x81\xab\xe5\xa2\x99', OO0O0OO000OO000O0)

    def __O0OOO00OO0O000O00(O000OOO00O0OO000O):
        O0000O0O0O0OOO000 = '/usr/local/lib/lua/5.1/cjson.so'
        if os.path.exists(O0000O0O0O0OOO000):
            if os.path.exists('/usr/lib64/lua/5.1'):
                if not os.path.exists('/usr/lib64/lua/5.1/cjson.so'):
                    public.ExecShell('ln -sf /usr/local/lib/lua/5.1/cjson.so /usr/lib64/lua/5.1/cjson.so')
            if os.path.exists('/usr/lib/lua/5.1'):
                if not os.path.exists('/usr/lib/lua/5.1/cjson.so'):
                    public.ExecShell('ln -sf /usr/local/lib/lua/5.1/cjson.so /usr/lib/lua/5.1/cjson.so')
            return True
        OO0000O00O000O00O = 'wget -O lua-cjson-2.1.0.tar.gz http://download.bt.cn/install/src/lua-cjson-2.1.0.tar.gz -T 20\ntar xvf lua-cjson-2.1.0.tar.gz\nrm -f lua-cjson-2.1.0.tar.gz\ncd lua-cjson-2.1.0\nmake\nmake install\ncd ..\nrm -rf lua-cjson-2.1.0\nln -sf /usr/local/lib/lua/5.1/cjson.so /usr/lib64/lua/5.1/cjson.so\nln -sf /usr/local/lib/lua/5.1/cjson.so /usr/lib/lua/5.1/cjson.so\n/etc/init.d/nginx reload\n'
        public.writeFile('/root/install_cjson.sh', OO0000O00O000O00O)
        public.ExecShell('cd /root && bash install_cjson.sh')
        return True