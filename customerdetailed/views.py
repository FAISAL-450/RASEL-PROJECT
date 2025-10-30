# A - Import Required Modules
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

from .models import CustomerDetailed
from .forms import CustomerDetailedForm

# B - Filtering Function
def filter_customerdetaileds(query=None, user=None, exclude_user=None):
    queryset = CustomerDetailed.objects.all()

    if user:
        queryset = queryset.filter(created_by=user)

    if exclude_user:
        queryset = queryset.exclude(created_by=exclude_user)

    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(company__icontains=query)
        )

    return queryset

# C - Reusable Pagination Function
def get_paginated_queryset(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")

    try:
        return paginator.page(page_number)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

# D - Unified Dashboard View (List View + Form Submission)
@login_required
def customerdetailed_dashboard(request):
    query = request.GET.get("q", "").strip()
    form = CustomerDetailedForm(request.POST or None)

    # Role-based data filtering
    if request.user.username == 'kamal':
        customerdetaileds = filter_customerdetaileds(query=query, exclude_user=request.user)
    else:
        customerdetaileds = filter_customerdetaileds(query=query, user=request.user)

    customerdetaileds_page = get_paginated_queryset(request, customerdetaileds)

    # Save logic: only non-Kamal users can submit
    if request.user.username != 'kamal' and request.method == "POST" and form.is_valid():
        customer = form.save(commit=False)
        customer.created_by = request.user
        customer.team = getattr(request.user.customerdetailed_profile, "role", None)
        customer.save()
        messages.success(request, "✅ Customer detailed record created successfully.")
        return redirect(f"{reverse('customerdetailed_dashboard')}?q={query}")

    return render(request, "customerdetailed/customerdetailed_dashboard.html", {
        "customerdetaileds": customerdetaileds_page,
        "query": query,
        "form": form,
        "mode": "list",
        "readonly": request.user.username == 'kamal'
    })

# E - Admin Dashboard View (Kamal only, read-only)
@user_passes_test(lambda u: u.username == 'kamal')
def admin_dashboard(request):
    query = request.GET.get("q", "").strip()
    customerdetaileds = filter_customerdetaileds(query=query, exclude_user=request.user)
    customerdetaileds_page = get_paginated_queryset(request, customerdetaileds)

    return render(request, "customerdetailed/customerdetailed_dashboard.html", {
        "customerdetaileds": customerdetaileds_page,
        "query": query,
        "form": CustomerDetailedForm(),  # Kamal can view form but not submit
        "mode": "admin",
        "readonly": True
    })

# F - Edit View (Only owner can edit)
@login_required
def edit_customer(request, pk):
    customer = get_object_or_404(CustomerDetailed, pk=pk)

    if customer.created_by != request.user or request.user.username == 'kamal':
        raise PermissionDenied

    query = request.GET.get("q", "").strip()
    form = CustomerDetailedForm(request.POST or None, instance=customer)

    if form.is_valid():
        form.save()
        messages.success(request, "✏️ Customer detailed record updated successfully.")
        return redirect(f"{reverse('customerdetailed_dashboard')}?q={query}")

    customerdetaileds = filter_customerdetaileds(query=query, user=request.user)
    customerdetaileds_page = get_paginated_queryset(request, customerdetaileds)

    return render(request, "customerdetailed/customerdetailed_dashboard.html", {
        "form": form,
        "mode": "edit",
        "customer": customer,
        "query": query,
        "customerdetaileds": customerdetaileds_page,
        "readonly": False
    })

# G - Delete View (Only owner can delete)
@login_required
def delete_customer(request, pk):
    customer = get_object_or_404(CustomerDetailed, pk=pk)

    if customer.created_by != request.user or request.user.username == 'kamal':
        raise PermissionDenied

    query = request.GET.get("q", "").strip()

    if request.method == 'POST':
        name = customer.name
        customer.delete()
        messages.success(request, f"🗑️ Customer '{name}' deleted successfully.")
        return redirect(f"{reverse('customerdetailed_dashboard')}?q={query}")

    return render(request, "customerdetailed/confirm_delete.html", {
        "customer": customer,
        "query": query
    })




