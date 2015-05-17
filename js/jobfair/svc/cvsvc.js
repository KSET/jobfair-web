cvApp.service('CvSvc', function ($window, $location, $http) {
    
    return({
    submitCV : submitCV,
    getCV:getCV,
    educationToHTML: educationToHTML,
    experienceToHTML: experienceToHTML,
    languageToHTML: languageToHTML
    });
    
    function submitCV(params) {
                
               var promise = $http({
                        contentType:"application/json",
                        dataType:"json",
                        url:"/php/saveCV.php",          
                        processData:false,
                        data: JSON.stringify(params),   
                        headers: {
                            "Content-Type": "application/json"
                        },
                        method:"POST",
                        error:function(e) { alert('error: '+e);}
                     }).then(function(resp) {
                        
                        return resp.data;
                        
                     });

        
        return promise;
   }
   
    function getCV() {
                
               var promise = $http({
                        contentType:"application/json",
                        dataType:"json",
                        url:"/php/showCV.php",          
                        processData:false,  
                        headers: {
                            "Content-Type": "application/json"
                        },
                        method:"GET",
                        error:function(e) { alert('error: '+e);}
                     }).then(function(resp) {
                        
                        return resp.data;
                        
                     });

        
        return promise;
   }
   
   function educationToHTML(obj) {
        obj = JSON.parse(obj);
        l = obj.length;
       
        html= '';
        for(i=0; i<l; i++) {
            html+='<p><b>-'+obj[i].name+'</b>, '+obj[i].year+
            ' ('+obj[i].from.day+'.'+obj[i].from.month+'.'+obj[i].from.year+'.'+' - '+obj[i].to.day+'.'+obj[i].to.month+'.'+obj[i].to.year+'.)<p>'
                
        }
        return html;
   }
   
   function experienceToHTML(obj) {
        obj = JSON.parse(obj);
        l = obj.length;
       
        html= '';
        for(i=0; i<l; i++) {
            html+='<p><b>-'+obj[i].name+', '+obj[i].title+'</b>'+
            ' ('+obj[i].from.day+'.'+obj[i].from.month+'.'+obj[i].from.year+'.'+' - '+obj[i].to.day+'.'+obj[i].to.month+'.'+obj[i].to.year+'.)</p>'+
            obj[i].description;
                
        }
        return html;
   }
   
   function languageToHTML(obj) {
        obj = JSON.parse(obj);
        l = obj.length;
       
        html= '';
        for(i=0; i<l; i++) {
            html+='<p><b>-'+obj[i].name+', </b>'+obj[i].val.text;
            
                
        }
        return html;
   }
    
});