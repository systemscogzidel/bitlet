from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def payment_success(request):
	
	return render(request,'send/payment_success.html',{})

def sending_confirm(request):
	
	return render(request,'send/sending_confirm.html',{})


def confirm_popup(request):
	
	return render(request,'send/confirm_popup.html',{})

def confirm_sending(request):
	
	return render(request,'send/confirm_sending.html',{})

def send(request):
	
	return render(request,'send/send.html',{})


def send_coin(request):
	
	return render(request,'send/send_coin.html',{})


def enter_amount(request):
	
	return render(request,'send/enter_amount.html',{})



def amount_enter(request):
	
	return render(request,'receive/amount_enter.html',{})
	
def received(request):
	
	return render(request,'receive/receive_home.html',{})

def custom_amount(request):
	
	return render(request,'receive/custom_amount.html',{})
