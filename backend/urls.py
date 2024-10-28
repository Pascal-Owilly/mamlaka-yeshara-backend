
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),  # Include the blog app's URLs
    path('api/blog/articles/', include('blog.urls_backup')),  # Include the blog app's URLs
    path('yeshara/', include('yeshara.urls')),
    path('', include('blog.template_urls')),  # Include the blog app's template URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Include the built-in auth views
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    # Custom password reset URLs
    path('accounts/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)