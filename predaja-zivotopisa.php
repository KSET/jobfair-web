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
            <div class="cv-menu">
                <ul class="ul-menu">
                    <li>
                        <a ng-click="scrollTo('osobni')"><i class="fa fa-user"></i> Osobni podaci</a>
                    </li>
                     <li>
                        <a ng-click="scrollTo('obrazovanje')"><i class="fa fa-graduation-cap"></i> Formalno obrazovanje</a>
                        <ul>
                            <li ng-repeat="edu in cv.education"><a ng-click="scrollTo('obrazovanje'+education.indexOf(edu))">{{edu.name}}</a></li>
                        </ul>
                    </li>
                    <li>
                        <a ng-click="scrollTo('posao')"><i class="fa fa-briefcase"></i> Radno iskustvo</a>
                         <ul>
                            <li ng-repeat="wo in cv.work"><a ng-click="scrollTo('posao'+work.indexOf(wo))">{{wo.title}}</a></li>
                        </ul>
                    </li>
                    <li>
                        <a ng-click="scrollTo('jezik')"><i class="fa fa-comment"></i> Znanje jezika</a>
                    </li>
                     <li>
                        <a ng-click="scrollTo('racunalne')"><i class="fa fa-laptop"></i> Računalne vještine</a>
                    </li>
                      <li>
                        <a ng-click="scrollTo('ostale')"><i class="fa fa-info"></i> Ostale vještine</a>
                    </li>
                </ul>
            </div>
            <form class="cv-form">
                <fieldset>
                 <h2 id="osobni"><i class="fa fa-user"></i> Osobni podaci</h2>     
                </fieldset>
               
                <fieldset class="half">
                    <label>Ime*</label>
                    <input type="text" placeholder="Ime" ng-model="cv.name">
                </fieldset>
                
                <fieldset class="half">
                    <label>Prezime*</label>
                    <input type="text" placeholder="Prezime" ng-model="cv.surname">
                </fieldset>
                
                <fieldset class="full">
                    <label>Adresa</label>
                    <input type="text" placeholder="Adresa" ng-model="cv.adress">
                </fieldset>
                
                <fieldset class="half">
                    <label>Poštanski broj</label>
                    <input type="text" placeholder="Poštanski broj" ng-model="cv.zip">
                </fieldset>
                
                 <fieldset class="half">
                    <label>Grad</label>
                    <input type="text" placeholder="Grad" ng-model="cv.city">
                </fieldset>
                 
                <fieldset class="half">
                    <label>Telefon*</label>
                    <input type="text" placeholder="Telefon" ng-model="cv.tel">
                </fieldset>
                
                <fieldset class="half">
                    <label>Email*</label>
                    <input type="text" placeholder="Email" ng-model="cv.email">
                </fieldset>
                
                 <fieldset class="half">
                    <label>Web stranica / blog</label>
                    <input type="text" placeholder="Web stranica / blog" ng-model="cv.web">
                </fieldset>
                 
                 <fieldset class="half">
                    <label>Datum rođenja</label>
                    <input type="text" class="input-day" maxlength="2" placeholder="DD" ng-model="cv.birth.day">
                    <input type="text" class="input-day" maxlength="2" placeholder="MM" ng-model="cv.birth.month">
                    <input type="text" class="input-year" maxlength="4" placeholder="GGGG" ng-model="cv.birth.year">
                </fieldset>
                 <fieldset class="full">
                 <h2 id="obrazovanje"><i class="fa fa-graduation-cap"></i> Formalno obrazovanje</h2>
                 
                 
                 </fieldset>
                 
                 <div class="education" ng-repeat="edu in cv.education">
                     <fieldset class="half" id="obrazovanje{{education.indexOf(edu)}}">
                    <label>Ime obrazovne ustanove</label>
                    <input type="text" placeholder="Ime obrazovne ustanove" ng-model="edu.name">
                    </fieldset>
                    <fieldset class="half">
                    <label>Od</label>
                    <input type="text" class="input-day" maxlength="2" placeholder="DD" ng-model="edu.from.day">
                    <input type="text" class="input-day" maxlength="2" placeholder="MM" ng-model="edu.from.month">
                    <input type="text" class="input-year" maxlength="4" placeholder="GGGG" ng-model="edu.from.year">
                    <a class="remove" ng-click="removeEducation(edu)"><i class="fa fa-trash"></i></a>
                    </fieldset>
                    <fieldset class="half">
                    <label>Godina i smjer</label>
                    <input type="text" placeholder="Godina i smjer" ng-model="edu.year">
                    </fieldset>
                    <fieldset class="half">
                    <label>Do</label>
                     <input type="text" class="input-day" maxlength="2" placeholder="DD" ng-model="edu.to.day">
                    <input type="text" class="input-day" maxlength="2" placeholder="MM" ng-model="edu.to.month">
                    <input type="text" class="input-year" maxlength="4" placeholder="GGGG" ng-model="edu.to.year">
                    
                    </fieldset>

                 </div>
                 <div class="add-block">
                    <a class="add" ng-click="addEducation()"><i class="fa fa-plus-circle"></i></a>
                 </div>
                  
                  
                  <fieldset class="full">
                 <h2 id="posao"><i class="fa fa-briefcase"></i> Radno iskustvo</h2>
                 
                 
                 </fieldset>
                 
                 <div class="education" ng-repeat="wo in cv.work">
                     <fieldset id="posao{{work.indexOf(wo)}}" class="half">
                    <label>Pozicija</label>
                    <input type="text" placeholder="Pozicija" ng-model="wo.title">
                    </fieldset>
                    
                    <fieldset class="half">
                    <label>Od</label>
                    <input type="text" class="input-day" maxlength="2" placeholder="DD" ng-model="wo.from.day">
                    <input type="text" class="input-day" maxlength="2" placeholder="MM" ng-model="wo.from.month">
                    <input type="text" class="input-year" maxlength="4" placeholder="GGGG" ng-model="wo.from.year">
                    <a class="remove" ng-click="removeEmployement(wo)"><i class="fa fa-trash"></i></a>
                    </fieldset>
                    <fieldset class="half">
                    <label>Ime firme</label>
                    <input type="text" placeholder="Ime firme" ng-model="wo.name">
                    </fieldset>
                    <fieldset class="half">
                    <label>Do</label>
                     <input type="text" class="input-day" maxlength="2" placeholder="DD" ng-model="wo.to.day">
                    <input type="text" class="input-day" maxlength="2" placeholder="MM" ng-model="wo.to.month">
                    <input type="text" class="input-year" maxlength="4" placeholder="GGGG" ng-model="wo.to.year">
                    
                    </fieldset>
                    <fieldset class="full">
                         <label>Opis poslova</label>
                        <text-angular ng-model="wo.description"></text-angular>
                    </fieldset>
                 </div>
                  <div class="add-block">
                    <a class="add" ng-click="addEmployement()"><i class="fa fa-plus-circle"></i></a>
                 </div>
                  
                   <fieldset class="full">
                 <h2 id="jezik"><i class="fa fa-comment"></i> Strani jezici</h2>
                 
                 
                 </fieldset>
                 
                 <div class="education" ng-repeat="la in cv.languages">
                     <fieldset class="half">
                    <label>Jezik</label>
                    <input type="text" placeholder="Jezik" ng-model="la.name">
                    </fieldset>
                     <fieldset class="half">
                          <label>Razina znanja</label>
                         <div dropdown-select="ddSelectOptions"
                            dropdown-model="la.val"
                            dropdown-item-label="text">
                        </div>
                           <a class="remove" ng-click="removeLanguage(la)"><i class="fa fa-trash"></i></a>
                     </fieldset>
                     <fieldset class="full"></fieldset>
                 </div>
                <div class="add-block">
                    <fieldset class="full">
                    <a class="add" ng-click="addLanguage()"><i class="fa fa-plus-circle"></i></a>
                    </fieldset>
                 </div>
                
                <fieldset class="full">
                 <h2 id="racunalne"><i class="fa fa-laptop"></i> Računalne vještine</h2>
                 </fieldset>
                 <fieldset class="full">
                     <text-angular ng-model="cv.computers"></text-angular>
                 </fieldset>
                 
                 <fieldset class="full">
                 <h2 id="ostale"><i class="fa fa-info"></i> Ostale vještine</h2>
                 </fieldset>
                 <fieldset class="full">
                     <text-angular ng-model="cv.other"></text-angular>
                 </fieldset>
                 
                 <fieldset class="full">
                <button class="pretty-gumb" ng-click="submitCV()">Predaj životopis!</button>
            </fieldset>
                 
            </form>
            
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