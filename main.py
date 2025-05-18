import streamlit as st

# *** Bank Account Class ***
class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.account_number = account_number
        self.balance = balance

    # Debit Money
    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return f"💸 You Withdrawn ${amount} Successfully!!\n💰 Your Remaining Balance is: ${self.balance}"
        else:
            return "🚫 Insufficient Balance .."

    # Credit Money
    def deposit(self, amount: float):
        fee_message = ""
        if amount > 100:
            amount -= 1  # $1 fee for deposits over $100
            fee_message = "💡 Note: A $1 fee has been deducted for deposits over $100."
        self.balance += amount
        return f"💳 You Successfully Deposited ${amount}\n💰 Your Remaining Balance is: ${self.balance}\n{fee_message}"

    # Check Balance
    def check_balance(self):
        return f"💼 Your Current Balance is: ${self.balance}"

# *** Customer Class ***
class Customer:
    def __init__(self, first_name: str, last_name: str, gender: str, age: int, mobile_number: int, account: BankAccount):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.mobile_number = mobile_number
        self.account = account

# *** Create Bank Accounts ***
accounts = [
    BankAccount(1001, 500),
    BankAccount(1002, 1000),
    BankAccount(1003, 1500)
]

# *** Create Customers ***
customers = [
    Customer("Muniza", "Malik", "Female", 25, 3112614571, accounts[0]),
    Customer("Nabeel", "Ahmed", "Male", 26, 3318673523, accounts[1]),
    Customer("Abdul", "Nafay", "Male", 2, 2345678910, accounts[2])
]

# *** Streamlit Interface ***
def service():
    st.title("🏦 Bank Account Management System")

    account_number = st.number_input("🔢 Enter Your Account Number:", step=1, min_value=0)

    customer = next((cust for cust in customers if cust.account.account_number == account_number), None)

    if customer:
        st.success(f"👋 Welcome!!!, {customer.first_name} {customer.last_name}")

        operation = st.selectbox("⚙️ Select An Operation:", ["Deposit", "Withdraw", "Check Balance", "Exit"])

        if operation == "Deposit":
            amount = st.number_input("💵 Enter The Amount To Deposit:", step=0.01, min_value=0.0)
            st.code("💡 Note: A $1 fee will be deducted for deposits over $100.")
            if st.button("✅ Deposit"):
                result = customer.account.deposit(amount)
                st.info(result)

        elif operation == "Withdraw":
            amount = st.number_input("💵 Enter The Amount To Withdraw:", step=0.01, min_value=0.0)
            if st.button("✅ Withdraw"):
                result = customer.account.withdraw(amount)
                st.info(result)

        elif operation == "Check Balance":
            if st.button("🔍 Check Balance"):
                result = customer.account.check_balance()
                st.info(result)

        elif operation == "Exit":
            st.warning("🚪 Exiting Program !!!\n🙏 Thank You For Coming .. Have a Nice Day !!!")

    else:
        if st.button("🔍 Verify Account"):
            st.error("❌ Invalid Account Number.. Please Try Again !!!")

service()
