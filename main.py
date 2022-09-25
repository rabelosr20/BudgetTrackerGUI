import tkinter as tk
import sys
import copy
from tkinter import messagebox


class BudgetTracker:
    """Creates a budget tracker object"""

    def __init__(self):
        self._income = 0
        self._needs_list = ["Rent", "Utilities", "Groceries", "Gas", "Pet", "Other needs"]
        self._needs_list_values = None
        self._wants_list = ["Dining Out", "Vacation", "TV/Streaming Services", "Misc"]
        self._wants_list_values = None
        self._needs_list_priorities = None
        self._wants_list_priorities = None
        self._new_income = 0
        self._debt = 0
        self._month_tracker = {"January": {}, "February": {}, "March": {}, "April": {}, "May": {}, "June": {},
                               "July": {}, "August": {}, "September": {}, "October": {}, "November": {},
                               "December": {}}
        self._needs_cost = 0
        self._wants_cost = 0
        self._month = None
        self._save_invest = ["Save/Invest"]
        self._target = 0
        self._new_dict = {}
        self._list_of_expenses = []
        self._cant_cut = 0
        self._ideal_budget = {"January": {}, "February": {}, "March": {}, "April": {}, "May": {}, "June": {},
                              "July": {}, "August": {}, "September": {}, "October": {}, "November": {},
                              "December": {}}
        self._month_list = ["January", "February", "March", "April", "May", "June",
                            "July", "August", "September", "October", "November",
                            "December"]
        self._invest_1 = 0
        self._invest_2 = 0
        self._needs_list_ratings = None
        self._wants_list_ratings = None

    def initial_income(self):
        """User enters their total income and the month that this income was from"""
        self._new_income = self._income
        print(f"Income and month set! {self._income} for income and {self._month} for the month.")

    def needs_value_list_creation(self):
        """Assigns values entered by the user to the various different expenses from the needs list"""
        expense = 0
        while expense < len(self._needs_list):
            new_expense = int(self._needs_list_values[expense])
            self._new_income -= int(new_expense)
            self._month_tracker[self._month][self._needs_list[expense]] = [new_expense]
            self._needs_cost = self._new_income
            expense += 1
        print(f"Needs expenses added! Here is the list {self._month_tracker[self._month]}.")

    def wants_value_list_creation(self):
        """Assigns values entered by the user to the various different expenses from the wants list."""
        expense = 0
        while expense < len(self._wants_list):
            new_expense = int(self._wants_list_values[expense])
            self._new_income -= int(new_expense)
            self._month_tracker[self._month][self._wants_list[expense]] = [new_expense]
            self._wants_cost = self._new_income
            expense += 1
        print(f"Wants expenses added! Here is the list {self._month_tracker[self._month]}.")

    def needs_priority_creation(self):
        """Assigns a priority to each need either no priority, low priority, or priority"""
        expense = 0
        while expense < len(self._needs_list):
            priority = self._needs_list_priorities[expense]
            self._month_tracker[self._month][self._needs_list[expense]].append(priority)
            expense += 1
        print(f"Needs priorities added! Here is the updated list {self._month_tracker[self._month]}.")

    def wants_priority_creation(self):
        """Assigns a priority to each want either no priority, low priority, or priority"""
        expense = 0
        while expense < len(self._wants_list):
            priority = self._wants_list_priorities[expense]
            self._month_tracker[self._month][self._wants_list[expense]].append(priority)
            expense += 1
        print(f"Wants priorities added! Here is the updated list {self._month_tracker[self._month]}.")

    def needs_and_wants_tracker(self):
        """Adds up and tracks the amount of expenses the user has and how much they have left after"""
        if self._new_income >= 1:
            return f"You have ${self._new_income} left over after necessities, wants, and savings/investments."
        elif self._new_income <= -1:
            return f"You are ${abs(self._new_income)} over budget we'll look at some ways to cut costs later."
        else:
            return "You have spent your entire budget we'll look at some ways to cut costs later."

    def debt_tracker(self):
        """Used to calculate how much money users should put towards their debt"""
        print("Ideally your debt payments should be 20% of your income, however if needed it should be at most 36% "
              "of your income")
        total_debt = self._debt
        debt_track = ["Debt"]
        print("You have $", total_debt, "in debt")
        self._month_tracker[self._month][debt_track[0]] = [total_debt]
        debt_percent = round(((total_debt / self._income) * 100), 2)
        self._new_income -= total_debt
        self._cant_cut += total_debt
        print(self._month_tracker)

        if debt_percent > 20:
            return (f"Your debt makes up  {debt_percent} % of your income.\n"
                    "Your debt is high ideally you need to cut this down to a more manageable percent.\n"
                    "Let's look at some ways we can do this!")
        else:
            return (f"Your debt makes up  {debt_percent}% of your income.\n"
                    "Your debt doesn't make up too high of percent of your income, however it is important\n"
                    "to focus on paying off debt if possible")

    def investment_and_save_recs_text(self):
        """Used to calculate how much the user should save/invest"""
        if self._new_income > self._income // 5:
            self._invest_1 = self._income // 10
            self._invest_2 = self._income // 5
            return (
                f"It is recommended to invest or save 10-20% of your income. You should try to invest and/or save at\n"
                f"least 10% of your income which is ${self._invest_1}, or if possible you should try to invest and/or\n"
                f"save 20% or more of your income which is ${self._invest_2}.\n"
                "Knowing this how much would you like to put towards your savings\n"
                f"and investments. Remember that you currently have ${self._new_income} left currently\n"
                "and that this amount will not be changed later on")

        elif self._new_income > self._income // 10:
            invest_1 = self._income // 10
            return (f"It is recommended that you invest about ${invest_1}. \n"
                    "Knowing this how much would you like to put towards your savings and investments.\n"
                    f"Remember that you currently have ${self._new_income} left currently \n "
                    f"and that this amount will not be changed later on.")

        else:
            return ("Unfortunately you do not have enough to save 10% or more of your income. We will look \n"
                    " at ways to cut costs so that you will be able to put some more money towards saving.\n"
                    "It is highly recommended that you invest $0.")

    def invest_and_save_entry(self, invest):
        """User enters the amount they would like to save/invest"""
        amount_saved = invest
        self._month_tracker[self._month][self._save_invest[0]] = [amount_saved]
        self._new_income -= int(amount_saved)
        print(self._month_tracker)

    def needs(self):
        """Tells the user what percent of their income that their needs make up"""
        save_needs = (self._needs_cost / self._income) * 100
        needs_percent = round(100 - save_needs)
        if needs_percent > 50:
            return (f"Your needs make up about {needs_percent}% of your income, ideally your needs should make up 50%\n"
                    "of your income. We should look at some ways we could cut this down to make it more manageable.")
        else:
            return (f"Your needs make up about {needs_percent}% of your income.  Which is ideal since wants should\n"
                    "make up 50% of your income or less.")

    def wants(self):
        """Tells the user what percent of their income that their wants make up"""
        save_wants = (self._wants_cost / self._income) * 100
        wants_percent = round(100 - save_wants)
        if wants_percent > 30:
            return (f"Your wants make up about {wants_percent}% of your income ideally your wants should make up\n"
                    "30% of your income. We should look at some ways we could cut this down to make if more "
                    "manageable.")
        else:
            return (f"Your wants make up about {wants_percent}% of your income. Which is ideal since wants should\n"
                    f"make up 30% of your income or less.")

    def priority(self):
        """Checks to see if any expenses are deemed priority, if they are it will add those costs to the expenses
                    that cannot be cut"""
        for expense in self._needs_list:
            if self._month_tracker[self._month][expense][1] == "Priority":
                self._cant_cut += self._month_tracker[self._month][expense][0]

    def cost_cut(self):
        """If the user has more than $0 left at this point it will ask them if they would like to cut costs
           if they have less than 0 it'll automatically prompt them for their target amount of money leftover
           from there it'll call various functions until costs are cut"""
        if self._new_income > 0:
            return ("It seems like you are on track with your budget, would you still like to look"
                    " at some ways you could cut costs?")
        else:
            return ("It looks like you need to cut some costs in order to have a net positive income."
                    "Select Yes to continue or No to restart.")

    def needs_cost_cut_np(self):
        """Cuts costs completely for any needs expense labeled no priority or np"""
        for expense in self._needs_list:
            if self._month_tracker[self._month][expense][1] == "No Priority":
                if self._new_income >= self._target:
                    return True
                else:
                    self._new_income += self._month_tracker[self._month][expense][0]
                    self._list_of_expenses.append(expense)
        return False

    def wants_cost_cut_np(self):
        """Cuts costs completely for any wants expense labeled no priority or np"""
        for expense in self._wants_list:
            if self._month_tracker[self._month][expense][1] == "No Priority":
                if self._new_income >= self._target:
                    return True
                else:
                    self._new_income += self._month_tracker[self._month][expense][0]
                    self._list_of_expenses.append(expense)

        return False

    def needs_cost_cut_lp(self):
        """Has the user rate their needs on a scale of 1-10 to determine what order the costs are cut in"""
        expense = 0
        for i in range(len(self._needs_list)):
            if self._month_tracker[self._month][self._needs_list[expense]][1] == "Low Priority":
                rating = self._needs_list_ratings[0]
                self._month_tracker[self._month][self._needs_list[expense]].append(rating)
                self._needs_list_ratings.remove(rating)
                expense += 1
            else:
                expense += 1

    def wants_cost_cut_lp(self):
        """Has the user rate their wants on a scale of 1-10 to determine what order the costs are cut in"""
        expense = 0
        for i in range(len(self._wants_list)):
            if self._month_tracker[self._month][self._wants_list[expense]][1] == "Low Priority":
                rating = self._needs_list_ratings[0]
                self._month_tracker[self._month][self._wants_list[expense]].append(rating)
                self._needs_list_ratings.remove(rating)
                expense += 1
            else:
                expense += 1

    def needs_priority(self):
        """Adds all the low priority needs to a new dictionary, so they can then be cut in correct order according
                  to priority"""
        rate = 0
        expense = 0
        while rate < 10:
            while expense < len(self._needs_list):
                if self._month_tracker[self._month][self._needs_list[expense]][1] == "Low Priority":
                    if self._month_tracker[self._month][self._needs_list[expense]][2] == rate:
                        self._new_dict[self._needs_list[expense]] = \
                            self._month_tracker[self._month][self._needs_list[expense]][0]
                    expense += 1
                else:
                    expense += 1
            rate += 1
            expense = 0
        print(self._new_dict)

    def wants_priority(self):
        """Adds all the low priority wants to a new dictionary, so they can then be cut in correct order according
                  to priority"""
        rate = 0
        expense = 0
        while rate < 10:
            while expense < len(self._wants_list):
                if self._month_tracker[self._month][self._wants_list[expense]][1] == "Low Priority":
                    if self._month_tracker[self._month][self._wants_list[expense]][2] == rate:
                        self._new_dict[self._wants_list[expense]] = \
                            self._month_tracker[self._month][self._wants_list[expense]][0]
                    expense += 1
                else:
                    expense += 1
            rate += 1
            expense = 0
        print(self._new_dict)

    def lp_cost_cut(self):
        """Cuts the low priority costs by a certain percent until the amount of money leftover equals the goal"""
        cut = 0.25
        times_run = 0
        while self._target > self._new_income or times_run != 100:
            for expense in self._new_dict.keys():
                self._new_income += self._new_dict[expense] * cut
                self._new_dict[expense] -= self._new_dict[expense] * cut
                times_run += 1
                if self._target <= self._new_income:
                    print(self._new_dict)
                    print(self._new_income)
                    return True
            if cut >= 0.06:
                cut -= 0.05
        return False

    def needs_results(self):
        """Displays the results for what they should cut their needs by in order to reach goal"""
        needs = ""
        for expense in self._needs_list:
            for expense_1 in self._new_dict.keys():
                if expense == expense_1:
                    saved = self._month_tracker[self._month][expense][0] - self._new_dict[expense_1]
                    needs = needs + f"You should cut {expense} by {saved} to help you meet your budget\n"
        return needs

    def wants_results(self):
        """Displays the results for what they should cut their wants by in order to reach goal"""
        wants = ""
        for expense in self._wants_list:
            for expense_1 in self._new_dict.keys():
                if expense == expense_1:
                    saved = self._month_tracker[self._month][expense][0] - self._new_dict[expense_1]
                    wants = wants + f"You should cut {expense} by {saved} to help you meet your budget\n"
        return wants

    def ideal_budget_needs(self):
        """Creates a copy of their dictionary showing the ideal budget for their n
                needs should look like after the costs are cut"""
        self._ideal_budget = copy.deepcopy(self._month_tracker.copy())
        for expense in self._needs_list:
            if self._ideal_budget[self._month][expense][1] == "No Priority":
                self._ideal_budget[self._month][expense][0] = 0
            elif self._ideal_budget[self._month][expense][1] == "Low Priority":
                for expense_1 in self._new_dict.keys():
                    if expense == expense_1:
                        self._ideal_budget[self._month][expense][0] = self._new_dict[expense_1]
        print(self._ideal_budget)
        self.ideal_budget_wants()

    def ideal_budget_wants(self):
        """Creates a copy of the original dictionary showing the ideal budget for their wants
                should look like after the costs are cut"""
        for expense in self._wants_list:
            if self._ideal_budget[self._month][expense][1] == "No Priority":
                self._ideal_budget[self._month][expense][0] = 0
            elif self._ideal_budget[self._month][expense][1] == "Low Priority":
                for expense_1 in self._new_dict.keys():
                    if expense == expense_1:
                        self._ideal_budget[self._month][expense][0] = self._new_dict[expense_1]
        print(self._ideal_budget)
        self.display_comparison()

    def display_comparison(self):
        """Displays the difference between the dictionaries for the user"""
        print("Here is your current budget,", self._month_tracker[self._month], "and this is what your budget"
                                                                                " could look like",
              self._ideal_budget[self._month])
        self.month_budget_finder()

    def month_budget_finder(self):
        """Asks them if they would like to see the budget for another month"""
        print("Please enter the month that you would like to see your data for")
        month_lookup = input()
        for month in self._month_tracker:
            if month_lookup == month:
                print(self._month_tracker[month_lookup])
        self.enter_more()

    def enter_more(self):
        """Allows the user to enter data for other months if they would like to"""
        print("Thank you so much for using budget finder would you like to enter data for another month? (y/n)")
        track_more = input()
        if track_more == "y":
            self.initial_income()
        elif track_more == "n":
            sys.exit(print("Thank you so much for using budget tracker comeback next month to continue to stay on track"
                           " with your budget"))

    def set_income(self, initial_income):
        self._income = initial_income

    def set_month(self, month):
        self._month = month

    def set_needs_list_values(self, values):
        self._needs_list_values = values

    def set_wants_list_values(self, values):
        self._wants_list_values = values

    def set_needs_list_priorities(self, priorities):
        self._needs_list_priorities = priorities

    def set_wants_list_priorities(self, priorities):
        self._wants_list_priorities = priorities

    def set_needs_list_ratings(self, priorities):
        self._needs_list_ratings = priorities

    def set_wants_list_ratings(self, priorities):
        self._wants_list_ratings = priorities

    def set_debt(self, debt):
        self._debt = debt

    def get_income(self):
        return self._income

    def get_new_income(self):
        return self._new_income

    def get_invest_1(self):
        return self._invest_1

    def get_invest_2(self):
        return self._invest_2

    def get_cannot_save(self):
        return self._income - self._cant_cut

    def set_target(self, target):
        self._target = target

    def get_month(self, month):
        return self._month_tracker[month]

    def get_lp_names(self):
        """Gets the names of the expenses labelled low priority"""
        names = []
        expense = 0
        while expense < len(self._needs_list):
            if self._month_tracker[self._month][self._needs_list[expense]][1] == "Low Priority":
                names.append(self._needs_list[expense])
                expense += 1
            else:
                expense += 1
        expense = 0
        while expense < len(self._wants_list):
            if self._month_tracker[self._month][self._wants_list[expense]][1] == "Low Priority":
                names.append(self._wants_list[expense])
                expense += 1
            else:
                expense += 1
        return names


