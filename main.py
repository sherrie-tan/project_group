import api, coh, overheads, profit_loss


def main(): 

    forex = api.apifunction()
    overheads.overhead_function(forex)
    coh.coh_function(forex)
    profit_loss.profitloss_function(forex)

main()