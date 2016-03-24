/*global APP*/
APP.Services.factory('managers.Calculator', [
    'payoff.calculators.LongCall',
    'payoff.calculators.LongPut',
    'payoff.calculators.ShortCall',
    'payoff.calculators.ShortPut',
    'payoff.calculators.LongUnderlying',
    function(longCall,
        longPut,
        shortCall,
        shortPut,
        longUnderlying
    ) {
    
    var payoffCalculatorMap = {
        'BuyCall': longCall,
        'BuyPut': longPut,
        'SellCall': shortCall,
        'SellPut': shortPut,
        'BuyStock': longUnderlying
    };
    
    var DATA_POINTS_COUNT = 101;
    
    return {
        calculateNewPayOff: function(options) {
            var payOff = new Array(DATA_POINTS_COUNT);
            options = options instanceof Array ? options : [options];
            
            for(var stockPrice=0; stockPrice<DATA_POINTS_COUNT; stockPrice++) {
                payOff[stockPrice] = 0;
                
                options.forEach(function(option) {
                    var optionPayOffCalculator = payoffCalculatorMap[option.side + option.type];
                    
                    if(optionPayOffCalculator) {
                        payOff[stockPrice] += optionPayOffCalculator.calculateNewPayOff(option, stockPrice);
                    }
                });
                
                //spayOff[stockPrice] += stockPrice;
            }
            
            return payOff;
        }
    };
}]);