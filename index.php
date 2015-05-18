<html>
    <head>
		<title>Jobfair 2015</title>
		<meta name="description"
      content="Job Fair je sajam poslova koji već godinama organiziraju Savez studenata FER-a i KSET. Svim studentima tehnoloških fakulteta pružamo uvid u mogućnosti zaposlenja i razvoja karijere, a tvrtkama koje traže takve radnike omogućavamo izravan kontakt s njihovim budućim zaposlenicima.">
        <meta name="author" content="KSET">
		<meta name="keywords" content="Jobfair, FER, KSET, sajam, posao, poslova, 2015">
		<link href='http://fonts.googleapis.com/css?family=Ubuntu:400,700,300italic,400italic' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Roboto+Slab:400,700' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="style/css/jobfair.css"> 
    </head>
    <body class="home" ng-app="blogApp">
        <div class="header">
            <div class="inner-header">
                <div class="logo-container">
                    <!--img src="style/img/JobFair_logo.png" height="26"-->
                    <a href="/"><h1 class="logo-h">JobFair</h1></a>
                </div>
                
                  <div class="social-container">
                    <a href="https://www.youtube.com/user/KlubKSET" target="_blank"><img src="style/img/yt.png"></a>
                   <a href="https://www.facebook.com/events/1453157368311006/" target="_blank"><img src="style/img/fb.png"></a>
                   <a href="https://twitter.com/JobFair_2011?lang=en" target="_blank"><img src="style/img/tw.png"></a>
                </div>
                
                <div class="option-container">
                    <ul>
                        <!--li class="addcv">
                            <a href="">predaj životopis</a>
                        </li-->
                        <!--li>
                            <a href="">Za poslodavce</a>
                        </li-->
                        
                         <li>
                            <a href="sudionici.php">Sudionici</a>
                        </li>
                         <!--li>
                            <a href="">Blog</a>
                        </li-->
						 <li>
                            <a href="/">Glavna</a>
                        </li>
                    </ul>
                </div>
                
              
            </div>
        </div>
        <div class="blue-block">
			<div class="banner-bg"></div>
            <div class="content">
				
				<div class="banner-container">
					
				</div>
             <div class="left-content">
                <!--img src="style/img/JobFair_logo.png" height="100"-->
                <!--h1 class="page-header">JobFair 2015.</h1-->
               
                <a href="" class="apply-box">predaj životopis</a>
                <div class="text">
                <p>
                    Job Fair je sajam poslova koji već godinama organiziraju Savez studenata FER-a i KSET. Svim studentima tehnoloških fakulteta pružamo uvid u mogućnosti zaposlenja i razvoja karijere, a tvrtkama koje traže takve radnike omogućavamo izravan kontakt s njihovim budućim zaposlenicima. 
                </p>
                <p>
                    Job Fair 2014. održat će se 20. i 21. svibnja na Fakultetu elektrotehnike i računarstva, Unska 3, Zagreb. U glavnoj auli Fakulteta bit će postavljeni štandovi za izlagače, a istovremeno će se u Sivoj vijećnici održavati prezentacije tvrtki.
                </p>
                <p>
                    Lijevo je raspored prezentacija, a na stranici "Sudionici" nalaze se i ovogodišnje tvrtke, kao i sudionici od proteklih godina. Svi zainteresirani mogu na stranici "Životopisi" ostaviti svoje podatke koje prosljeđujemo svim tvrtkama sudionicama i na taj način učiniti prvi korak ka sigurnijoj poslovnoj budućnosti!
                </p>
                </div>
            </div>
            
        <div class="right-content">
                
        <div class="timetable" ng-controller="BlogCtrl">
            <h2>Termini prezentacija</h2>
			<div ng-repeat="day in timetable" class="time-holder">
            <h3>{{day.name}}</h3>
			<table class="times">
                <tbody>
					
		    <tr ng-repeat="time in day.times">
		    <td>{{time.time}}</td>
		    <td><a href="{{time.link}}">{{time.name}}</a></td>
			</tr>
		 
			</tbody>
            </table>
			</div>
        </div>
                
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