class NotEnoughMoney(Exception):
    pass


class MonthNotEnteredCorrectly(Exception):
    pass


LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Veranda", 8)

budget_tracker = BudgetTracker()


class MainUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        """Initializes the window for the application"""
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        self.title('Budget Tracker')
        self.geometry('800x800')
        self.resizable(False, False)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(1, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        """Shows the specified frame from the frames list"""
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        """Initializes the starting page of the budget tracker"""
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter Month and Income", font=LARGE_FONT)
        label.grid(row=0, column=1)

        options = [
            "January", "February", "March", "April", "May", "June", "July", "August", "September", "November",
            "December"]
        self.clicked_month = tk.StringVar()
        self.clicked_month.set("January")
        month_label = tk.Label(self, text="Month:")
        month_label.grid(row=1, column=0)
        month_entry = tk.OptionMenu(self, self.clicked_month, *options)
        month_entry.grid(row=1, column=1)

        income_label = tk.Label(self, text="Income:")
        income_label.grid(row=2, column=0)
        self.income_entry = tk.Entry(self, width=10)
        self.income_entry.grid(row=2, column=1)
        button = tk.Button(self, text="Submit",
                           command=lambda: self.check_for_int())
        button.grid(row=3, column=1)

    def check_for_int(self):
        """Checks that the entered income is an integer"""
        try:
            int(self.income_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a number for your income")
            self.income_entry.delete(0, 'end')
        else:
            self.on_submit()

    def on_submit(self):
        """Submits information and shows next page"""
        budget_tracker.set_income(int(self.income_entry.get()))
        budget_tracker.set_month(self.clicked_month.get())
        budget_tracker.initial_income()
        self.income_entry.delete(0, 'end')
        self.controller.show_frame(PageOne)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        """Initializes page one of the budget tracker"""
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Please enter your income for each area", font=LARGE_FONT)
        label.grid(row=1, column=1)

        self.label2 = tk.Label(self, text="Needs Expenses:")
        self.label2.grid(row=2, column=1)

        self.label3 = tk.Label(self, text="Wants Expenses:")
        self.label3.grid(row=9, column=1)

        rent_label = tk.Label(self, text="Rent:")
        rent_label.grid(row=3, column=0)
        self.rent_entry = tk.Entry(self, width=10)
        self.rent_entry.grid(row=3, column=1)

        utilities_label = tk.Label(self, text="Utilities:")
        utilities_label.grid(row=4, column=0)
        self.utilities_entry = tk.Entry(self, width=10)
        self.utilities_entry.grid(row=4, column=1)

        groceries_label = tk.Label(self, text="Groceries:")
        groceries_label.grid(row=5, column=0)
        self.groceries_entry = tk.Entry(self, width=10)
        self.groceries_entry.grid(row=5, column=1)

        gas_label = tk.Label(self, text="Gas:")
        gas_label.grid(row=6, column=0)
        self.gas_entry = tk.Entry(self, width=10)
        self.gas_entry.grid(row=6, column=1)

        pet_label = tk.Label(self, text="Pet:")
        pet_label.grid(row=7, column=0)
        self.pet_entry = tk.Entry(self, width=10)
        self.pet_entry.grid(row=7, column=1)

        other_needs_label = tk.Label(self, text="Other Needs:")
        other_needs_label.grid(row=8, column=0)
        self.other_needs_entry = tk.Entry(self, width=10)
        self.other_needs_entry.grid(row=8, column=1)

        dining_out_label = tk.Label(self, text="Dining Out:")
        dining_out_label.grid(row=10, column=0)
        self.dining_out_entry = tk.Entry(self, width=10)
        self.dining_out_entry.grid(row=10, column=1)

        vacation_label = tk.Label(self, text="Vacation:")
        vacation_label.grid(row=11, column=0)
        self.vacation_entry = tk.Entry(self, width=10)
        self.vacation_entry.grid(row=11, column=1)

        tv_services_label = tk.Label(self, text="TV/Streaming Services:")
        tv_services_label.grid(row=12, column=0)
        self.tv_services_entry = tk.Entry(self, width=10)
        self.tv_services_entry.grid(row=12, column=1)

        misc_label = tk.Label(self, text="Miscellaneous:")
        misc_label.grid(row=13, column=0)
        self.misc_entry = tk.Entry(self, width=10)
        self.misc_entry.grid(row=13, column=1)

        button1 = tk.Button(self, text="Submit",
                            command=lambda: self.check_entries())
        button1.grid(row=14, column=1)

    def check_entries(self):
        """Checks each entry to make sure they are all integers"""
        try:
            int(self.rent_entry.get())
            int(self.misc_entry.get())
            int(self.utilities_entry.get())
            int(self.groceries_entry.get())
            int(self.gas_entry.get())
            int(self.pet_entry.get())
            int(self.other_needs_entry.get())
            int(self.dining_out_entry.get())
            int(self.vacation_entry.get())
            int(self.tv_services_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter numbers for all entries")

            self.rent_entry.delete(0, 'end')
            self.utilities_entry.delete(0, 'end')
            self.groceries_entry.delete(0, 'end')
            self.gas_entry.delete(0, 'end')
            self.pet_entry.delete(0, 'end')
            self.other_needs_entry.delete(0, 'end')
            self.dining_out_entry.delete(0, 'end')
            self.vacation_entry.delete(0, 'end')
            self.tv_services_entry.delete(0, 'end')
            self.misc_entry.delete(0, 'end')
        else:
            self.on_submit()

    def on_submit(self):
        """Submits the information and shows the next page"""
        needs_values = []
        wants_values = []

        needs_values.append(self.rent_entry.get())
        needs_values.append(self.utilities_entry.get())
        needs_values.append(self.groceries_entry.get())
        needs_values.append(self.gas_entry.get())
        needs_values.append(self.pet_entry.get())
        needs_values.append(self.other_needs_entry.get())

        budget_tracker.set_needs_list_values(needs_values)

        wants_values.append(self.dining_out_entry.get())
        wants_values.append(self.vacation_entry.get())
        wants_values.append(self.tv_services_entry.get())
        wants_values.append(self.misc_entry.get())

        budget_tracker.set_wants_list_values(wants_values)

        budget_tracker.needs_value_list_creation()
        budget_tracker.wants_value_list_creation()

        self.rent_entry.delete(0, 'end')
        self.utilities_entry.delete(0, 'end')
        self.groceries_entry.delete(0, 'end')
        self.gas_entry.delete(0, 'end')
        self.pet_entry.delete(0, 'end')
        self.other_needs_entry.delete(0, 'end')
        self.dining_out_entry.delete(0, 'end')
        self.vacation_entry.delete(0, 'end')
        self.tv_services_entry.delete(0, 'end')
        self.misc_entry.delete(0, 'end')

        self.controller.show_frame(PageTwo)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        """Initializes page two of the budget tracker"""
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Please enter your priority of each item", font=LARGE_FONT)
        label.grid(row=1, column=1)
        label2 = tk.Label(self, text="Note that no priority costs will be completely cut if needed, "
                                     "low priority costs will be cut a percent amount and priority "
                                     "costs cannot be cut", font=SMALL_FONT)
        label2.grid(row=2, column=1)
        options = [
            "No Priority",
            "Low Priority",
            "Priority"
        ]

        self.clicked_rent = tk.StringVar()
        self.clicked_rent.set("No Priority")
        rent_label = tk.Label(self, text="Rent:")
        rent_label.grid(row=3, column=0)
        rent_priority = tk.OptionMenu(self, self.clicked_rent, *options)
        rent_priority.grid(row=3, column=1)

        self.clicked_utilities = tk.StringVar()
        self.clicked_utilities.set("No Priority")
        utilities_label = tk.Label(self, text="Utilities:")
        utilities_label.grid(row=4, column=0)
        utilities_priority = tk.OptionMenu(self, self.clicked_utilities, *options)
        utilities_priority.grid(row=4, column=1)

        self.clicked_groceries = tk.StringVar()
        self.clicked_groceries.set("No Priority")
        groceries_label = tk.Label(self, text="Groceries:")
        groceries_label.grid(row=5, column=0)
        groceries_priority = tk.OptionMenu(self, self.clicked_groceries, *options)
        groceries_priority.grid(row=5, column=1)

        self.clicked_gas = tk.StringVar()
        self.clicked_gas.set("No Priority")
        gas_label = tk.Label(self, text="Gas:")
        gas_label.grid(row=6, column=0)
        gas_priority = tk.OptionMenu(self, self.clicked_gas, *options)
        gas_priority.grid(row=6, column=1)

        self.clicked_pet = tk.StringVar()
        self.clicked_pet.set("No Priority")
        pet_label = tk.Label(self, text="Pet:")
        pet_label.grid(row=7, column=0)
        pet_priority = tk.OptionMenu(self, self.clicked_pet, *options)
        pet_priority.grid(row=7, column=1)

        self.clicked_other_needs = tk.StringVar()
        self.clicked_other_needs.set("No Priority")
        other_needs_label = tk.Label(self, text="Other Needs:")
        other_needs_label.grid(row=8, column=0)
        other_needs_priority = tk.OptionMenu(self, self.clicked_other_needs, *options)
        other_needs_priority.grid(row=8, column=1)

        self.clicked_dining_out = tk.StringVar()
        self.clicked_dining_out.set("No Priority")
        dining_out_label = tk.Label(self, text="Dining Out:")
        dining_out_label.grid(row=9, column=0)
        dining_out_priority = tk.OptionMenu(self, self.clicked_dining_out, *options)
        dining_out_priority.grid(row=9, column=1)

        self.clicked_vacation = tk.StringVar()
        self.clicked_vacation.set("No Priority")
        vacation_label = tk.Label(self, text="Vacation:")
        vacation_label.grid(row=10, column=0)
        vacation_priority = tk.OptionMenu(self, self.clicked_vacation, *options)
        vacation_priority.grid(row=10, column=1)

        self.clicked_tv_services = tk.StringVar()
        self.clicked_tv_services.set("No Priority")
        tv_services_label = tk.Label(self, text="TV/Streaming Services:")
        tv_services_label.grid(row=11, column=0)
        tv_services_priority = tk.OptionMenu(self, self.clicked_tv_services, *options)
        tv_services_priority.grid(row=11, column=1)

        self.clicked_misc = tk.StringVar()
        self.clicked_misc.set("No Priority")
        misc_label = tk.Label(self, text="Miscellaneous:")
        misc_label.grid(row=12, column=0)
        misc_priority = tk.OptionMenu(self, self.clicked_misc, *options)
        misc_priority.grid(row=12, column=1)

        button1 = tk.Button(self, text="See Results",
                            command=lambda: self.on_submit())
        button1.grid(row=13, column=1)

    def on_submit(self):
        """Submits the necessary information and shows the next page"""
        needs_priorities = []
        wants_priorities = []

        needs_priorities.append(self.clicked_rent.get())
        needs_priorities.append(self.clicked_utilities.get())
        needs_priorities.append(self.clicked_groceries.get())
        needs_priorities.append(self.clicked_gas.get())
        needs_priorities.append(self.clicked_pet.get())
        needs_priorities.append(self.clicked_other_needs.get())

        wants_priorities.append(self.clicked_dining_out.get())
        wants_priorities.append(self.clicked_vacation.get())
        wants_priorities.append(self.clicked_tv_services.get())
        wants_priorities.append(self.clicked_misc.get())

        budget_tracker.set_needs_list_priorities(needs_priorities)
        budget_tracker.set_wants_list_priorities(wants_priorities)

        budget_tracker.needs_priority_creation()
        budget_tracker.wants_priority_creation()

        for widget in PageTwo.winfo_children(self):
            widget.destroy()

        label = tk.Label(self, text="Please enter your priority of each item", font=LARGE_FONT)
        label.grid(row=1, column=1)
        label2 = tk.Label(self, text="Note that no priority costs will be completely cut if needed, "
                                     "low priority costs will be cut a percent amount and priority "
                                     "costs cannot be cut", font=SMALL_FONT)
        label2.grid(row=2, column=1)
        options = [
            "No Priority",
            "Low Priority",
            "Priority"
        ]

        self.clicked_rent = tk.StringVar()
        self.clicked_rent.set("No Priority")
        rent_label = tk.Label(self, text="Rent:")
        rent_label.grid(row=3, column=0)
        rent_priority = tk.OptionMenu(self, self.clicked_rent, *options)
        rent_priority.grid(row=3, column=1)

        self.clicked_utilities = tk.StringVar()
        self.clicked_utilities.set("No Priority")
        utilities_label = tk.Label(self, text="Utilities:")
        utilities_label.grid(row=4, column=0)
        utilities_priority = tk.OptionMenu(self, self.clicked_utilities, *options)
        utilities_priority.grid(row=4, column=1)

        self.clicked_groceries = tk.StringVar()
        self.clicked_groceries.set("No Priority")
        groceries_label = tk.Label(self, text="Groceries:")
        groceries_label.grid(row=5, column=0)
        groceries_priority = tk.OptionMenu(self, self.clicked_groceries, *options)
        groceries_priority.grid(row=5, column=1)

        self.clicked_gas = tk.StringVar()
        self.clicked_gas.set("No Priority")
        gas_label = tk.Label(self, text="Gas:")
        gas_label.grid(row=6, column=0)
        gas_priority = tk.OptionMenu(self, self.clicked_gas, *options)
        gas_priority.grid(row=6, column=1)

        self.clicked_pet = tk.StringVar()
        self.clicked_pet.set("No Priority")
        pet_label = tk.Label(self, text="Pet:")
        pet_label.grid(row=7, column=0)
        pet_priority = tk.OptionMenu(self, self.clicked_pet, *options)
        pet_priority.grid(row=7, column=1)

        self.clicked_other_needs = tk.StringVar()
        self.clicked_other_needs.set("No Priority")
        other_needs_label = tk.Label(self, text="Other Needs:")
        other_needs_label.grid(row=8, column=0)
        other_needs_priority = tk.OptionMenu(self, self.clicked_other_needs, *options)
        other_needs_priority.grid(row=8, column=1)

        self.clicked_dining_out = tk.StringVar()
        self.clicked_dining_out.set("No Priority")
        dining_out_label = tk.Label(self, text="Dining Out:")
        dining_out_label.grid(row=9, column=0)
        dining_out_priority = tk.OptionMenu(self, self.clicked_dining_out, *options)
        dining_out_priority.grid(row=9, column=1)

        self.clicked_vacation = tk.StringVar()
        self.clicked_vacation.set("No Priority")
        vacation_label = tk.Label(self, text="Vacation:")
        vacation_label.grid(row=10, column=0)
        vacation_priority = tk.OptionMenu(self, self.clicked_vacation, *options)
        vacation_priority.grid(row=10, column=1)

        self.clicked_tv_services = tk.StringVar()
        self.clicked_tv_services.set("No Priority")
        tv_services_label = tk.Label(self, text="TV/Streaming Services:")
        tv_services_label.grid(row=11, column=0)
        tv_services_priority = tk.OptionMenu(self, self.clicked_tv_services, *options)
        tv_services_priority.grid(row=11, column=1)

        self.clicked_misc = tk.StringVar()
        self.clicked_misc.set("No Priority")
        misc_label = tk.Label(self, text="Miscellaneous:")
        misc_label.grid(row=12, column=0)
        misc_priority = tk.OptionMenu(self, self.clicked_misc, *options)
        misc_priority.grid(row=12, column=1)

        button1 = tk.Button(self, text="See Results",
                            command=lambda: self.on_submit())
        button1.grid(row=13, column=1)

        self.controller.show_frame(PageThree)


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        """Initializes the third page of the budget tracker"""
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Do you have any debt?", font=LARGE_FONT)
        self.label.grid(row=1, column=1)

        self.button1 = tk.Button(self, text="Yes", command=lambda: self.yes_debt())
        self.button1.grid(row=2, column=1)

        self.button2 = tk.Button(self, text="No", command=lambda: self.no_debt())
        self.button2.grid(row=2, column=2)
        self.debt_entry = None
        self.submit_button = None

    def yes_debt(self):
        """Allows the user to enter an amount of debt"""

        self.button1.destroy()
        self.button2.destroy()

        label1 = tk.Label(self, text="Let's look at how we could pay some debt!")
        label1.grid(row=3, column=1)

        debt_label = tk.Label(self, text="Please enter the total amount of your monthly debt payments:")
        debt_label.grid(row=4, column=1)
        self.debt_entry = tk.Entry(self, width=10)
        self.debt_entry.grid(row=4, column=2)

        self.submit_button = tk.Button(self, text="Continue", command=lambda: self.check_debt())
        self.submit_button.grid(row=5, column=2)

    def check_debt(self):
        """Checks that the entered debt is an integer"""
        try:
            int(self.debt_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter numbers for all entries")
            self.debt_entry.delete(0, 'end')
        else:
            self.on_submit()

    def no_debt(self):
        """"Allows the user to move on past the debt page"""
        self.button1.destroy()
        self.button2.destroy()

        budget_tracker.set_debt(0)

        label2 = tk.Label(self, text="Congratulations!")
        label2.grid(row=3, column=1)

        continue_button = tk.Button(self, text="Continue", command=lambda: self.on_continue())
        continue_button.grid(row=4, column=1)

    def on_submit(self):
        """Submits the information and shows the continue button"""
        budget_tracker.set_debt(int(self.debt_entry.get()))
        self.debt_entry.destroy()
        self.submit_button.destroy()
        debt_statement = budget_tracker.debt_tracker()
        label3 = tk.Label(self, text=debt_statement, wraplength=400)
        label3.grid(row=6, rowspan=2, column=1)

        continue_button = tk.Button(self, text="Continue", command=lambda: self.on_continue())
        continue_button.grid(row=20, column=1)

    def on_continue(self):
        """Shows the next page"""
        for widget in PageThree.winfo_children(self):
            widget.destroy()

        self.label = tk.Label(self, text="Do you have any debt?", font=LARGE_FONT)
        self.label.grid(row=1, column=1)

        self.button1 = tk.Button(self, text="Yes", command=lambda: self.yes_debt())
        self.button1.grid(row=2, column=1)

        self.button2 = tk.Button(self, text="No", command=lambda: self.no_debt())
        self.button2.grid(row=2, column=2)
        self.debt_entry = None
        self.submit_button = None

        self.controller.show_frame(PageFour)


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        """Initializes page four of the budget tracker"""
        self.controller = controller
        tk.Frame.__init__(self, parent)

        label_1 = tk.Label(self, text="Investment, Savings, and Budgeting Recommendations", font=LARGE_FONT)
        label_1.grid(row=0, column=1)

        label_2 = tk.Label(self, text="Click continue to see investment recommendations!")
        label_2.grid(row=1, column=1)

        self.continue_button = tk.Button(self, text="Continue", command=lambda: self.on_continue())
        self.continue_button.grid(row=2, column=1)
        self.invest_entry = None
        self.submit_button = None

    def on_continue(self):
        """Allows the user to enter an amount they would like to invest"""

        self.continue_button.destroy()

        label_3 = tk.Label(self, text=budget_tracker.investment_and_save_recs_text())
        label_3.grid(row=3, column=1, rowspan=2)

        self.invest_entry = tk.Entry(self, width=10)
        self.invest_entry.grid(row=9, column=1)

        self.submit_button = tk.Button(self, text="Submit", command=lambda: self.check_invest())
        self.submit_button.grid(row=10, column=1)

    def check_invest(self):
        """Checks that the invested amount is an integer and that the user has enough money to invest"""
        try:
            int(self.invest_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter numbers for all entries")
            self.invest_entry.delete(0, 'end')
        else:
            try:
                if int(self.invest_entry.get()) >= budget_tracker.get_cannot_save():
                    raise NotEnoughMoney
            except NotEnoughMoney:
                tk.messagebox.showerror("Error", "You do not have enough money to save that amount!")
                self.invest_entry.delete(0, 'end')
            else:
                self.on_submit()

    def on_submit(self):
        """Submits the information and shows the continue button"""

        budget_tracker.invest_and_save_entry(self.invest_entry.get())
        label_4 = tk.Label(self, text=budget_tracker.needs_and_wants_tracker())
        label_4.grid(row=11, column=1)

        self.invest_entry.destroy()
        self.submit_button.destroy()

        continue_button = tk.Button(self, text="Continue", command=lambda: self.move_on())
        continue_button.grid(row=12, column=1)

    def move_on(self):
        """Shows the next page"""
        for widget in PageFour.winfo_children(self):
            widget.destroy()

        label_1 = tk.Label(self, text="Investment, Savings, and Budgeting Recommendations", font=LARGE_FONT)
        label_1.grid(row=0, column=1)

        label_2 = tk.Label(self, text="Click continue to see investment recommendations!")
        label_2.grid(row=1, column=1)

        self.continue_button = tk.Button(self, text="Continue", command=lambda: self.on_continue())
        self.continue_button.grid(row=2, column=1)
        self.invest_entry = None
        self.submit_button = None

        self.controller.show_frame(PageFive)


class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        """Initializes the fifth page of the budget tracker"""
        self.invest_entry = None
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Let's look at some ways we could cut costs!", font=LARGE_FONT)
        self.label.grid(row=1, column=1)

        self.continue_button = tk.Button(self, text="Continue", command=lambda: self.show_info())
        self.continue_button.grid(row=2, column=1)
        self.labels_and_options = []
        self.label_2 = None
        self.label_3 = None
        self.label_4 = None
        self.button1 = None
        self.button2 = None
        self.saved_label = None
        self.saved_entry = None
        self.submit_button = None
        self.clicked_values = []
        self.titles = None

    def show_info(self):
        """Shows the user their budget info and asks if they would like to save more"""
        self.continue_button.destroy()

        self.label_2 = tk.Label(self, text=budget_tracker.needs())
        self.label_3 = tk.Label(self, text=budget_tracker.wants())

        self.label_2.grid(row=2, rowspan=2, column=1)
        self.label_3.grid(row=4, rowspan=2, column=1)

        self.label_4 = tk.Label(self, text=budget_tracker.cost_cut())
        self.label_4.grid(row=6, column=1)

        self.button1 = tk.Button(self, text="No",
                                 command=lambda: self.controller.show_frame(PageSeven))
        self.button2 = tk.Button(self, text="Yes", command=lambda: self.enter_amount())
        self.button1.grid(row=10, column=2)
        self.button2.grid(row=10, column=1)
        budget_tracker.priority()

    def enter_amount(self):
        """Allows the user to enter the amount they would like to save"""
        self.label_2.destroy()
        self.label_3.destroy()
        self.label_4.destroy()
        self.button1.destroy()
        self.button2.destroy()

        self.saved_label = tk.Label(self, text="Please enter the amount you would like to have leftover")
        self.saved_entry = tk.Entry(self, width=10)

        self.saved_label.grid(row=2, column=1)
        self.saved_entry.grid(row=2, column=2)

        self.submit_button = tk.Button(self, text="Submit", command=lambda: self.check_save())
        self.submit_button.grid(row=3, column=2)

    def check_save(self):
        """Checks the amount they would like to save for it being an integer and that they have enough money to save"""
        try:
            int(self.saved_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter numbers for all entries")
            self.saved_entry.delete(0, 'end')
        else:
            self.check_enough()

    def check_enough(self):
        try:
            if int(self.saved_entry.get()) >= budget_tracker.get_cannot_save():
                raise NotEnoughMoney
        except NotEnoughMoney:
            tk.messagebox.showerror("Error", "You do not have enough money to save that amount!")
            self.invest_entry.delete(0, 'end')
        else:
            self.enter_priorities()

    def enter_priorities(self):
        """Allows the user to enter a priority value for each low priority item"""
        budget_tracker.set_target(int(self.saved_entry.get()))

        self.saved_entry.destroy()
        self.saved_label.destroy()
        self.submit_button.destroy()

        self.info = tk.Label(self,
                             text="Note: Wants will always be cut before needs, even if they have a higher priority.")
        self.info.grid(row=2, column=1)
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.titles = budget_tracker.get_lp_names()
        for i in range(len(self.titles)):
            self.clicked_values.append(tk.IntVar())
            self.labels_and_options.append(
                [tk.Label(self, text=self.titles[i]), tk.OptionMenu(self, self.clicked_values[i], *options)])
        row = 3
        column = 1
        for i in range(len(self.labels_and_options)):
            self.labels_and_options[i][0].grid(row=row, column=column)
            self.labels_and_options[i][1].grid(row=row, column=column + 1)
            row += 1

        button1 = tk.Button(self, text="Continue",
                            command=lambda: self.on_submit())
        button1.grid(row=10, column=1)

    def on_submit(self):
        """Submits the information and calculates cost cuts"""
        needs_priorities = []

        for i in range(len(self.clicked_values)):
            needs_priorities.append(self.clicked_values[i].get())

        budget_tracker.set_needs_list_ratings(needs_priorities)

        budget_tracker.needs_cost_cut_lp()
        budget_tracker.wants_cost_cut_lp()

        budget_tracker.wants_priority()
        budget_tracker.needs_priority()

        for widget in PageFive.winfo_children(self):
            widget.destroy()

        self.label = tk.Label(self, text="Let's look at some ways we could cut costs!", font=LARGE_FONT)
        self.label.grid(row=1, column=1)

        self.continue_button = tk.Button(self, text="Continue", command=lambda: self.show_info())
        self.continue_button.grid(row=2, column=1)
        self.labels_and_options = []
        self.label_2 = None
        self.label_3 = None
        self.label_4 = None
        self.button1 = None
        self.button2 = None
        self.saved_label = None
        self.saved_entry = None
        self.submit_button = None
        self.clicked_values = []
        self.titles = None

        self.controller.show_frame(PageSix)


class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        """Initializes the sixth page of the budget tracker"""
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Lets see what would need to be cut to reach your goal!", font=LARGE_FONT)
        label.grid(row=1, column=1)

        self.lets_see = tk.Button(self, text="Lets See!", command=lambda: self.compute_savings())
        self.lets_see.grid(row=2, column=1)

    def compute_savings(self):
        """Shows the user information about how they could save"""
        self.lets_see.destroy()

        if budget_tracker.wants_cost_cut_np():
            label_1 = tk.Label(self, text="Looks like you can hit your target by cutting NP wants!")
            label_2 = tk.Label(self, text=budget_tracker.wants_results())
            label_1.grid(row=2, column=1)
            label_2.grid(row=3, column=1)
            continue_button = tk.Button(self, text="Continue", command=lambda: self.on_continue())
            continue_button.grid(row=20, column=1)
        elif budget_tracker.needs_cost_cut_np():
            label_1 = tk.Label(self, text="Looks like you can hit your target by cutting NP needs and NP wants!")
            label_2 = tk.Label(self, text=budget_tracker.needs_results())
            label_3 = tk.Label(self, text=budget_tracker.wants_results())
            label_1.grid(row=2, column=1)
            label_2.grid(row=3, column=1)
            label_3.grid(row=10, column=1)
            continue_button = tk.Button(self, text="Continue", command=lambda: self.on_continue())
            continue_button.grid(row=20, column=1)
        elif budget_tracker.lp_cost_cut():
            label_1 = tk.Label(self, text="Looks like you can hit your target by cutting multiple needs and wants!")
            label_2 = tk.Label(self, text=budget_tracker.needs_results())
            label_3 = tk.Label(self, text=budget_tracker.wants_results())
            label_1.grid(row=2, column=1)
            label_2.grid(row=3, column=1)
            label_3.grid(row=10, column=1)
            continue_button = tk.Button(self, text="Continue", command=lambda: self.on_continue())
            continue_button.grid(row=20, column=1)
        else:
            tk.Label(self, text="There is no way to reach your target! Hit continue to restart.")
            continue_button = tk.Button(self, text="Continue", command=lambda: self.on_continue())
            continue_button.grid(row=20, column=1)

    def on_continue(self):
        """Shows the next page"""
        for widget in PageSix.winfo_children(self):
            widget.destroy()

        label = tk.Label(self, text="Lets see what would need to be cut to reach your goal!", font=LARGE_FONT)
        label.grid(row=1, column=1)

        self.lets_see = tk.Button(self, text="Lets See!", command=lambda: self.compute_savings())
        self.lets_see.grid(row=2, column=1)

        self.controller.show_frame(PageSeven)


class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        """Initializes the seventh page of the budget tracker"""
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Would you like to enter another month or view a previous month?",
                              font=LARGE_FONT)
        self.label.grid(row=1, column=1)

        self.button1 = tk.Button(self, text="Enter More",
                                 command=lambda: controller.show_frame(StartPage))
        self.button1.grid(row=10, column=1)

        self.button2 = tk.Button(self, text="See a Previous Month",
                                 command=lambda: self.show_previous_month())
        self.button2.grid(row=11, column=1)

        self.button3 = tk.Button(self, text="Exit Program", command=lambda: self.exit())
        self.button3.grid(row=12, column=1)

        self.label1 = None
        self.clicked_month = None
        self.month_label = None
        self.month_entry = None
        self.button = None
        self.label2 = None

    def show_previous_month(self):
        self.button2.destroy()
        self.button1.destroy()
        self.label.destroy()
        self.label1 = tk.Label(self, text="Enter the month you would like to see data on.", font=LARGE_FONT)
        self.label1.grid(row=1, column=1)

        options = [
            "January", "February", "March", "April", "May", "June", "July", "August", "September", "November",
            "December"]
        self.clicked_month = tk.StringVar()
        self.clicked_month.set("January")
        self.month_label = tk.Label(self, text="Month:")
        self.month_label.grid(row=2, column=0)
        self.month_entry = tk.OptionMenu(self, self.clicked_month, *options)
        self.month_entry.grid(row=2, column=1)
        self.button = tk.Button(self, text="Submit",
                                command=lambda: self.submit())
        self.button.grid(row=3, column=1)

    def submit(self):
        wanted_info = budget_tracker.get_month(self.clicked_month.get())
        self.label1.destroy()
        self.month_entry.destroy()
        self.month_label.destroy()
        self.button.destroy()

        self.label2 = tk.Label(self, text=wanted_info)
        self.label2.grid(row=1, column=0)
        self.label2.configure(wraplength=700)

        self.button1 = tk.Button(self, text="Enter More",
                                 command=lambda: self.show_start())
        self.button1.grid(row=10, column=1)

        self.button3 = tk.Button(self, text="Exit Program", command=lambda: self.exit())
        self.button3.grid(row=12, column=1)

    def exit(self):
        sys.exit()

    def show_start(self):
        for widget in PageSeven.winfo_children(self):
            widget.destroy()

        self.label = tk.Label(self, text="Would you like to enter another month or view a previous month?",
                              font=LARGE_FONT)
        self.label.grid(row=1, column=1)

        self.button1 = tk.Button(self, text="Enter More",
                                 command=lambda: self.show_start())
        self.button1.grid(row=10, column=1)

        self.button2 = tk.Button(self, text="See a Previous Month",
                                 command=lambda: self.show_previous_month())
        self.button2.grid(row=11, column=1)

        self.button3 = tk.Button(self, text="Exit Program", command=lambda: self.exit())
        self.button3.grid(row=12, column=1)

        self.label1 = None
        self.clicked_month = None
        self.month_label = None
        self.month_entry = None
        self.button = None
        self.label2 = None

        self.controller.show_frame(StartPage)


app = MainUI()
app.mainloop()
