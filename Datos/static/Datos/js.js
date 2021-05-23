function row () {
    var a = document.getElementById('container');
    a.id = 'row'; 
    
}

function column () {
    var a = document.getElementById('row');
    a.id = 'container'; 
    
}
window.onscroll = function () {
    var y = window.scrollY;
    var foot = document.getElementById('foot-three');
    console.log(y);
    if (y>=600){
        foot.id = 'change';     
    }
    else{
        foot.id = 'foot-three'
    }
    
}