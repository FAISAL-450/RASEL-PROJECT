from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from account.models import Account

# 🔁 Reusable Pagination Function
def get_paginated_queryset(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")
    try:
        return paginator.page(page_number)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

# 💼 Finance Account Detailed View
def finance_ac_list(request):
    query = request.GET.get('q', '').strip()
    accounts = Account.objects.all()
    if query:
        accounts = accounts.filter(account_name__icontains=query)

    accounts_page = get_paginated_queryset(request, accounts, per_page=10)

    return render(request, 'finance/finance_ac_list.html', {
        'accounts': accounts_page,
        'query': query
    })

# 💼 Finance Transaction Detailed View
def finance_tn_list(request):
    query = request.GET.get('q', '').strip()
    transactions = Transaction.objects.all()
    if query:
        transactions = transactions.filter(transaction_type__icontains=query)

    transactions_page = get_paginated_queryset(request, transactions, per_page=10)

    return render(request, 'finance/finance_tn_list.html', {
        'transactions': transactions_page,
        'query': query
    })

