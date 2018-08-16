#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
pluginPath=/www/server/panel/plugin/btwaf
dataPath=/www/server/panel/data
install_tmp='/tmp/bt_install.pl'
download_Url='http://download.bt.cn'

Install_btwaf()
{
	Install_cjson
	mkdir -p $pluginPath
	echo '正在安装脚本文件...' > $install_tmp
	cp ./plugin/btwaf/*  $pluginPath/


	cp ./conf/btwaf.conf /www/server/panel/vhost/nginx/


	btwaf_path=/www/server/btwaf
	mkdir -p $btwaf_path/html

	python -m compileall $pluginPath/btwaf_init.py
	
	if [ ! -f $btwaf_path/html/get.html ];then
		cp ./server/btwaf/html/*   $btwaf_path/html/
	fi
	
	mkdir -p $btwaf_path/rule
	if [ ! -f $btwaf_path/rule/url.json ];then
		cp ./server/btwaf/rule/* $btwaf_path/rule/
	fi
	
	if [ ! -f $btwaf_path/site.json ];then
		cp  ./server/btwaf/site.json $btwaf_path/site.json
	fi
	
	if [ ! -f $btwaf_path/config.json ];then
		cp  ./server/btwaf/config.json $btwaf_path/config.json
	fi
	
	if [ ! -f $btwaf_path/total.json ];then
		cp  ./server/btwaf/total.json $btwaf_path/total.json
	fi
	
	if [ ! -f $btwaf_path/drop_ip.log ];then
		\cp -a -r ./server/btwaf/drop_ip.log $btwaf_path/drop_ip.log
	fi
	\cp -a -r ./server/btwaf/init.lua $btwaf_path/init.lua
	\cp -a -r ./server/btwaf/waf.lua $btwaf_path/waf.lua

	chmod +x $btwaf_path/waf.lua
	chmod +x $btwaf_path/init.lua
	
	mkdir -p /www/wwwlogs/btwaf
	chmod 777 /www/wwwlogs/btwaf
	chmod -R 755 /www/server/btwaf
	chmod -R 666 /www/server/btwaf/rule
	chmod -R 666 /www/server/btwaf/total.json
	chmod -R 666 /www/server/btwaf/drop_ip.log
	echo '' > /www/server/nginx/conf/luawaf.conf

	python $pluginPath/btwaf_main.py
	#if [ -f $pluginPath/btwaf_init.pyc ];then
	#	rm -f $pluginPath/btwaf_init.py
	#fi
	cp ./data/* $dataPath/


	/etc/init.d/nginx reload
	echo '安装完成' > $install_tmp
}



Install_cjson()
{
	if [ -f /usr/bin/yum ];then
		isInstall=`rpm -qa |grep lua-devel`
		if [ "$isInstall" == "" ];then
			yum install lua lua-devel -y
		fi
	else
		isInstall=`dpkg -l|grep liblua5.1-0-dev`
		if [ "$isInstall" == "" ];then
			apt-get install lua5.1 lua5.1-dev -y
		fi
	fi
	if [ ! -f /usr/local/lib/lua/5.1/cjson.so ];then
		wget -O lua-cjson-2.1.0.tar.gz $download_Url/install/src/lua-cjson-2.1.0.tar.gz -T 20
		tar xvf lua-cjson-2.1.0.tar.gz
		rm -f lua-cjson-2.1.0.tar.gz
		cd lua-cjson-2.1.0
		make clean
		make
		make install
		cd ..
		rm -rf lua-cjson-2.1.0
		ln -sf /usr/local/lib/lua/5.1/cjson.so /usr/lib64/lua/5.1/cjson.so
		ln -sf /usr/local/lib/lua/5.1/cjson.so /usr/lib/lua/5.1/cjson.so
	else
		if [ -d "/usr/lib64/lua/5.1" ];then
			ln -sf /usr/local/lib/lua/5.1/cjson.so /usr/lib64/lua/5.1/cjson.so
		fi
		
		if [ -d "/usr/lib/lua/5.1" ];then
			ln -sf /usr/local/lib/lua/5.1/cjson.so /usr/lib/lua/5.1/cjson.so
		fi
	fi
}


Uninstall_btwaf()
{
	rm -rf /www/server/panel/static/btwaf
	if [ ! -d /www/server/panel/plugin/btwaf_httpd ];then
		rm -rf /www/server/btwaf
	fi
	rm -f /www/server/panel/vhost/nginx/btwaf.conf
	rm -rf $pluginPath
	cat > /www/server/nginx/conf/luawaf.conf<<EOF
lua_shared_dict limit 10m;
lua_package_path "/www/server/nginx/waf/?.lua";
init_by_lua_file  /www/server/nginx/waf/init.lua;
access_by_lua_file /www/server/nginx/waf/waf.lua;
EOF

}

if [ "${1}" == 'install' ];then
	Install_btwaf
elif [ "${1}" == 'uninstall' ];then
	Uninstall_btwaf
fi
