from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, cart_add, cart_count, cart_clear


urlpatterns = [
	path("", home, name="organic_home"),
	# Cart endpoints
	path("cart/add", cart_add, name="cart_add"),
	path("cart/count", cart_count, name="cart_count"),
	path("cart/clear", cart_clear, name="cart_clear"),
	# Auth
	path("accounts/login/", auth_views.LoginView.as_view(template_name="organic_theme/login.html"), name="login"),
	path("accounts/logout/", auth_views.LogoutView.as_view(next_page="organic_home"), name="logout"),
]

