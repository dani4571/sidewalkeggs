(function () {
  'use strict';

  angular
    .module('sidewalkeggs', [
      'sidewalkeggs.config',
      'sidewalkeggs.routes',
      'sidewalkeggs.authentication'
    ]);

  angular
    .module('sidewalkeggs.routes', ['ngRoute']);

  angular
    .module('sidewalkeggs.config', []);

  angular
    .module('sidewalkeggs')
    .run(run);

  run.$inject = ['$http'];

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
