# SL Digital – Batch 0 spike (unofficial, synthetic data only)

Purpose: validate that Django can serve Somali / English / Arabic (RTL) cleanly,
before committing to it. This is **not** a government platform and uses no real data.

## Run
```
python -m venv .venv && . .venv/bin/activate
pip install "django>=5.2,<5.3" polib
cd spike
python manage.py compilemessages   # needs GNU gettext
python manage.py test
python manage.py runserver
```

## Findings
- Somali (`so`) is not a built-in Django language; it is registered in `config/settings.py`
  via `LANG_INFO`. Works with `LocaleMiddleware`, the language switcher and the cookie.
- Arabic renders `dir="rtl"`; Somali/English `dir="ltr"`. Language preference is stored in the `sl_lang` cookie.
- Home page weight: ~2.5 KB raw / ~1.3 KB gzip per language; ~1–2 ms render (local, no DB).
  Real-network latency on weak links is not measured here.
- Not yet verified: font rendering of Arabic/Somali on low-end phones, Postgres, and visual QA in a browser.

## Translation review
All Somali strings are **machine drafts** (marked in `locale/so/.../django.po`).
They must be reviewed by a fluent Somali speaker before approval; none is an official term.
