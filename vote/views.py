from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from .models import Emoji


def emoji_list(request):
    emojis = Emoji.objects.all()
    return render(request, "vote/emoji_list.html", {"emojis": emojis})


@require_POST
def emoji_vote(request, pk):
    emoji = get_object_or_404(Emoji, pk=pk)
    emoji.votes = F("votes") + 1
    emoji.save(update_fields=["votes"])
    emoji.refresh_from_db()
    return render(request, "vote/_emoji_card.html", {"emoji": emoji})
