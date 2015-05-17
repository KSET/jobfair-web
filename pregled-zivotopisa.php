<html>
    <head>
        <link href='http://fonts.googleapis.com/css?family=Ubuntu:400,700,300italic,400italic' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Roboto+Slab:400,700' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="style/css/jobfair.css">
        <link rel="stylesheet" href="style/css/textAngular.css">
        <link rel="stylesheet" href="style/css/angular-dropdowns.css">
       
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    </head>
    <body class="home" ng-app="cvApp">
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
        
        <div class="content" ng-controller="CvCtrl">
			
			<div class="cvs">
			
			<div class="cv-search">
				<i class="fa fa-search"></i>
				<input type="text" class="cv-field" ng-model="searchTerm" placeholder="Pretraži bazu životopisa">
				<div dropdown-select="searchOptions"
                            dropdown-model="searchVar"
                            dropdown-item-label="text"
							dropdown-onchange="searchVar == 'all' ? searchTerm= searchTerm : searchTerm = searchTerm['searchVar']"
							>
                </div>
			</div>
			<div class="cv-fields">
				<p>Polja u tablici: <a  ng-repeat="field in cvFieldsShown">{{field.placeholder}} <i class="fa fa-remove"></i></a></p>
			</div>
			
			<table class="cv-show">
			<tr><td ng-repeat="shown in cvFieldsShown">{{shown.placeholder}}</td><td></td></tr>
            <tr ng-repeat="cv in cvs | filter:searchTerm">
                <td ng-repeat="shown in cvFieldsShown" ng-bind-html="showSwitch(shown, cv[shown.name])"></td>
                <td ng-click="showFullCv(cv)">više <i class="fa fa-plus-circle"></i></td>
                
            </tr>
           </table>
			</div>
           
            
            
        </div>
                 
        
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.28/angular.min.js"></script>
		<script src="js/vendors/textAngular-rangy.min.js"></script>
        <script src="js/vendors/textAngular-sanitize.js"></script>
        <script src="js/vendors/textAngularSetup.js"></script>
        <script src="js/vendors/textAngular.js"></script>
        <script src="js/vendors/angular-dropdowns.min.js"></script>
        <script src="js/vendors/angular-modal-service.js"></script>
        <script src="js/jobfair/module/cvmodule.js"></script>
        <script src="js/jobfair/svc/cvsvc.js"></script>
        <script src="js/jobfair/ctrl/cvctrl.js"></script>
    </body>
</html>