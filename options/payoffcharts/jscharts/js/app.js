/*global angular */
'use strict';
var APP = {};

APP.Controllers = angular.module('Controllers', []);
APP.Services = angular.module('Services', []);
APP.Components = angular.module('Components', []);

APP.Dependencies = [
    'Controllers',
    'Services',
    'Components',
    'ngRoute',
    'ui.bootstrap'
];

APP.Main = angular.module('webplay', APP.Dependencies);

APP.Main.config([
    '$routeProvider', 
    function($routeProvider) {
        $routeProvider.when('/home', {
            templateUrl: '/partials/home-ptl.html'
        }).when('/charts', {
            templateUrl: '/partials/charts-ptl.html'
        }).otherwise({
            redirectTo: 'home'
        })
    }
]);