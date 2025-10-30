from django.db import models

# 🔢 Account Name for Dropdown
ACCOUNT_NAME_CHOICES = [
    ('Cash', 'Cash'),
    ('Bank', 'Bank'),
    ('Receivables', 'Receivables'),
    ('Payables', 'Payables'),
    ('Equity Capital', 'Equity Capital'),

    # Assets
    ('Inventory', 'Inventory'),
    ('Prepaid Expenses', 'Prepaid Expenses'),
    ('Fixed Assets', 'Fixed Assets'),
    ('Investments', 'Investments'),

    # Liabilities
    ('Accrued Expenses', 'Accrued Expenses'),
    ('Unearned Revenue', 'Unearned Revenue'),
    ('Loans Payable', 'Loans Payable'),

    # Equity
    ('Retained Earnings', 'Retained Earnings'),
    ('Owner’s Draw', 'Owner’s Draw'),

    # Income
    ('Sales Revenue', 'Sales Revenue'),
    ('Service Income', 'Service Income'),
    ('Interest Income', 'Interest Income'),

    # Expenses
    ('Rent Expense', 'Rent Expense'),
    ('Utilities Expense', 'Utilities Expense'),
    ('Salaries Expense', 'Salaries Expense'),
    ('Office Supplies', 'Office Supplies'),
    ('Depreciation Expense', 'Depreciation Expense'),
]

# 🔢 Account Types for Dropdown
ACCOUNT_TYPE_CHOICES = [
    ('ASSET', 'Asset'),
    ('LIABILITY', 'Liability'),
    ('EQUITY', 'Equity'),
    ('INCOME', 'Income'),
    ('EXPENSE', 'Expense'),
]

# 💱 Currency Options for Dropdown
CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('BDT', 'Bangladeshi Taka'),
    ('EUR', 'Euro'),
    ('INR', 'Indian Rupee'),
    ('GBP', 'British Pound'),
]

# ✅ Status Dropdown
STATUS_CHOICES = [
    ('ACTIVE', 'Active'),
    ('INACTIVE', 'Not Active'),
]

class Account(models.Model):
    account_name = models.CharField(max_length=100, choices=ACCOUNT_NAME_CHOICES, default='Cash')  # Account Name
    account_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES, default='ASSET')
    account_description = models.TextField(blank=True, null=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='USD')
    cost_center = models.CharField(max_length=50, blank=True, null=True)  # 🔓 Free-text input
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_name} ({self.account_code})"


