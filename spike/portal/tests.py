from django.test import Client, TestCase


class LanguageSpikeTests(TestCase):
    def get(self, lang):
        return Client().get("/", HTTP_ACCEPT_LANGUAGE=lang)

    def test_arabic_is_rtl(self):
        html = self.get("ar").content.decode()
        self.assertIn('lang="ar" dir="rtl"', html)
        self.assertIn("نموذج تجريبي غير رسمي", html)

    def test_english_is_ltr(self):
        html = self.get("en").content.decode()
        self.assertIn('lang="en" dir="ltr"', html)

    def test_somali_is_ltr_and_translated(self):
        html = self.get("so").content.decode()
        self.assertIn('lang="so" dir="ltr"', html)
        self.assertIn("Tijaabo aan rasmi ahayn", html)

    def test_language_switch_persists_in_cookie(self):
        c = Client()
        r = c.post("/i18n/setlang/", {"language": "ar", "next": "/"}, follow=True)
        self.assertIn('lang="ar" dir="rtl"', r.content.decode())
        self.assertEqual(c.cookies["sl_lang"].value, "ar")

    def test_unofficial_banner_on_every_language(self):
        for lang in ("so", "en", "ar"):
            self.assertIn('role="note"', self.get(lang).content.decode())
