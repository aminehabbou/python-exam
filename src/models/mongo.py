from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, IntField, StringField


class MSG(EmbeddedDocument):
    role = StringField()
    content = StringField()


class Choice(EmbeddedDocument):
    index = IntField()
    message = EmbeddedDocumentField(MSG)
    finish_reason = StringField()


class CH(EmbeddedDocument):
    role_ch = StringField()
    content = StringField()


class Chat(Document):
    id = IntField(required=True)
    object = StringField()
    created = IntField()
    model = StringField()
    choice = EmbeddedDocumentField(Choice)
    conversation_history = EmbeddedDocumentField(CH)
