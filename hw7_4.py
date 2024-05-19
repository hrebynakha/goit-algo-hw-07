"""
Реалізуйте структуру даних для системи коментарів так, щоб коментарі могли мати відповіді, 
які, в свою чергу, також могли мати відповіді, формуючи таким чином ієрархічну структуру.
"""
from datetime import datetime
class Comment():
    def __init__(self, text, author) -> None:
        self.text = text
        self.author = author
        self.replies = []
        self.is_removed = False
        self.created_at = datetime.now()

    def created_time(self):
        return self.created_at.strftime("%H:%M:%S")

    def add_reply(self, comment) -> None:
        self.replies.append(comment)

    def remove_reply(self,) -> None:
        self.is_removed = True

    def display(self, tab=""):
        if self.is_removed:
            print(f"{tab}Цей коментар було видалено.")
        else:
            print(f"{tab}{self.author}: {self.text}[{self.created_time()}]")
        tab += "\t"
        for reply in self.replies:
            reply.display(tab)


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
