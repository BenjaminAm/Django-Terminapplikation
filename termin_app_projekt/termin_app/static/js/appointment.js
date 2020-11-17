let appointments = document.getElementsByClassName("appointment_link");
for (appointment of appointments) {

}

$('li.appointment_link').mouseover(function(event) {
    createTooltip(event);
}).mouseout(function(){
    // create a hidefunction on the callback if you want
    //hideTooltip();
});

function createTooltip(event){
    $('<div class="tooltip">test</div>').appendTo('body');
    positionTooltip(event);
};

function positionTooltip(event){
    var tPosX = event.pageX - 10;
    var tPosY = event.pageY - 100;
    $('div.tooltip').css({'position': 'absolute', 'top': tPosY, 'left': tPosX});
};