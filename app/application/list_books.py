from app.domain.ports import BookRepository

class ListBooks:
    
    def __init__(self, repo: BookRepository):
        self.repo = repo
        
        
    def execute(self):
        return self.repo.get_all()