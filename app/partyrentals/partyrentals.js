'use strict';

angular.module('myApp.partyrentals', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/partyrentals', {
    templateUrl: 'partyrentals/partyrentals.html',
    controller: 'partyrentalsCtrl'
  });
}])

.controller('partyrentalsCtrl', [function() {

}]);
