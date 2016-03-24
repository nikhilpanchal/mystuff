/* global APP*/
APP.Services.factory('payoff.calculators.LongCall', function() {
    
    return {
        calculateNewPayOff: function(option, stockPrice) {
            var payoff = 0;
            
            // Calculate the payoff
            // If the underlying is higher than the strike, the payoff is the
            // difference of the two
            if(stockPrice > option.strike) {
                payoff += stockPrice - option.strike;
            }
            
            // Subtract the price from the payoff.
            payoff -= option.price;
            
            return payoff;
        }
    }
})