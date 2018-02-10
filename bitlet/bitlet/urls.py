"""bitlet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from accounts.views import login
from bitlet_web.views import bitcoin_chart,received_popup,bitcoin_buy,credit_card,receive,receive_funds,send_funds
from home.views import home
from includes.views import header
from setting_home.views import setting_home
from payment.views import custom_amount,confirm_popup,payment_success,sending_confirm,amount_enter,confirm_sending,received,send,send_coin,enter_amount

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   
    url(r'^$',login, name="login"),
    url(r'^amount_enter/$', amount_enter, name="amount_enter"),
    url(r'^custom_amount/$', custom_amount, name="custom_amount"),
    url(r'^enter_amount/$', enter_amount, name="enter_amount"),
    url(r'^confirm_sending/$', confirm_sending, name="confirm_sending"),
    url(r'^sending_confirm/$', sending_confirm, name="sending_confirm"),
  	url(r'^payment_success/$', payment_success, name="payment_success"),
  	url(r'^confirm_popup/$', confirm_popup, name="confirm_popup"),
    url(r'^home/$', home, name="home"),
    url(r'^header/$', header, name="header"),
    url(r'^send/$', send, name="send"),
    url(r'^receive/$',receive, name="receive"),
    url(r'^bitcoin_chart/$', bitcoin_chart, name="bitcoin_chart"),
    url(r'^bitcoin_buy/$', bitcoin_buy, name="bitcoin_buy"),
    url(r'^credit_card/$', credit_card, name="credit_card"),
    url(r'^send_coin/$', send_coin, name="send_coin"),
    url(r'^setting_home/$',setting_home, name="setting_home"),
    url(r'^received/$', received, name="received"),
    url(r'^receive_funds/$', receive_funds, name="receive_funds"),
    url(r'^received_popup/$', received_popup, name="received_popup"),
    url(r'^send_funds/$', send_funds, name="send_funds"),
    url(r'^send_coin/$', send_coin, name="send_coin"),
   

]
