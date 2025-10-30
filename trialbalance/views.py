from django.shortcuts import render
from django.db.models import Sum, Case, When, DecimalField
from journalentry.models import JournalEntry

def trialbalance_dashboard(request):
    posted_entries = JournalEntry.objects.select_related('account').all()

    account_totals = posted_entries.values(
        'account__account_name',
        'account__account_type'  # ✅ Include account type from related Account model
    ).annotate(
        debit_total=Sum(
            Case(
                When(entry_type='DEBIT', then='amount'),
                default=0,
                output_field=DecimalField()
            )
        ),
        credit_total=Sum(
            Case(
                When(entry_type='CREDIT', then='amount'),
                default=0,
                output_field=DecimalField()
            )
        )
    ).order_by('account__account_type', 'account__account_name')  # ✅ Optional: group by type

    total_debit = sum(item['debit_total'] for item in account_totals)
    total_credit = sum(item['credit_total'] for item in account_totals)

    return render(request, "trialbalance/trialbalance_dashboard.html", {
        "account_totals": account_totals,
        "total_debit": total_debit,
        "total_credit": total_credit,
    })













