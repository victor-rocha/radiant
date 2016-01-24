angular.module('radiant', [])
    .config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    }])
    .controller('SubscribeCtrl', ['$http', function($http) {
        var sb = this;
        sb.email = '';
        sb.message = 'Press enter to subscribe.';
        sb.helper_error = false;

        sb.subscribe = function() {
            console.log(sb.email);
            if (sb.email) {
                var data = $.param({email: sb.email});
                $http.post('/subscribe/', data).success(function(data){
                    sb.subscribed = true;
                    sb.message = data;
                }).error(function(data) {
                    sb.message = 'Please try again later.';
                    sb.helper_error = true;
                });
            } else {
                sb.message = 'Please enter a valid email address.';
                sb.helper_error = true;
            }
        };
    }]);
