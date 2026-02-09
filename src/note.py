class NoteAuthor:
    def __init__(self, user_data: dict):
        if not user_data:
            return
        self.id = user_data.get("id")
        self.nickname = user_data.get("nickname")
        self.urlname = user_data.get("urlname")
        self.note_count = user_data.get("note_count", 0)
        self.follower_count = user_data.get("follower_count", 0)
        self.profile_image = user_data.get("user_profile_image_path")
        self.twitter_id = user_data.get("twitter_nickname")

    def __repr__(self):
        return f"<NoteAuthor(nickname='{self.nickname}')>"

class Note:
    def __init__(self, json_data: dict):
        data = json_data
        
        self.id = data.get("id")
        self.title = data.get("name")
        self.body = data.get("body")
        self.price = data.get("price", 0)
        self.publish_at = data.get("publish_at")
        self.note_url = data.get("note_url")
        self.eyecatch_url = data.get("eyecatch")
        
        self.like_count = data.get("like_count", 0)
        self.comment_count = data.get("comment_count", 0)
        
        self.author = NoteAuthor(data.get("user"))

    def __repr__(self):
        return f"<Note(title='{self.title}', price={self.price})>"
    
class DraftSavedNote:
    def __init__(self, json_data: dict):
        data = json_data

        self.result = data.get('result')
        self.note_days_count = data.get('note_days_count')
        self.updated_at = data.get('updated_at')

    def __repr__(self):
        return f"<DraftSavedNote(result='{self.result}')>"
    
class TextNote:
    def __init__(self, json_data: dict):
        data = json_data
        
        self.id = data.get("id")
        self.key = data.get("key")
        self.type = data.get("type")
        self.name = data.get("name")
        self.body = data.get("body")
        self.description = data.get("description")
        self.user_id = data.get("user_id")
        self.status = data.get("status")
        self.price = data.get("price")
        self.publish_at = data.get("publish_at")
        self.created_at = data.get("created_at")
        self.slug = data.get("slug")
        self.can_publish = data.get("can_publish")
        self.can_update = data.get("can_update")
        self.can_read = data.get("can_read")

    def __repr__(self):
        return f"<TextNote(id='{self.id}')>"