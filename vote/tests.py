from django.test import TestCase
from django.urls import reverse

from .models import Emoji


class EmojiVoteIntegrationTests(TestCase):
    def test_post_vote_increments_votes_in_database(self):
        emoji = Emoji.objects.create(character="😀", name="smile", votes=3)
        url = reverse("emoji_vote", kwargs={"pk": emoji.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        emoji.refresh_from_db()
        self.assertEqual(emoji.votes, 4)
        self.assertIn(b"emoji-card", response.content)
        self.assertIn(b"4 vote", response.content)

    def test_get_vote_returns_405(self):
        emoji = Emoji.objects.create(character="🎉", name="party", votes=0)
        url = reverse("emoji_vote", kwargs={"pk": emoji.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)
