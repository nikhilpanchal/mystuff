/* global APP*/
APP.Services.factory('payoff.calculators.LongPut', [
    function() {
        return {
            calculateNewPayOff: function(option, stockPrice) {
                var payOff = 0;
                
                // Calculate the payoff
                // If the underlying goes below the strike the payoff is the 
                // difference of the two
                if (stockPrice < option.strike) {
                    payOff += option.strike - stockPrice;
                }
                
                // Subtract the price from the payoff
                payOff -= option.price;
                
                return payOff;
            }
        }
    }
]);