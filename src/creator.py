class Creator:
    def __init__(self, json_data: dict):
        data = json_data

        self.id = data.get("id")
        self.key = data.get("key")
        self.nickname = data.get("nickname")
        self.urlname = data.get("urlname")
        self.profile = data.get("profile")
        
        self.note_count = data.get("noteCount", 0)
        self.following_count = data.get("followingCount", 0)
        self.follower_count = data.get("followerCount", 0)
        
        self.is_myself = data.get("isMyself", False)
        self.is_pro = data.get("isPro", False)
        
        self.profile_image_url = data.get("profileImageUrl")
        
        self.socials = data.get("socials", {})
        
    def __repr__(self):
        return f"<Creator(nickname='{self.nickname}', id={self.id})>"
    
class CreatorsSearch:
    def __init__(self, json_data):
        data_part = json_data.get("data", {})
        user_data = data_part.get("users", {})
        
        self.users = [Creator(u) for u in user_data.get("contents", [])]
        
        self.total_count = user_data.get("total_count", 0)
        self.user_cursor = data_part.get("user_cursor")
        
    def get(self):
        return self.users
    
    def __repr__(self):
        return f"<CreatorsSearch(total_count='{self.total_count}'>"