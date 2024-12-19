from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .utils import generate_pie_charts
from ..forms import BudgetForm
from ..models import Budget

budgets = Blueprint('budgets', __name__, template_folder='../templates/budgets')

@budgets.route('/budgets')
@login_required
def view_budgets():
    budgets = Budget.objects(user=current_user)
    if not budgets:
        pie_chart1, pie_chart2 = None, None
    else:
        pie_chart1, pie_chart2 = generate_pie_charts(budgets)

    return render_template('view_budgets.html', budgets=budgets, pie_chart1=pie_chart1, pie_chart2=pie_chart2)

@budgets.route('/budgets/create', methods=['GET', 'POST'])
@login_required
def create_budget():
    form = BudgetForm()
    if form.validate_on_submit():
        category = form.category.data
        amount = form.amount.data
        start_date = form.start_date.data
        end_date = form.end_date.data

        if amount <= 0:
            flash('Budget amount must be positive!', 'danger')
            return redirect(url_for('budgets.create_budget'))

        if start_date > end_date:
            flash('Start date cannot be after end date!', 'danger')
            return redirect(url_for('budgets.create_budget'))

        new_budget = Budget(category=category, amount=amount, start_date=start_date, end_date=end_date, user=current_user)
        new_budget.save()
        return redirect(url_for('budgets.view_budgets'))

    return render_template('create_budget.html', form=form)

@budgets.route('/budgets/view/<budget_id>')
@login_required
def view_budget(budget_id):
    budget = Budget.objects(id=budget_id, user=current_user).first()
    if not budget:
        flash('Budget not found.', 'danger')
        return redirect(url_for('budgets.view_budgets'))

    return render_template('view_budget.html', budget=budget)

@budgets.route('/budgets/edit/<budget_id>', methods=['GET', 'POST'])
@login_required
def edit_budget(budget_id):
    budget = Budget.objects(id=budget_id, user=current_user).first()
    if not budget:
        flash('Budget not found.', 'danger')
        return redirect(url_for('budgets.view_budgets'))

    form = BudgetForm()
    if form.validate_on_submit():
        category = form.category.data
        amount = form.amount.data
        start_date = form.start_date.data
        end_date = form.end_date.data

        if amount <= 0:
            flash('Budget amount must be positive!', 'danger')
            return redirect(url_for('budgets.edit_budget', budget_id=budget.id))

        if start_date > end_date:
            flash('Start date cannot be after end date!', 'danger')
            return redirect(url_for('budgets.edit_budget', budget_id=budget.id))

        budget.category = category
        budget.amount = amount
        budget.start_date = start_date
        budget.end_date = end_date
        budget.save()
        return redirect(url_for('budgets.view_budgets'))

    form.category.data = budget.category
    form.amount.data = budget.amount
    form.start_date.data = budget.start_date
    form.end_date.data = budget.end_date

    return render_template('edit_budget.html', form=form, budget=budget)

@budgets.route('/budgets/delete/<budget_id>', methods=['POST'])
@login_required
def delete_budget(budget_id):
    budget = Budget.objects(id=budget_id, user=current_user).first()
    if budget:
        budget.delete()
    else:
        flash('Budget not found.', 'danger')

    return redirect(url_for('budgets.view_budgets'))