/* global APP */
APP.Components.directive('optionLeg', [
    function() {
        return {
            restrict: 'E',
            templateUrl: 'js/components/optionleg/option-leg-ptl.html',
            controller: function($scope) {
                $scope.isStock = function() {
                    return $scope.option.type === 'Stock';
                }
            },
            link: function($scope, elem, attr) {
                elem.find('#side').focus();
            }
        }
    }
])