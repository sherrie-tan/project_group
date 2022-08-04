# importing modules 
import api, cash_on_hand, overheads, profit_loss

# defining modules using docstring
def main(): 
    """
    This function will execute the codes in each module and write data 
    into the summary report 
    """
    # assigning api_function to forex with no parameters 
    forex = api.api_function()
    overheads.overhead_function(forex)
    cash_on_hand.cash_on_hand_function(forex)
    profit_loss.profitloss_function(forex)

main()



