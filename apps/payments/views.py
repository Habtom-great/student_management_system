from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm


def payments_dashboard(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payments:dashboard')  # Use namespaced URL name here
    else:
        form = PaymentForm()

    payments = Payment.objects.select_related('user').order_by('-timestamp')  # Adjust 'timestamp' field name if needed
    recent_payments = payments[:10]

    total_amount = sum(p.amount for p in payments)
    num_paid = payments.filter(status='paid').count()
    num_unpaid = payments.filter(status='unpaid').count()

    context = {
        'form': form,
        'payments': payments,
        'total_payments': total_amount,
        'paid_students': num_paid,
        'unpaid_students': num_unpaid,
        'recent_payments': recent_payments,
    }
    return render(request, 'payments/dashboard.html', context)

def dashboard(request):
    # your logic here
    return render(request, 'some_template.html')
def dashboard(request):
    return render(request, 'payments/dashboard.html')
