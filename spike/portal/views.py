from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Synthetic, clearly unofficial demo services (names are placeholders, not real agencies).
DEMO_SERVICES = [
    {"name": _("Book an appointment (demo)"), "agency": _("Demo Agency A")},
    {"name": _("Request a certificate (demo)"), "agency": _("Demo Agency B")},
    {"name": _("Business service enquiry (demo)"), "agency": _("Demo Agency C")},
    {"name": _("Track a request (demo)"), "agency": _("Demo Agency D")},
]


def home(request):
    return render(request, "portal/home.html", {"services": DEMO_SERVICES})
