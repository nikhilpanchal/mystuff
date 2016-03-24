/*global APP*/
APP.Components.directive('optionPayoffChart', [
    'managers.Calculator',
    '$rootScope',
    function(calculator, $rootScope) {
        return {
            restrict: 'E',
            template: '<div id="chartContainer"></div>',
            scope: {
                options: '=options'
            },
            link: function(scope, element, attrs) {

                var drawChart = function() {
                    // Calculate the data for the option chart
                    var data = calculator.calculateNewPayOff(scope.options);

                    // Render it out.
                    element.find("#chartContainer").highcharts({
                        chart: {
                            type: 'line',
                            showAxes: false
                        },
                        credits: {
                            enabled: false
                        },
                        title: {
                            text: 'Option Payoff'
                        },
                        xAxis: {
                            title: {
                                text: "Underlying"
                            }
                        },
                        yAxis: {
                            title: {
                                text: 'Payoff'
                            }
                        },
                        series: [{
                            pointStart: 0,
                            data: data
                        }]
                    });
                }
                
                
                drawChart();
            }
        }
    }
]);