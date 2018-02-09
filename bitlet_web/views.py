from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



	
def payment_popup(request):
	
	return render(request,'payment_popup.html',{})

def receive(request):
	
	return render(request,'receive.html',{})


def received_popup(request):
	
	return render(request,'received_popup.html',{})



def credit_card(request):
	
	return render(request,'credit_card.html',{})


def bitcoin_chart(request):
	
	return render(request,'bitcoin_chart.html',{})

def bitcoin_buy(request):
	
	return render(request,'bitcoin_buy.html',{})


def receive_funds(request):
	
	return render(request,'receive_funds.html',{})


def send_funds(request):
	
	return render(request,'send_funds.html',{})

	
def send_coin(request):
	
	return render(request,'send_coin.html',{})



