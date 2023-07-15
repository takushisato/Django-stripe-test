"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings            # settings.pyの変数
from django.conf.urls.static import static  # メディア表示

# App_Folderからviews.pyで定義した関数呼出
from payment.views import (
    CreateCheckoutSessionView,
    ProductTopPageView,
    SuccessPageView,
    CancelPageView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),                                                                               # 管理画面
    path("", ProductTopPageView.as_view(), name="product-top-page"),                                               # 商品トップ
    path("create-checkout-session/<pk>/", CreateCheckoutSessionView.as_view(), name="create-checkout-session"),    # 個別商品決済画面
    path("success/", SuccessPageView.as_view(), name="success"),                                                   # 決済成功時にリダイレクト先
    path("cancel/", CancelPageView.as_view(), name="cancel"),                                                      # 決済キャンセル時のリダイレクト先
]

# メディア表示
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)