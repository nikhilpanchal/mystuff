/* global APP*/
APP.Services.factory('payoff.calculators.LongUnderlying', function() {
    
    return {
        calculateNewPayOff: function(option, stockPrice) {
            // Calculate the payoff
            // This is simply the difference between the current price of the
            // underlying security and the price at which it was purchased.
            return stockPrice - option.price;
        }
    }
})