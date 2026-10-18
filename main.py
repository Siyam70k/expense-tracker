# import flet as ft

# def main(page: ft.Page):
#     page.title = "Expense Tracker"
#     page.window_width = 380
#     page.window_height = 700
#     page.theme_mode = ft.ThemeMode.LIGHT

#     # Variables
#     total_income = 0
#     total_expense = 0

#     # UI Components
#     balance_text = ft.Text("Balance: ৳0", size=22, weight=ft.FontWeight.BOLD)
#     income_text = ft.Text("Income: ৳0", color=ft.colors.GREEN_600)
#     expense_text = ft.Text("Expense: ৳0", color=ft.colors.RED_600)

#     amount_input = ft.TextField(label="Amount (৳)", keyboard_type=ft.KeyboardType.NUMBER)
#     category_dropdown = ft.Dropdown(
#         label="Category",
#         options=[
#             ft.dropdown.Option("🍔 Food"),
#             ft.dropdown.Option("🚗 Transport"),
#             ft.dropdown.Option("💡 Bills"),
#             ft.dropdown.Option("🛍️ Shopping"),
#         ]
#     )
#     type_radio = ft.RadioGroup(
#         content=ft.Row([
#             ft.Radio(value="income", label="Income"),
#             ft.Radio(value="expense", label="Expense"),
#         ]),
#         value="expense"
#     )

#     history_list = ft.ListView(expand=True, spacing=10)

#     def add_transaction(e):
#         nonlocal total_income, total_expense
        
#         if not amount_input.value or not category_dropdown.value:
#             return

#         amt = float(amount_input.value)
#         cat = category_dropdown.value
#         t_type = type_radio.value

#         if t_type == "income":
#             total_income += amt
#             icon_color = ft.colors.GREEN
#             sign = "+"
#         else:
#             total_expense += amt
#             icon_color = ft.colors.RED
#             sign = "-"

#         net_balance = total_income - total_expense

#         # Update Display
#         balance_text.value = f"Balance: ৳{net_balance:.2f}"
#         income_text.value = f"Income: ৳{total_income:.2f}"
#         expense_text.value = f"Expense: ৳{total_expense:.2f}"

#         # Add to history
#         history_list.controls.insert(0, ft.ListTile(
#             leading=ft.Icon(ft.icons.ATTACH_MONEY, color=icon_color),
#             title=ft.Text(f"{cat}"),
#             subtitle=ft.Text(f"{t_type.capitalize()}"),
#             trailing=ft.Text(f"{sign}৳{amt:.2f}", color=icon_color, weight=ft.FontWeight.BOLD)
#         ))

#         # Clear Inputs
#         amount_input.value = ""
#         page.update()

#     add_btn = ft.ElevatedButton("Add Transaction", on_click=add_transaction, bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE)

#     # Layout Setup
#     page.add(
#         ft.Card(
#             content=ft.Container(
#                 content=ft.Column([
#                     balance_text,
#                     ft.Row([income_text, expense_text], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
#                 ]),
#                 padding=20
#             )
#         ),
#         amount_input,
#         category_dropdown,
#         type_radio,
#         add_btn,
#         ft.Text("Recent History", size=16, weight=ft.FontWeight.BOLD),
#         history_list
#     )

# ft.app(main)
# import flet as ft

# def main(page: ft.Page):
#     page.title = "Expense Tracker"
    
#     # মোবাইল সাইজ লক করা
#     page.window.width = 390
#     page.window.height = 740
#     page.window.resizable = False
    
#     page.theme_mode = ft.ThemeMode.LIGHT
#     page.padding = 15

#     # হিসাব রাখার ভেরিয়েবল
#     total_income = 0.0
#     total_expense = 0.0

#     # UI উপাদানসমূহ
#     balance_text = ft.Text("Balance: Tk 0", size=22, weight=ft.FontWeight.BOLD)
#     income_text = ft.Text("Income: Tk 0", color=ft.Colors.GREEN_600)
#     expense_text = ft.Text("Expense: Tk 0", color=ft.Colors.RED_600)

#     amount_input = ft.TextField(label="Amount (Tk)", keyboard_type=ft.KeyboardType.NUMBER)
#     category_dropdown = ft.Dropdown(
#         label="Category",
#         options=[
#             ft.dropdown.Option("Food"),
#             ft.dropdown.Option("Transport"),
#             ft.dropdown.Option("Bills"),
#             ft.dropdown.Option("Shopping"),
#         ]
#     )
#     type_radio = ft.RadioGroup(
#         content=ft.Row([
#             ft.Radio(value="income", label="Income"),
#             ft.Radio(value="expense", label="Expense"),
#         ]),
#         value="expense"
#     )

#     history_list = ft.ListView(expand=True, spacing=10)

#     def add_transaction(e):
#         nonlocal total_income, total_expense
        
#         if not amount_input.value or not category_dropdown.value:
#             return

#         amt = float(amount_input.value)
#         cat = category_dropdown.value
#         t_type = type_radio.value

