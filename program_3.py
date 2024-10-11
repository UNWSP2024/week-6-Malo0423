STATE_TAX = 0.05
COUNTY_TAX = 0.025



def main():
    total_sales = float(input('Enter total sales for the month: '))
    total_state = total_sales * STATE_TAX
    total_county = total_sales * COUNTY_TAX
    total_tax = total_state + total_county

    print(f'The state tax is ${total_state}')
    print(f'The county tax is ${total_county}')
    print(f'The total sales tax is ${total_tax}')

if __name__ == '__main__':
    main()