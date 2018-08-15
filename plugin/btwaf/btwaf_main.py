#coding: utf-8
# +-------------------------------------------------------------------
# | 宝塔Linux面板
# +-------------------------------------------------------------------
# | Copyright (c) 2015-2099 宝塔软件(http://bt.cn) All rights reserved.
# +-------------------------------------------------------------------
# | Author: 黄文良 <287962566@qq.com>
# +-------------------------------------------------------------------

#+--------------------------------------------------------------------
#|   宝塔网站防火墙
#+--------------------------------------------------------------------
import sys,os;
p_path = '/www/server/panel/plugin/btwaf';
sys.path.append(p_path);
reload(sys);
import btwaf_init;
reload(btwaf_init);

class btwaf_main(btwaf_init.plugin_nginx_init):pass;
        
if __name__ == "__main__":
    os.chdir('/www/server/panel')
    p = btwaf_main();
    p.sync_cnlist(None);
    