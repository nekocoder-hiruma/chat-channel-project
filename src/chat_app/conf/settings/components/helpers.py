from django.core.mail.backends.locmem import EmailBackend
from django.core.mail.message import make_msgid


class TestEmailBackendMixin:
    """
    Work around slow development email backend due to slow socket.getfqdn() call.
    This simply uses "example.com" instead of your local machine's hostname.
    """

    def send_messages(self, messages):
        for message in messages:
            if 'message-id' not in message.extra_headers:
                message.extra_headers['Message-ID'] = make_msgid(domain='example.com')
        return super().send_messages(messages)


class FastEmailBackend(TestEmailBackendMixin, EmailBackend):
    pass
