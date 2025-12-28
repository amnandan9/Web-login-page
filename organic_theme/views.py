from django.conf import settings
from django.http import FileResponse, Http404, JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from pathlib import Path



@ensure_csrf_cookie
def home(request):
	index_path = Path(settings.BASE_DIR) / "index.html"
	if not index_path.exists():
		raise Http404("index.html not found")
	return HttpResponse(index_path.read_text(encoding="utf-8"))


def _get_cart(session):
	cart = session.get("cart", {})
	if not isinstance(cart, dict):
		cart = {}
	return cart


def cart_add(request):
	if request.method != "POST":
		return JsonResponse({"error": "POST required"}, status=405)
	product_id = request.POST.get("product_id") or "unknown"
	qty = request.POST.get("quantity") or "1"
	try:
		qty_int = max(1, int(qty))
	except Exception:
		qty_int = 1
	cart = _get_cart(request.session)
	cart[product_id] = cart.get(product_id, 0) + qty_int
	request.session["cart"] = cart
	request.session.modified = True
	return JsonResponse({"ok": True, "count": sum(cart.values())})


def cart_count(request):
	cart = _get_cart(request.session)
	return JsonResponse({"count": sum(cart.values())})


def cart_clear(request):
	request.session["cart"] = {}
	request.session.modified = True
	return JsonResponse({"ok": True, "count": 0})

