// ieproxyApp.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "../ieproxy/ieproxy.h"

#pragma comment(lib, "../Debug/ieproxy.lib")

int main()
{
	//setproxy(_T("127.0.0.1:8118"), true);
//	int size;
//	getProxy(nullptr, size);
//	TCHAR* server = new TCHAR[size];
//	getProxy(server, size);
//	delete[] server;
	bool enabled = proxy_enabled();

    return 0;
}

