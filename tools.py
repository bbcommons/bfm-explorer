#!/usr/bin/env python3

def downloadFile(item, session):
    id = item['id']
    filename = item['file_name']
    url = f'https://fundingmap.fcc.gov/bfm/api/map/getBFMDataDownloadFile/{id}'
    r = session.get(url)
    open(f'{filename}.zip', 'wb').write(r.content)
    return filename