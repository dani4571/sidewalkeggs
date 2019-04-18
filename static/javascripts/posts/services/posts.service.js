/**
* Posts
* @namespace thinkster.posts.services
*/
(function () {
	'use strict';

	angular
	  .module('sidewalkeggs.posts.services')
	  .factory('Posts', Posts);

	/**
	* @namespace Posts
	* @returns {Factory}
	*/
	function Posts($http) {
		var Posts = {
			all: all,
			create: create,
			get: get
		};

		return Posts;

		////////////////////

		/**
		* @name all
		* @desc Get all Posts
		* @returns {Promise}
		* @memberOf thinkster.posts.services.Posts
		*/
		function all() {
			return $http.get('/api/v1/posts/');
		}

	    /**
	    * @name create
	    * @desc Create a new Post
	    * @param {string} content The content of the new Post
	    * @returns {Promise}
	    * @memberOf thinkster.posts.services.Posts
	    */
	    function create(content) {
	    	return $http.get('/api/v1/accounts/' + username + '/posts/');
	    }

	    /**
		* @name get
		* @desc Get the Posts of a given user
		* @param {string} username The username to get Posts for
		* @returns {Promise}
		* @memberOf thinkster.posts.services.Posts
		*/
		function get(username) {
			return $http.get('/api/v1/accounts/' + username + '/posts/');
		}
	}
})();