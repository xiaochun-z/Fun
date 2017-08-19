// ieproxy.cpp: 定义 DLL 应用程序的导出函数。
//

#include "stdafx.h"
#define IEPROXY_EXPORTS
#include "ieproxy.h"
#include <Wininet.h>
#include <stdlib.h>
#include <tchar.h>

#pragma comment(lib, "Wininet.lib")

IEPROXY_API bool setproxy(TCHAR* server, bool enabled)
{
	INTERNET_PER_CONN_OPTION_LIST list;
	DWORD dwBufSize = sizeof(list);

	// Fill the list structure.
	list.dwSize = sizeof(list);

	// NULL == LAN, otherwise connectoid name.
	list.pszConnection = nullptr;

	// Set three options.
	list.dwOptionCount = 3;
	list.pOptions = new INTERNET_PER_CONN_OPTION[3];

	// Ensure that the memory was allocated.
	if (nullptr == list.pOptions)
	{
		// Return FALSE if the memory wasn't allocated.
		return false;
	}

	// Set flags.
	list.pOptions[0].dwOption = INTERNET_PER_CONN_FLAGS;
	list.pOptions[0].Value.dwValue = enabled ? PROXY_TYPE_PROXY : PROXY_TYPE_DIRECT;

	// Set proxy name.
	list.pOptions[1].dwOption = INTERNET_PER_CONN_PROXY_SERVER;

	list.pOptions[1].Value.pszValue = server;

	// Set proxy override.
	list.pOptions[2].dwOption = INTERNET_PER_CONN_PROXY_BYPASS;
	list.pOptions[2].Value.pszValue = TEXT("localhost;127.*;10.*;172.16.*;172.17.*;172.18.*;172.19.*;172.20.*;172.21.*;172.22.*;172.23.*;172.24.*;172.25.*;172.26.*;172.27.*;172.28.*;172.29.*;172.30.*;172.31.*;172.32.*;192.168.*");

	// Set the options on the connection.
	auto bReturn = InternetSetOption(nullptr,
	                                 INTERNET_OPTION_PER_CONNECTION_OPTION, &list, dwBufSize);
	if (bReturn)
	{
		InternetSetOption(nullptr,
		                  INTERNET_OPTION_SETTINGS_CHANGED, nullptr, 0);
		InternetSetOption(nullptr,
		                  INTERNET_OPTION_REFRESH, nullptr, 0);
	}

	// Free the allocated memory.
	delete[] list.pOptions;
	return bReturn;
}

IEPROXY_API void getproxy(TCHAR* server, int& size)
{
	DWORD psize = 0;

	/* first see how big a buffer we need for the IPO structure */
	InternetQueryOption(nullptr, INTERNET_OPTION_PROXY, nullptr, &psize);
	if (!psize)
	{
		return;
	}

	if (server == nullptr)
	{
		size = psize;
		return;
	}

	auto buf = new char[psize];

	/* now run the real query */
	if (!InternetQueryOption(nullptr, INTERNET_OPTION_PROXY, buf, &psize))
	{
		delete[] buf;
		return;
	}

	INTERNET_PROXY_INFO* pinfo = reinterpret_cast<INTERNET_PROXY_INFO *>(buf);
	size = psize;

	int len = lstrlen(pinfo->lpszProxy);
	_tcscpy_s(server, len, pinfo->lpszProxy);

	delete[] buf;
}

IEPROXY_API bool proxyEnabled()
{
	DWORD psize = 0;

	/* first see how big a buffer we need for the IPO structure */
	InternetQueryOption(nullptr, INTERNET_OPTION_PROXY, nullptr, &psize);
	if (!psize)
	{
		return false;
	}

	auto buf = new char[psize];

	/* now run the real query */
	if (!InternetQueryOption(nullptr, INTERNET_OPTION_PROXY, buf, &psize))
	{
		delete[] buf;
		return false;
	}

	INTERNET_PROXY_INFO* pinfo = reinterpret_cast<INTERNET_PROXY_INFO *>(buf);
	bool enabled = pinfo->dwAccessType == INTERNET_OPEN_TYPE_PROXY;

	delete[] buf;
	return enabled;
}
