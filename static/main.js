$(function(){
    var newpage = "?" + ((window.location.href.match(/([^\/]*)\/?$/)[1]).substring(0)) ;
    var NoSelect = true;
    newpage = newpage.replace("?", "/");
     $("ul.nav a").each(function(){
            if($(this).attr("href")==newpage + "/"){
                 $(this).parents().addClass('active');
               $(this).parent().addClass('active');
                NoSelect = false;
            }
        })
     if(NoSelect){
        $("ul.nav > li:first").addClass('active');
     }
})
