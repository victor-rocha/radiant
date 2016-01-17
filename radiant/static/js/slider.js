angular
    .module('radiant', [
        'ngSanitize',
        'angular-carousel-3d'
    ])
    .controller('AppController', ['$scope', '$log', '$sce', function($scope, $log, $sce) {
        var vm = this;
        vm.slides = slides;
        console.log(vm.slides);

        vm.options = {
            visible: vm.slides.length,
            perspective: 65,
            startSlide: 0,
            border: 0,
            dir: 'ltr',
            //width: 622,
            //height: 350,
            width: 711,
            height: 400,
            inverseScaling: 400,
            space: 'auto',
            controls: false,
            animationSpeed: 800
        };

        vm.selectedClick = selectedClick;
        vm.slideChanged = slideChanged;
        vm.beforeChange = beforeChange;
        vm.lastSlide = lastSlide;

        vm.trustSrc = function(src) {
            return $sce.trustAsResourceUrl(src);
        };

        function lastSlide(index) {
            $log.log('Last Slide Selected callback triggered. \n == Slide index is: ' + index + ' ==');
        }

        function beforeChange(index) {
            $log.log('Before Slide Change callback triggered. \n == Slide index is: ' + index + ' ==');
        }

        function selectedClick(index) {
            window.location = '/radiant-human/' + $('.current video').attr('id').split('_')[1] + '/';
            $log.log('Selected Slide Clicked callback triggered. \n == Slide index is: ' + index + ' ==');
        }

        function slideChanged(index) {
            // pause all video players
            var video_players = $('video');
            angular.forEach(video_players, function(player) {
                if (!player.paused) {
                    player.pause();
                }
            });
            // play current video
            var video = $('.current video')[0];
            video.play();
            $log.log('Slide Changed callback triggered. \n == Slide index is: ' + index + ' ==');
        }
    }]);
