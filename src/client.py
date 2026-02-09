import requests
import urllib.parse
from bs4 import BeautifulSoup

from convert import Convert
from creator import Creator, CreatorsSearch
from note import Note, DraftSavedNote, TextNote

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
}

class Client:
    def __init__(self, cookie: dict = None):
        self.TOPURL = "https://note.com/api/v3"
        self.V2TOPURL = "https://note.com/api/v2"
        self.V1TOPURL = "https://note.com/api/v1"

        self.convert = Convert()

        self.cookie = cookie
        pass

    def fetchCreator(self, creatorName: int):
        data = requests.get(self.V2TOPURL + f"/creators/{creatorName}", headers=header)
        return Creator(data.json()["data"])
    
    def searchCreators(self, keyword: str):
        data = requests.get(self.TOPURL + f"/searches?context=user&q={urllib.parse.quote(keyword)}", headers=header)
        return CreatorsSearch(data.json())
    
    def fetchNotes(self):
        data = requests.get(self.TOPURL + "/notes", headers=header)
        return [Note(_) for _ in data.json().get('data', [])]
    
    def fetchNote(self, noteId: str):
        data = requests.get(self.TOPURL + f"/notes/{urllib.parse.quote(noteId)}", headers=header)
        return Note(data.json())
    
    def createNote(self, template_key: str = None):
        if not self.cookie:
            return ValueError("cookieを指定してください。")

        json_data = {
            'template_key': template_key,
        }

        data = requests.post(self.V1TOPURL + '/text_notes', cookies=self.cookie, json=json_data, headers=header)
        print(data.text)
        return TextNote(data.json()["data"])

    def draftSave(self, id: str, name: str, body: str):
        # この関数のbodyはConvert.markdown_to_htmlを使用して変換してください。

        if not self.cookie:
            return ValueError("cookieを指定してください。")
        
        body_length = len(BeautifulSoup(body, 'html.parser').text)
        print(body_length)
        
        params = {
            'id': id,
            'is_temp_saved': True,
        }

        json_data = {
            'body': body,
            'body_length': body_length,
            'name': name,
            'index': False,
            'is_lead_form': False,
        }
        data = requests.post(self.V1TOPURL + f"/text_notes/draft_save", headers=header, json=json_data, cookies=self.cookie, params=params)
        print(data.text)
        return DraftSavedNote(data.json()["data"])