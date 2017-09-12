var techsprinkle =  angular.module('techsprinkle',['ngRoute']);

techsprinkle.config(function($interpolateProvider,$routeProvider,$locationProvider,$httpProvider){
 $locationProvider.hashPrefix('');
$routeProvider
    .when('/', {
        templateUrl: '/static/static-templates/list.html',
        controller: 'displayBlog'
    }).when('/new', {
        templateUrl: '/static/static-templates/new.html',
        controller: 'newBlog'
    }).when('/edit/:hid', {
        templateUrl: '/static/static-templates/edit.html',
        controller: 'editBlog'
    }).otherwise({
        templateUrl : '/static/static-templates/404.html',
    });;
$interpolateProvider.startSymbol('<%');
$interpolateProvider.endSymbol('%>');
$httpProvider.defaults.xsrfCookieName = 'csrftoken';
$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
techsprinkle.factory('blogService', ['$rootScope', function ($rootScope) {
   var blogContent = {
       post_title: "",
       post_description: "",
       hid:""
    };

   return { blogContent:blogContent};
}]);
techsprinkle.controller('displayBlog',['$scope','$http','$location','$routeParams','$rootScope','blogService',function($scope,$http,$location,$routeParams,$rootScope,blogService){
    $scope.blogHome = function(){
        $scope.currentpage = "techsprinkle.in";
        $http({
            method:'GET',
            url:'/blog/getPosts/'
            }).then(function successHandler(response){
                $scope.blogObj = response.data;
            },function errorHandler(response){
                $scope.errorMessage = response.data
            });
        $location.path("/");
    }
    $scope.getPosts = function(){
    $scope.currentpage = "techsprinkle.in";
        $http({
            method:'GET',
            url:'/blog/getPosts/'
            }).then(function successHandler(response){
                $scope.blogObj = response.data;
            },function errorHandler(response){
                $scope.errorMessage = response.data
            });
    }
    $scope.addNew = function(path){
        $scope.currentpage = "Add New Post"
        $location.path("/new");
    }
    $scope.editBlog = function(hid,obj){
    $scope.currentpage = "Edit " +obj.fields.projectname;
    blogService.blogContent.post_title= obj.fields.projectname;
    blogService.blogContent.post_description = obj.fields.description;
    blogService.blogContent.hid =hid;
    $location.path("/edit/"+hid);
    }

     $scope.parJson = function (json) {
            return JSON.parse(json);
    }
        $scope.savePost = function (post_title,post_description) {
        console.log(post_title,post_description);
        $http.defaults.headers.post["Content-Type"] ='application/x-www-form-urlencoded';

        var paramData = { blogtitle: post_title, description: post_description };

        var data = $.param({
                    json: paramData,
                });
                console.log(data);
        $http.post('/blog/savePost/',data ).then(
        function (response){
            Materialize.toast("Blog Added Successfully", 4000)
            $scope.blogObj = response.data;
            $location.path("/");
            $scope.getPosts();

         },
         function (response) {
            console.log("Unable to save Post");
         });
    }
    $scope.deletePost = function (hid) {
        $http.defaults.headers.post["Content-Type"] ='application/x-www-form-urlencoded';

        var paramData = { hid: hid};

        var data = $.param({
                    json: paramData,
                });
                console.log(data);
        $http.post('/blog/deletePost/',data ).then(
        function (response){
            Materialize.toast("Blog Deleted Successfully", 4000)
            $scope.blogObj = response.data;

         },
         function (response) {
            console.log("Unable to Delete Post");
         });
    }
}


]);
techsprinkle.controller('newBlog',['$scope','$http','$location','$routeParams',function($scope,$http,$location,$routeParams,blogService){
$scope.currentpage = "techsprinkle.in";

}]);

techsprinkle.controller('editBlog',['$scope','$http','$location','$routeParams','$rootScope','blogService',function($scope,$http,$location,$routeParams,$rootScope,blogService){
    $scope.currentpage = "Edit " +blogService.blogContent.post_title;
    $scope.post_title = blogService.blogContent.post_title
    $scope.post_description =  blogService.blogContent.post_description
    $scope.hid =  blogService.blogContent.hid;
    $scope.test ="sdaasdas"
$scope.savePost = function (post_title,post_description) {
        console.log($scope.hid,post_title,post_description);
        $http.defaults.headers.post["Content-Type"] ='application/x-www-form-urlencoded';

        var paramData = {hid: $scope.hid, blogtitle: post_title, description: post_description };

        var data = $.param({
                    json: paramData,
                });
                console.log(data);
        $http.post('/blog/editPost/',data ).then(
        function (response){
            Materialize.toast("Blog Edited Successfully", 4000)
            $scope.blogObj = response.data;
            $location.path("/");
            $scope.getPosts();

         },
         function (response) {
            console.log("Unable to Edit Post");
         });
    }
}]);