#         if t_type == "income":
#             total_income += amt
#             icon_color = ft.Colors.GREEN
#             sign = "+"
#         else:
#             total_expense += amt
#             icon_color = ft.Colors.RED
#             sign = "-"

#         net_balance = total_income - total_expense

#         # আপডেট মেসেজ
#         balance_text.value = f"Balance: Tk {net_balance:.2f}"
#         income_text.value = f"Income: Tk {total_income:.2f}"
#         expense_text.value = f"Expense: Tk {total_expense:.2f}"

#         # হিস্ট্রিতে যোগ করা
#         history_list.controls.insert(0, ft.ListTile(
#             leading=ft.Icon(ft.Icons.ATTACH_MONEY, color=icon_color),
#             title=ft.Text(f"{cat}"),
#             subtitle=ft.Text(f"{t_type.capitalize()}"),
#             trailing=ft.Text(f"{sign} Tk {amt:.2f}", color=icon_color, weight=ft.FontWeight.BOLD)
#         ))

#         amount_input.value = ""
#         page.update()

#     add_btn = ft.ElevatedButton("Add Transaction", on_click=add_transaction, bgcolor=ft.Colors.BLUE_400, color=ft.Colors.WHITE)

#     # স্ক্রিন সাজানো
#     page.add(
#         ft.Card(
#             content=ft.Container(
#                 content=ft.Column([
#                     balance_text,
#                     ft.Row([income_text, expense_text], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
#                 ]),
#                 padding=20
#             )
#         ),
#         amount_input,
#         category_dropdown,
#         type_radio,
#         add_btn,
#         ft.Text("Recent History", size=16, weight=ft.FontWeight.BOLD),
#         history_list
#     )

# # Flet-এর নতুন ভার্সনের জন্য ft.run()
# if __name__ == "__main__":
#     ft.run(main)
import flet as ft

def main(page: ft.Page):
    page.title = "Expense Tracker"
    
    # মোবাইল আকৃতির স্ক্রিন ফিক্সড করা
    page.window.width = 390
    page.window.height = 740
    page.window.resizable = False
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 15

    # হিসাবের ভেরিয়েবল
    total_income = 0.0
    total_expense = 0.0

    # UI কম্পোনেন্ট
    balance_text = ft.Text("Balance: Tk 0", size=22, weight=ft.FontWeight.BOLD)
    income_text = ft.Text("Income: Tk 0", color=ft.Colors.GREEN_600)
    expense_text = ft.Text("Expense: Tk 0", color=ft.Colors.RED_600)

    amount_input = ft.TextField(label="Amount (Tk)", keyboard_type=ft.KeyboardType.NUMBER)
    category_dropdown = ft.Dropdown(
        label="Category",
        options=[
            ft.dropdown.Option("Food"),
            ft.dropdown.Option("Transport"),
            ft.dropdown.Option("Bills"),
            ft.dropdown.Option("Shopping"),
        ]
    )
    type_radio = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="income", label="Income"),
            ft.Radio(value="expense", label="Expense"),
        ]),
        value="expense"
    )

    history_list = ft.ListView(expand=True, spacing=10)

    def add_transaction(e):
        nonlocal total_income, total_expense
        
        if not amount_input.value or not category_dropdown.value:
            return

        amt = float(amount_input.value)
        cat = category_dropdown.value
        t_type = type_radio.value

        if t_type == "income":
            total_income += amt
            icon_color = ft.Colors.GREEN
            sign = "+"
        else:
            total_expense += amt
            icon_color = ft.Colors.RED
            sign = "-"

        net_balance = total_income - total_expense

        # ট্যাক্স বা টেক্সট আপডেট
        balance_text.value = f"Balance: Tk {net_balance:.2f}"
        income_text.value = f"Income: Tk {total_income:.2f}"
        expense_text.value = f"Expense: Tk {total_expense:.2f}"

        # হিস্ট্রি যোগ করা
        history_list.controls.insert(0, ft.ListTile(
            leading=ft.Icon(ft.Icons.ATTACH_MONEY, color=icon_color),
            title=ft.Text(f"{cat}"),
            subtitle=ft.Text(f"{t_type.capitalize()}"),
            trailing=ft.Text(f"{sign} Tk {amt:.2f}", color=icon_color, weight=ft.FontWeight.BOLD)
        ))

        amount_input.value = ""
        page.update()

    # আপডেট করা বাটন (ft.Button)
    add_btn = ft.Button("Add Transaction", on_click=add_transaction, bgcolor=ft.Colors.BLUE_400, color=ft.Colors.WHITE)

    # স্ক্রিনে যুক্ত করা
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    balance_text,
                    ft.Row([income_text, expense_text], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                ]),
                padding=20
            )
        ),
        amount_input,
        category_dropdown,
        type_radio,
        add_btn,
        ft.Text("Recent History", size=16, weight=ft.FontWeight.BOLD),
        history_list
    )

if __name__ == "__main__":
    ft.run(main)