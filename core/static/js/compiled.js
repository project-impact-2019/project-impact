(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
// Shorthand function for calling document.querySelector
function q (selector) {
    return document.querySelector(selector)
}

// Shorthand function for calling document.querySelectorAll
function qAll (selector) {
    return document.querySelectorAll(selector)
}

// Navigation Variables
const hamburger = q('.hamburger');
const navLinks = q('.nav-links');
const links = qAll('.nav-links li');
const newGoal = q('.new_goal')
const newStep = qAll('.new_step')

// Main execution
document.addEventListener('DOMContentLoaded', function() {

    // Hamburger Style Navigation
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle("open");
        links.forEach(link => {
            link.classList.toggle('fade');
        });
    });

});

newGoal.addEventListener('submit', function (e) {
    // e.preventDefault();
    console.log(newGoal)
    $.ajax({
        type: 'POST',
        url: $("#new_goal").attr('action'),
        data: {
            'description': $('.newGoal').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: 'json',
        success: function (data) {
            console.log('Success')
            // $(".goals").load(" .goals")
        }
    });
});


newStep.forEach(item => {
    item.addEventListener('submit', function (e) {
    // e.preventDefault();
    console.log(item.action)
    console.log(item.dataset.goal)
    $.ajax({
        type: 'POST',
        url: item.action,
        data: {
            'goal': item.dataset.goal,
            'step': $(item).find('.newStep').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        // dataType: 'json',
        success: function (data) {
            console.log('Success')
            // $(".goals").load(" .goals")
        }
    });
});
})
},{}]},{},[1]);
