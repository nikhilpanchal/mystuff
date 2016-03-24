/* global APP */
APP.Services.factory('payoff.calculators.ShortCall', function() {

    return {
        calculateNewPayOff: function(option, stockPrice) {
            var payOff = 0;
            
            option.strike = parseFloat(option.strike);
            option.price = parseFloat(option.price);
            
            // Calculate the payoff
            // If the underlying goes above the strike, the payff is the
            // negative difference
            if(stockPrice > option.strike) {
                payOff = option.strike - stockPrice;
            }
            
            // Add the price since this is a sale of an option
            payOff += option.price;
            
            return payOff;
        }
    };
})