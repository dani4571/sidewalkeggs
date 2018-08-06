(function () {
  'use strict';

  angular
    .module('sidewalkeggs.authentication', [
      'sidewalkeggs.authentication.controllers',
      'sidewalkeggs.authentication.services'
    ]);

    angular
      .module('sidewalkeggs.authentication.controllers', []);

    angular
      .module('sidewalkeggs.authentication.services', ['ngCookies']);
})();
