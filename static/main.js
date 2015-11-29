$(function(){
    var link = document.location.href.split('/');
    var newpage = '/' + link[3] + '/'
    var NoSelect = true;

     $("ul.nav a").each(function(){
            if($(this).attr("href")==newpage){
                 $(this).parents().addClass('active');
               $(this).parent().addClass('active');
                NoSelect = false;
            }
        })
     if(NoSelect){
        $("ul.nav > li:first").addClass('active');
     }
})
