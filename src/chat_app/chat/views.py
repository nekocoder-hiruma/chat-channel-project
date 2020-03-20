from django.http import Http404
from django.views.generic import TemplateView


class ChatIndexView(TemplateView):
    template_name = 'chat/index.html'


class ChatRoomView(TemplateView):
    template_name = 'chat/chat_room.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        room_name = kwargs.get('room_name', None)
        if not room_name:
            raise Http404
        context_data['room_name'] = room_name
        context_data['page_title'] = f'Chat Room - {room_name}'

        return context_data
