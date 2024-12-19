from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Budget, Expense
from ..forms import ExpenseForm

expenses = Blueprint('expenses', __name__, template_folder='../templates/expenses')

@expenses.route('/expenses')
@login_required
def view_expenses():
    user_expenses = Expense.objects(user=current_user)
    return render_template('view_expenses.html', expenses=user_expenses)

@expenses.route('/expenses/create', methods=['GET', 'POST'])
@login_required
def create_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        category = form.category.data
        amount = form.amount.data
        description = form.description.data
        date = form.date.data
        budget = Budget.objects(category=form.category.data, user=current_user).first()

        if not budget:
            flash("No budget found for this category!", "danger")
            return redirect(url_for('expenses.create_expense'))

        if date < budget.start_date or date > budget.end_date:
            flash("Invalid date for this budget!", "danger")
            return redirect(url_for('expenses.create_expense'))

        if amount <= 0:
            flash('Expense amount must be positive!', 'danger')
            return redirect(url_for('expenses.create_expense'))

        new_expense = Expense(category=category, amount=amount, description=description, date=date, user=current_user)
        new_expense.save()
        return redirect(url_for('expenses.view_expenses'))

    return render_template('create_expense.html', form=form)

@expenses.route('/expenses/view/<expense_id>')
@login_required
def view_expense(expense_id):
    expense = Expense.objects(id=expense_id, user=current_user).first()
    if not expense:
        flash('Expense not found.', 'danger')
        return redirect(url_for('expenses.view_expenses'))

    return render_template('view_expense.html', expense=expense)

@expenses.route('/expenses/edit/<expense_id>', methods=['GET', 'POST'])
@login_required
def edit_expense(expense_id):
    expense = Expense.objects(id=expense_id, user=current_user).first()
    if not expense:
        flash('Expense not found.', 'danger')
        return redirect(url_for('expenses.view_expenses'))

    form = ExpenseForm()
    if form.validate_on_submit():
        category = form.category.data
        amount = form.amount.data
        description = form.description.data
        date = form.date.data
        budget = Budget.objects(category=form.category.data, user=current_user).first()

        if not budget:
            flash("No budget found for this category!", "danger")
            return redirect(url_for('expenses.edit_expense', expense_id=expense.id))

        if date < budget.start_date or date > budget.end_date:
            flash("Invalid date for this budget!", "danger")
            return redirect(url_for('expenses.edit_expense', expense_id=expense.id))

        if amount <= 0:
            flash('Expense amount must be positive!', 'danger')
            return redirect(url_for('expenses.edit_expense', expense_id=expense.id))

        expense.category = category
        expense.amount = amount
        expense.description = description
        expense.date = date
        expense.save()
        return redirect(url_for('expenses.view_expenses'))

    form.category.data = expense.category
    form.amount.data = expense.amount
    form.description.data = expense.description
    form.date.data = expense.date

    return render_template('edit_expense.html', form=form, expense=expense)

@expenses.route('/expenses/delete/<expense_id>', methods=['POST'])
@login_required
def delete_expense(expense_id):
    expense = Expense.objects(id=expense_id, user=current_user).first()
    if expense:
        expense.delete()
    else:
        flash('Expense not found.', 'danger')

    return redirect(url_for('expenses.view_expenses'))