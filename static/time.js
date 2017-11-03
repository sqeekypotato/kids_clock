$(document).ready(function(){
console.log("read to time!")

var hour = 0;
var tens = 0;
var ones = 0;
var other = '';
var weather_icon = '';
var weather_text = '';
var weather_scale = '';


setInterval(function() {
    getTime = $.post("/");
    getTime.done(function(results){
        checkOnes(results['ones']);
        checkTens(results['tens']);
        checkHours(results['hour']);
        checkOther(results['other']);
//        $("#PM").text(results['PM']);
        checkWeatherIcon(results['weather_symbol']);
        checkWeatherText(results['text']);
        checkWeatherScale(results['temperature_scale'])
        console.log(results['weather_symbol'])
    });
}, 1000); //1 seconds

function checkOnes(value){
    if (value != ones){
    $('#ones').slideToggle('slow', function(){
        if ($(this).is(':hidden')) {$('#ones').text(value);}
    });
    $('#ones').slideToggle('slow');
    ones = value;
    }

}

function checkTens(value){
    if (value != tens){
    $('#tens').slideToggle('slow', function(){
        if ($(this).is(':hidden')) {$('#tens').text(value);}
    });
    $('#tens').slideToggle('slow');
    tens = value;
    }
}

function checkHours(value){
    if (value != hour){
    $('#hour').slideToggle('slow', function(){
        if ($(this).is(':hidden')) {$('#hour').text(value);}
    });
    $('#hour').slideToggle('slow');
    hour = value;
    }
}

function checkOther(value){
    if (value != other){
    $('#other').slideToggle('slow', function(){
        if ($(this).is(':hidden')) {$('#other').text(value);}
    });
    $('#other').slideToggle('slow');
    other = value;
    }
}

function checkWeatherIcon(value){
    if (value != weather_icon){
    $('#weather_icon').html(value);
    weather_icon = value;
    }
}

function checkWeatherText(value){
    if (value != weather_text){
    $('#weather_text').fadeToggle('slow', function(){
        if ($(this).is(':hidden')) {$('#weather_text').text(value);}
    });
    $('#weather_text').fadeToggle('slow');
    weather_text = value;
    }
}

function checkWeatherScale(value){
    if (value != weather_scale){
    $('#temperature_scale').empty().append(value);
    weather_scale = value;
    }
}

});