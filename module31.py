sales_tax = 0.06

def total_tax(total):
    global sales_tax
    total_tax = total * sales_tax
    return total_tax

def totalSale_tax(total):
    totalSale_tax = total_tax(total) + total
    return totalSale_tax
    
    