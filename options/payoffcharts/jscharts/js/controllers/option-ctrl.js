/* global APP */
APP.Controllers.controller('optionCtrl', [
    '$scope',
    '$uibModal',
    '$rootScope',
    function($scope, $uiModal, $rootScope) {
        $scope.options = [];
        $scope.modal = null;
        var option;
        
        function initialize() {
            option = new Option();
            option.side = 'Buy';
            option.type = 'Put';
            option.strike = 0;
            option.price = 1;
            
            $scope.options.push(option);
        }
        
        
        $scope.createLeg = function() {
            $scope.options.push(new Option());
        };
        
        $scope.drawChart = function() {
            $uiModal.open({
               templateUrl: 'partials/modal-ptl.html',
                scope: $scope
            }).result.then(function() {
                console.log("We're closed");
            }, function(error) {
                console.log("We're dismissed ");
            });
        };
        
        initialize();
    }
]);