/* global APP */

APP.Services.factory('payoff.calculators.ShortPut', function() {
    return {
        calculateNewPayOff: function(option, stockPrice) {
            var payOff = 0;
            
            option.strike = parseFloat(option.strike);
            option.price = parseFloat(option.price);
            
            
            // Calculate the payoff
            // If the underlying goes below the strike, the payoff is the 
            // negative difference of the two
            if(stockPrice < option.strike) {
                payOff = stockPrice - option.strike;
            }
            
            // Add the price since this is a sale
            payOff += option.price;
            
            return payOff;
        }
    };
});