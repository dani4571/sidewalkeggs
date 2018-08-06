(function () {
  'use strict';

  angular
    .module('sidewalkeggs.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/register', {
      controller: 'RegisterController',
      controllerAs: 'vm',
      templateUrl: '/authentication/static/templates/authentication/register.html'
    }).otherwise('/');
  }
})();
