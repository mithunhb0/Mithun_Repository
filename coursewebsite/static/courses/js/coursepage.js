// this is one line of comment
var player;

document.onreadystatechange = function(){
    if(document.readyState == 'interactive'){
        player = document.getElementById("player")
        maintainRatio()
    }
}

function maintainRatio(){
    var w = player.clientwidth
    var h = (w*9)/16
    console.log({ w, h});
    player.height = h
}

window.onresize = maintainRatio
