def main():
    while True:
        inp = input('Enter q to quit or any other key to continue: ')
        if inp == 'q':
            break
        sale_price = float(input('Enter price: '))
        down_pay_rate = float(input('Enter percentage of downpayment to be paid upfront: '))
        num_months = float(input('Enter term of loan in months: '))
        apr = float(input('Enter APR: ')) 

        down_payment = sale_price * (down_pay_rate * 0.01) 
        finance_amount = sale_price - down_payment
        apr_percentage = apr // 1200
        monthly_payment = (finance_amount * apr_percentage) / 1 - (1 + apr_percentage) ** -num_months


        print(f'''
Relevant details are as follows:

1. Sale price = ${sale_price}
2. Down payment rate = %{down_pay_rate}
3. Down Payment = ${down_payment}
4. Finance amount = ${finance_amount}
5. APR = %{apr}
6. Number of months = {num_months}
7. Monthly payment = ${monthly_payment}
8. Loan cost = $
9. Total cost = $''')


main()
    

    