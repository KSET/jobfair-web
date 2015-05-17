cvApp.controller('ModalController', function($scope, cv, close) {
   $scope.cv = cv;
   if (typeof $scope.cv.education === 'object') {
      
   } else {
      $scope.cv.education = JSON.parse($scope.cv.education);
      $scope.cv.experience = JSON.parse($scope.cv.experience);
      $scope.cv.languages = JSON.parse($scope.cv.languages);
   }
   
   $scope.close = function() {
      close();
      }
});


cvApp.controller('CvCtrl',
  function ($scope, $anchorScroll, $location, $window, CvSvc, ModalService) {
     
      $scope.showSwitch = function(field, val) {
         if (field.type == 'education') {
            return CvSvc.educationToHTML(val);
         } else if (field.type == 'experience') {
            return CvSvc.experienceToHTML(val);
         } else if (field.type == 'languages') {
            return CvSvc.languageToHTML(val);
         } else {
            return val;
         }
         
      }
     
     $scope.submitCV = function() {
      CvSvc.submitCV($scope.cv).then(function(d) {
         })
     }
     
     $scope.cvFields = [{name : 'name', placeholder: 'Ime', type: ''},
                             {name : 'surname', placeholder: 'Prezime' , type: ''},
                             {name : 'city', placeholder: 'Grad', type: ''},
                             {name : 'zip', placeholder: 'ZIP', type: ''},
                             {name : 'adress', placeholder: 'Adresa', type: ''},
                             {name : 'email', placeholder: 'Email', type: ''},
                             {name : 'phone', placeholder: 'Telefon', type: ''},
                             {name : 'web', placeholder: 'Web', type: ''},
                             {name : 'birth', placeholder: 'Rođenje', type: ''},
                             {name : 'education', placeholder: 'Obrazovanje', type: 'education'},
                             {name : 'experience', placeholder: 'Iskustvo', type: 'experience'},
                             {name : 'languages', placeholder: 'Jezici', type: 'languages'}];
     
     $scope.cvFieldsShown = [{name : 'name', placeholder: 'Ime', type: ''},
                             {name : 'surname', placeholder: 'Prezime' , type: ''},
                             {name : 'email', placeholder: 'Email', type: ''},
                             {name : 'phone', placeholder: 'Telefon', type: ''},
                             {name : 'education', placeholder: 'Obrazovanje', type: 'education'},
                             {name : 'experience', placeholder: 'Iskustvo', type: 'experience'}];
     
     
     $scope.addColumn = function(col) {
         index = $scope.cvFields.indexOf(col);
         $scope.cvFields.splice(index, 1);
         $scope.cvFieldsShown.push(col);
     }
     
     $scope.removeColumn = function() {
      
     }
     
     $scope.ddSelectOptions = [
        {
            text: 'A1 - minimalno poznavanje jezika, pripremni stupanj',
            value: 'A1'
        },
         {
            text: 'A2 - osnovno poznavanje jezika, temeljni stupanj',
            value: 'A2'
        }, {
            text: 'B1 - napredni, prijelazni stupanj',
            value: 'B1'
        }, {
            text: 'B2 - samostalni stupanj ',
            value: 'B2'
        }, {
            text: 'C1 - napredni stupanj',
            value: 'C1'
        }, {
            text: 'C2 - skoro materinji jezik, vrsni stupanj',
            value: 'C2'
        }
    ];
     
   $scope.searchOptions = [
      {
            text: 'Sva polja',
            value: 'all'
        },
        {
            text: 'Obrazovanje',
            value: 'education'
        },
         {
            text: 'Radno iskustvo',
            value: 'experience'
        }, {
            text: 'Znanje jezika',
            value: 'languages'
        }, {
            text: 'Računalne vještine',
            value: 'computerskills'
        }, {
            text: 'Ostale vještine',
            value: 'otherskills'
        }
    ];

    $scope.deleteField = function(obj) {
      index = $scope.cvFieldsShown.indexOf(obj);
      $scope.cvFields.push(obj);
    }

  $scope.showFullCv = function(cv) {
   //$window.alert(cv);
    ModalService.showModal({
      templateUrl: "templates/modal.html",
      controller: "ModalController",
      inputs: {
        cv: cv
      }
       })
   
  }
     
   
   
   $scope.scrollTo = function(id) {
      $location.hash(id);
      $anchorScroll();
   }
   
   $scope.addLanguage = function() {
      $scope.cv.languages.push({name: '', val:{
            text: 'A1 - minimalno poznavanje jezika, pripremni stupanj',
            value: 'A1'
        }});
   }
   
   $scope.removeLanguage = function(la) {
        var index = $scope.cv.languages.indexOf(la);
            if (index != -1) {
                $scope.cv.languages.splice(index, 1);
            }
   }
     
     $scope.addEducation = function() {
            $scope.cv.education.push({from : {day: '', month: '', year:''},
                                  to: {day: '', month: '', year:''},
                                  name : '',
                                  year : ''
                                  })
        }
        
        
        $scope.removeEducation = function(edu) {
            var index = $scope.cv.education.indexOf(edu);
            if (index != -1) {
                $scope.cv.education.splice(index, 1);
            }
        }
        
        $scope.addEmployement = function() {
             $scope.cv.work.push({from : {day: '', month: '', year:''},
                                  to: {day: '', month: '', year:''},
                                  name : '',
                                  title : '',
                                  description : ''
                                  })
        }
    
        
        $scope.removeEmployement = function(wo) {
            var index = $scope.cv.work.indexOf(wo);
            if (index != -1) {
            $scope.cv.work.splice(index, 1);
            }
        }
        
       
        
        var init = function() {
            $scope.cv={};
            $scope.cv.education = [];
            $scope.cv.work = [];
            $scope.cv.languages = [];
            $scope.searchVar = {
            text: 'Sva polja',
            value: 'all'
        };
            $scope.searchTerm = '';
            CvSvc.getCV().then(function(d) {
               $scope.cvs = d;
               
            });
        }
        
        init();
  });

