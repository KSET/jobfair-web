<html>
    <head>
        <link href='http://fonts.googleapis.com/css?family=Ubuntu:400,700,300italic,400italic' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Roboto+Slab:400,700' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="style/css/jobfair.css">
        <link rel="stylesheet" href="style/css/textAngular.css">
        <link rel="stylesheet" href="style/css/angular-dropdowns.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    </head>
    <body class="home" ng-app="blogApp">
        <div class="header">
            <div class="inner-header">
                <div class="logo-container">
                    <!--img class="logo-img" src="style/img/logo-sm.png"-->
                    <h1 class="logo-h">JobFair</h1>
                </div>
                
                  <div class="social-container">
                    <a href=""><img src="style/img/yt.png"></a>
                   <a href=""><img src="style/img/fb.png"></a>
                   <a href=""><img src="style/img/tw.png"></a>
                </div>
                
                <div class="option-container">
                    <ul>
                        <li class="addcv">
                            <a href="">predaj životopis</a>
                        </li>
                        <li>
                            <a href="">Za poslodavce</a>
                        </li>
                        
                         <li>
                            <a href="">Sudionici</a>
                        </li>
                         <li>
                            <a href="">Blog</a>
                        </li>
                    </ul>
                </div>
                
              
            </div>
        </div>
        
        <div class="content participants" ng-controller="BlogCtrl">
            <div class="participant" ng-repeat="img in logos">
                <div class="part-holder" ng-click="showFullLogo(img)">
                    <img src="{{img.src}}">
                </div>
            </div>
            
        </div>
                 
        
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.28/angular.min.js"></script>
        <script src="js/vendors/angular-modal-service.js"></script>
        <script src="js/jobfair/module/blogmodule.js"></script>
        <script src="js/jobfair/svc/blogsvc.js"></script>
        <script src="js/jobfair/ctrl/blogctrl.js"></script>
    </body>
</html>