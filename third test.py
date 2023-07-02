from Stock import*

def main():
    stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)

    print("Stock information: \n",
          "\nCompany Symbol:", stock.getsymbol(),
          "Company Name:", stock.getname(),
          "\nPrevious Closing Price:", stock.getpreviousprice(),
          "\nCurrent Price:", stock.getcurrentprice(),
          "\nPrice Difference:", stock.getChangepercent())
main()